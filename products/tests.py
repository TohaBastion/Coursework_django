import unittest
from products.models import Product

class ProductModelTest(unittest.TestCase):

    def test_product_creation(self):
        product = Product.objects.create(name='Test Product', description='Test Description', price=100.0)
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(product.price, 100.0)