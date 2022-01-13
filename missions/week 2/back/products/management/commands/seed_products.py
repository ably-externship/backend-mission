import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from products.models import Product
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
        colors = ['white', 'black', 'red', 'green', 'blue']
        sizes = ['s', 'm', 'l']
        categories = ['neat', 'hood', 'mtm', 'shirt']
        seeder = Seed.seeder()
        seeder.add_entity(
            Product,
            number,
            {
                "market": lambda x: random.choice(all_markets),
                "name": lambda x: fake.unique.bs(),
                "price": lambda x: random.randint(10000, 1000000),
                "color": lambda x: random.choice(colors),
                "size": lambda x: random.choice(sizes),
                "category": lambda x: random.choice(categories),
                "stock": lambda x: random.randint(0, 1000),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} products created"))
