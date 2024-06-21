from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserModelTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='ex@ex.com', password='testpassword')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(username='admin', email='ex@ex.com', password='adminpassword')
        self.assertEqual(admin_user.username, 'admin')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)