from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Comment, Service, CommentService
from .forms import CommentForm, CommentServiceForm


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


def service_list(request):
    sort_by = request.GET.get('sort', 'created_at')
    if sort_by not in ['created_at', 'price', 'name']:
        sort_by = 'created_at'
    services = Service.objects.all().order_by(sort_by)
    return render(request, 'products/services.html', {'services': services, 'sort_by': sort_by})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    comments = service.comments.all()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentServiceForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.service = service
                comment.user = request.user
                comment.save()
                return redirect('service_detail', pk=service.pk)
        else:
            return redirect('login')
    else:
        form = CommentForm()
    return render(request, 'products/service_detail.html', {'service': service, 'comments': comments, 'form': form})


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('product_detail', pk=comment.product.pk)
    else:
        return redirect('product_detail', pk=comment.product.pk)


def delete_service_comment(request, pk):
    comment = get_object_or_404(CommentService, pk=pk)
    if comment.user == request.user:
        comment.delete()
        return redirect('service_detail', pk=comment.service.pk)
    else:
        return redirect('service_detail', pk=comment.service.pk)
