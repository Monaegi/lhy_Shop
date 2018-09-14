from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Product, ProductCategory

User = get_user_model()

TEST_USERNAME = 'test_username'
TEST_PRODUCT_CATEGORY_TITLE = 'test_category'
TEST_PRODUCT_TITLE = 'test_product'
TEST_PRODUCT_OPTIONS = [
    {
        'title': 'test_option_1',
        'unit': 100,
        'price': 3,
    },
    {
        'title': 'test_option_2',
        'unit': 200,
        'price': 5.5,
    }
]


class CartAPITest(APITestCase):
    URL = reverse('api:orders:cart')

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.get_or_create(
            username=TEST_USERNAME,
        )
        category = ProductCategory.objects.create(title=TEST_PRODUCT_CATEGORY_TITLE)
        cls.product = Product.objects.create(
            category=category,
            title=TEST_PRODUCT_TITLE,
        )
        for data_product_option in TEST_PRODUCT_OPTIONS:
            cls.product.option_set.create(**data_product_option)

    @staticmethod
    def make_test_user():
        return User.objects.get_or_create(
            username=TEST_USERNAME,
        )

    def test_anonymous_user_get_cart(self):
        response = self.client.get(self.URL)
        self.assertDictEqual({'items': [], 'amount': 0}, response.data)

    def test_signup_user_get_blank_cart(self):
        user = self.make_test_user()
        self.client.force_authenticate(user)
        response = self.client.get(self.URL)
        self.assertDictEqual({'items': [], 'amount': 0}, response.data)

    def test_cart_item_add(self):
        user = self.make_test_user()
        self.client.force_authenticate(user)
        data1 = {
            'product_option': self.product.option_set.all()[0].pk,
            'quantity': 3,
        }
        response = self.client.post(self.URL, data1)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(
            response.data['items'][0]['product_option']['pk'],
            self.product.option_set.all()[0].pk,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['items'][0]['quantity'], 3)

        data2 = {
            'product_option': self.product.option_set.all()[1].pk,
            'quantity': 5,
        }
        response = self.client.post(self.URL, data2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data['items']), 2)
        self.assertEqual(
            response.data['items'][1]['product_option']['pk'],
            self.product.option_set.all()[1].pk,
        )
        self.assertEqual(response.data['items'][1]['quantity'], 5)

    def test_cart_item_add_exception(self):
        # product_option이 빠진 경우
        data_except_product_option = {
            'quantity': 1,
        }
        response = self.client.post(self.URL, data_except_product_option)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('product_option', response.data)

        # quantity가 빠진 경우
        data_except_quantity = {
            'product_option': self.product.option_set.first().pk,
        }
        response = self.client.post(self.URL, data_except_quantity)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('quantity', response.data)

    def test_cart_item_delete(self):
        data_add = {
            'product_option': self.product.option_set.all()[0].pk,
            'quantity': 3,
        }
        response = self.client.post(self.URL, data_add)
        self.assertEqual(len(response.data['items']), 1)

        data_delete = {
            'product_option': self.product.option_set.all()[0].pk,
        }
        response = self.client.delete(self.URL, data_delete)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['items']), 0)

    def test_cart_item_delete_exception(self):
        # product_option을 지정하지 않은 경우
        data_except_product_option = {}
        response = self.client.delete(self.URL, data_except_product_option)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('product_option', response.data)
