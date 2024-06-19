from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment
from .forms import CommentForm


def product_list(request):
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by not in ['created_at', 'price', 'name']:
        sort_by = 'created_at'
    products = Product.objects.all().order_by(sort_by)
    return render(request, 'products/products.html', {'products': products, 'sort_by': sort_by})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    comments = product.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.product = product
                comment.user = request.user
                comment.save()
                return redirect('product_detail', pk=product.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    return render(request, 'products/product_detail.html', {'product': product, 'comments': comments, 'form': form})
