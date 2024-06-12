from django.db import models
from main.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='blog_comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
