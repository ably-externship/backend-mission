import random
from django.core.management.base import BaseCommand
from products.models import Product, ProductOption


class Command(BaseCommand):
    help = "This command make Product Options"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", '-n', default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")

        colors = ['white', 'black', 'red', 'green', 'blue']
        # sizes = ['s', 'm', 'l', 'xl']
        # products = Product.objects.all()
        # for product in products:
        #     ProductOption.objects.create(
        #         product=product,
        #         color=lambda x: random.choice(colors),
        #         size=lambda x: random.choice(sizes)
        #     )
        self.stdout.write(self.style.SUCCESS(f"{number} category created"))
