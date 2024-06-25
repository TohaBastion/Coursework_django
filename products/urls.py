from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('services/', views.service_list, name='services'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('comment/service/<int:pk>/delete/', views.delete_service_comment, name='delete_service_comment'),
]
