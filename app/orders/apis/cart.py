from rest_framework.exceptions import APIException, ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from ..cart import Cart
from ..forms import CartItemAddForm, CartItemRemoveForm
from ..serializers import CartSerializer

__all__ = (
    'CartAPIView',
)


class CartAPIView(APIView):
    def get(self, request):
        cart = Cart(request)
        return Response(CartSerializer(cart).data)

    def post(self, request):
        form = CartItemAddForm(request.data)
        if form.is_valid():
            cart = form.save(request)
            return Response(CartSerializer(cart).data)
        raise ValidationError(form.errors)

    def delete(self, request):
        form = CartItemRemoveForm(request.data)
        if form.is_valid():
            cart = form.save(request)
            return Response(CartSerializer(cart).data)
