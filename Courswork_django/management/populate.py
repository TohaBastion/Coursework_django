import os
import django
import random
from django.contrib.auth import get_user_model
from faker import Faker
from blog.models import Post, Comment
from main.models import CustomUser
# from products.models import Product, Comment, Service, CommentService


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Courswork_django.settings')
django.setup()



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


def create_services(n):
    for _ in range(n):
        name = fake.word().capitalize()
        description = fake.text()
        price = round(random.uniform(10.0, 1000.0), 2)
        photo = 'static/images/products/all-metalic.jpg'
        service = Service.objects.create(
            name=name,
            description=description,
            price=price,
            image=photo
        )

        users = CustomUser.objects.all()
        for _ in range(random.randint(1, 5)):
            CommentService.objects.create(
                user=random.choice(users),
                service=service,
                text=fake.text()
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


def create_blog_posts_and_comments(n_posts, n_comments):
    users = list(CustomUser.objects.all())
    for _ in range(n_posts):
        post = Post.objects.create(
            title=fake.sentence(),
            content=fake.text()
        )
        for _ in range(n_comments):
            Comment.objects.create(
                post=post,
                user=random.choice(users),
                text=fake.text()
            )


create_users(10)
create_products(10)
create_services(10)
create_blog_posts_and_comments(10, 3)
