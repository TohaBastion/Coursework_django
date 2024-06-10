from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
]