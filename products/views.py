from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm


def products(request):
    return render(request, 'products/products.html')

def services(request):
    return render(request, 'products/services.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.user = request.user
            comment.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = CommentForm()

    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'form': form})
