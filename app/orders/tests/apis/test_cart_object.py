from django.contrib.sessions.middleware import SessionMiddleware
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from orders.cart import Cart


class CartObjectTestCase(TestCase):
    URL_INDEX = reverse('index')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.factory = RequestFactory()

    def test_unique_cart_per_request_session(self):
        request1 = self.factory.get(self.URL_INDEX)
        request2 = self.factory.get(self.URL_INDEX)
        middleware = SessionMiddleware()
        middleware.process_request(request1)
        middleware.process_request(request2)

        cart1 = Cart(request1)
        cart1_same_request = Cart(request1)
        cart2 = Cart(request2)

        self.assertNotEqual(cart1.session, cart2.session)
        self.assertEqual(cart1.session, cart1_same_request.session)

    def test_init_removed_product_option_key_delete(self):
        """
        장바구니에 존재하던 아이템 중, 서버에서 삭제된 아이템은 장바구니에서 자동으로 지워지는지 테스트
        :return:
        """
