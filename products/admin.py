from django.contrib import admin
from .models import Product, Comment, Service, CommentService

admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Service)
admin.site.register(CommentService)