import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Courswork_django.settings')
django.setup()

from main.models import CustomUser
from products.models import Product, Comment

fake = Faker()


def create_users(n):
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = '+380' + fake.msisdn()[3:12]
        password = 'password123'
        CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            password=password
        )


def create_products(n):
    for _ in range(n):
        name = fake.word().capitalize()
        description = fake.text()
        price = round(random.uniform(10.0, 1000.0), 2)
        photo = 'static/images/products/photo.jpg'
        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=photo
        )

        users = CustomUser.objects.all()
        for _ in range(random.randint(1, 5)):
            Comment.objects.create(
                user=random.choice(users),
                product=product,
                text=fake.text()
            )


# create_users(10)
create_products(10)
