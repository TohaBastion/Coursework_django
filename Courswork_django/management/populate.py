import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Courswork_django.settings')
django.setup()

from main.models import CustomUser
from products.models import Product, Service
from blog.models import Post, Comment

fake = Faker()


def create_users(n):
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        password = "password123"
        first_name = fake.first_name()
        last_name = fake.last_name()
        phone_number = "+380" + "".join(random.choices("0123456789", k=9))

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        print(f"Created user: {username}")


def create_products(n):
    for _ in range(n):
        name = fake.word().capitalize()
        description = fake.text(max_nb_chars=200)
        price = round(random.uniform(10.0, 100.0), 2)
        image = fake.image_url()

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            image=image
        )
        print(f"Created product: {name}")


def create_services(n):
    for _ in range(n):
        name = fake.word().capitalize()
        description = fake.text(max_nb_chars=200)
        price = round(random.uniform(50.0, 500.0), 2)

        service = Service.objects.create(
            name=name,
            description=description,
            price=price
        )
        print(f"Created service: {name}")


def create_blog_posts(n):
    users = list(CustomUser.objects.all())
    for _ in range(n):
        title = fake.sentence(nb_words=6)
        content = fake.text(max_nb_chars=1000)
        published_date = fake.date_time_this_year()

        post = Post.objects.create(
            title=title,
            content=content,
            published_date=published_date
        )
        print(f"Created post: {title}")

        for _ in range(3):  # Creating 3 comments per post
            user = random.choice(users)
            text = fake.text(max_nb_chars=200)
            created_at = fake.date_time_this_year()

            comment = Comment.objects.create(
                post=post,
                user=user,
                text=text,
                created_at=created_at
            )
            print(f"Created comment by {user.username} on {post.title}")


if __name__ == "__main__":
    create_users(10)
    create_products(10)
    create_services(10)
    create_blog_posts(10)
