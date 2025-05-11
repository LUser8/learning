import random
from decimal import Decimal
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from django.utils import lorem_ipsum

from api.models import Category, Product



class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **options):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='@#$asd123')
        
        # create category
        categories = [
            Category(name='Grocery', description=lorem_ipsum.paragraph()),
            Category(name='Health & Beauty', description=lorem_ipsum.paragraph()),
            Category(name='Fashion & Apparel', description=lorem_ipsum.paragraph()),
            Category(name='Electronics', description=lorem_ipsum.paragraph()),
            Category(name='Automotive', description=lorem_ipsum.paragraph())
        ]
        Category.objects.bulk_create(categories)
        categories = Category.objects.all()

        # create products - name, desc, price, stock, image
        products = [
            Product(name="A Scanner Darkly", description=lorem_ipsum.paragraph(), price=Decimal('12.99'), stock=4, category=random.choice(list(categories))),
            Product(name="Coffee Machine", description=lorem_ipsum.paragraph(), price=Decimal('70.99'), stock=6, category=random.choice(list(categories))),
            Product(name="Velvet Underground & Nico", description=lorem_ipsum.paragraph(), price=Decimal('15.99'), stock=11, category=random.choice(list(categories))),
            Product(name="Enter the Wu-Tang (36 Chambers)", description=lorem_ipsum.paragraph(), price=Decimal('17.99'), stock=2, category=random.choice(list(categories))),
            Product(name="Digital Camera", description=lorem_ipsum.paragraph(), price=Decimal('350.99'), stock=4, category=random.choice(list(categories))),
            Product(name="Stationery", description=lorem_ipsum.paragraph(), price=Decimal('500.05'), stock=0, category=random.choice(list(categories))),
            Product(name="Toys", description=lorem_ipsum.paragraph(), price=Decimal('400.05'), stock=0, category=random.choice(list(categories))),
            Product(name="Accessories", description=lorem_ipsum.paragraph(), price=Decimal('350.05'), stock=0, category=random.choice(list(categories))),
            Product(name="Food", description=lorem_ipsum.paragraph(), price=Decimal('50.05'), stock=0, category=random.choice(list(categories))),
            Product(name="Books", description=lorem_ipsum.paragraph(), price=Decimal('100.05'), stock=0, category=random.choice(list(categories))),
            Product(name="Beverages", description=lorem_ipsum.paragraph(), price=Decimal('200.05'), stock=0, category=random.choice(list(categories))),
        ]

        # create products & re-fetch from DB
        Product.objects.bulk_create(products)
        products = Product.objects.all()