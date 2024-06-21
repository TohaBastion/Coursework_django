
from .forms import CommentForm
from main.models import CustomUser
from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(title="Test Post", content="Test Content")
        self.assertTrue(isinstance(post, Post))
        self.assertEqual(post.__str__(), post.title)

class CommentFormTest(TestCase):
    def test_valid_form(self):
        user = CustomUser.objects.create_user(username='testuser', email='qwer@ex.com', password='12345')
        post = Post.objects.create(title="Test Post", content="Test Content")
        data = {'text': 'Test comment'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        comment.post = post
        comment.user = user
        comment.save()
        self.assertEqual(comment.text, 'Test comment')


class PostViewsTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Test Post", content="Test Content")

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)
