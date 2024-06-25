from products.models import Product
from django.shortcuts import render, get_object_or_404, redirect
from .models import CartItem, Cart, Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required



def add_to_cart(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


def cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_item_price = item.product.price * item.quantity
    return render(request, 'orders/cart.html', {'cart_items': cart_items, 'total_price': total_price})


@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sum(item.product.price * item.quantity for item in cart_items)
            order.save()
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity,
                                         price=item.product.price)
                item.delete()
            return redirect('order_success')
    else:
        form = OrderForm()

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_item_price = item.product.price * item.quantity
    return render(request, 'orders/checkout.html', {'form': form, 'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')


def clear_cart(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    cart_items.delete()
    return redirect('cart')

def order_success(request):
    return render(request, 'orders/order_success.html')