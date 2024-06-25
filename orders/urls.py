from django.urls import path
from .views import add_to_cart, cart, checkout, remove_from_cart, clear_cart, order_success

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/clear/', clear_cart, name='clear_cart'),
    path('order_success/', order_success, name='order_success'),
]
