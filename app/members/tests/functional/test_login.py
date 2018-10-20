import time

import selenium.webdriver.support.ui as ui
from django.contrib.auth import get_user_model
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium.common.exceptions import WebDriverException

from utils.functions import get_browser

User = get_user_model()


class LoginTestCase(StaticLiveServerTestCase):
    URL_LOGIN = reverse('members:login')
    TEST_USERNAME = 'test_username'
    TEST_PASSWORD = 'test_password'
    TEST_LAST_NAME = '홍'
    TEST_FIRST_NAME = '길동'

    def create_test_user(self):
        return User.objects.create_user(
            username=self.TEST_USERNAME,
            password=self.TEST_PASSWORD,
            last_name=self.TEST_LAST_NAME,
            first_name=self.TEST_FIRST_NAME,
        )

    def setUp(self):
        self.browser = get_browser(no_options=True)
        self.browser.switch_to_window(self.browser.current_window_handle)

    def tearDown(self):
        self.browser.quit()

    def test_login(self):
        # 테스트용 유저 생성
        self.create_test_user()
        print(User.objects.all())
        # 메인페이지 접근
        self.browser.get(self.live_server_url)
        wait = ui.WebDriverWait(self.browser, 1)

        # DDT툴바 있으면 숨겨줌
        try:
            debug_hide_button = self.browser.find_element_by_css_selector('a#djHideToolBarButton')
            debug_hide_button.click()
        except WebDriverException:
            pass

        # 계정 버튼 선택자
        selector_account_btn = '.toolbar > .inner > a.toolbar-toggle.account-toggle'
        # 계정 버튼 클릭
        wait.until(lambda driver: driver.find_element_by_css_selector(selector_account_btn))
        self.browser.find_element_by_css_selector(selector_account_btn).click()

        # 나오는 창에서 username, password입력 후 로그인 버튼 클릭
        selector_login_form = 'form#login-form'
        wait.until(lambda driver: driver.find_element_by_css_selector(selector_login_form))
        form = self.browser.find_element_by_css_selector('form#login-form')
        input_username = form.find_element_by_css_selector('input#input-username')
        input_password = form.find_element_by_css_selector('input#input-password')
        btn_submit = form.find_element_by_css_selector('button[type=submit]')
        input_username.send_keys(self.TEST_USERNAME)
        input_password.send_keys(self.TEST_PASSWORD)
        btn_submit.click()

        # 로그인 처리 후 다시 로그인 버튼 나올때까지 기다림
        wait.until(lambda driver: driver.find_element_by_css_selector(selector_account_btn))
        btn_account = self.browser.find_element_by_css_selector(selector_account_btn)
        # 로그인 버튼에 현재 로그인 한 사용자의 이름이 나오는지 확인
        self.assertEqual(
            f'{self.TEST_LAST_NAME}{self.TEST_FIRST_NAME}',
            btn_account.text,
        )
        time.sleep(10)
