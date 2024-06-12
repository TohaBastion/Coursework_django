from django.db import models
from main.models import CustomUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
