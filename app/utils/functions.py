import subprocess

from selenium import webdriver

__all__ = (
    'get_browser',
)


def get_browser(no_options=False, *args):
    chromedriver_location = subprocess.run(
        ['which', 'chromedriver'],
        stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    options = webdriver.ChromeOptions()
    if not no_options:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('disable-gpu')
    for arg in args:
        options.add_argument(arg)
    client = webdriver.Chrome(chromedriver_location, chrome_options=options)
    return client
