from django.db import models
from main.models import CustomUser


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/image/products/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(Product):
    service_id = models.AutoField(primary_key=True)


class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Коментар від {self.user.username} про {self.product.name}'


class CommentService(Comment):
    service = models.ForeignKey(Service, related_name='comments', on_delete=models.CASCADE)
