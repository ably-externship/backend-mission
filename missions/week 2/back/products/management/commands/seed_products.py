import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from products.models import Product, Category, ProductOption
from markets.models import Market


class Command(BaseCommand):
    help = "This command make Products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", '-n', default=1, type=int
        )

    def handle(self, *args, **options):
        fake = Faker(["ko_KR"])
        number = options.get("number")
        all_markets = Market.objects.all()
        all_categories = Category.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            Product,
            number,
            {
                "market": lambda x: random.choice(all_markets),
                "category": lambda x: random.choice(all_categories),
                "name": lambda x: fake.unique.bs(),
                "price": lambda x: random.randint(10000, 1000000),
            },
        )
        seeder.execute()

        # create options
        colors = ['white', 'black', 'red', 'green', 'blue']
        sizes = ['s', 'm', 'l', 'xl']
        products = Product.objects.all()

        for product in products:
            color = random.choice(colors)
            size = random.choice(sizes)
            ProductOption.objects.create(
                product=product,
                color=color,
                size=size
            )
        self.stdout.write(self.style.SUCCESS(f"{number} products created"))
