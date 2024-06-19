from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    # path('services/', views.services, name='services'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
