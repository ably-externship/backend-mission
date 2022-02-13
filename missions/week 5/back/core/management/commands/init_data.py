import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from faker import Faker

from products.models import Product, Category, ProductOption
from markets.models import Market
from accounts.models import User


class Command(BaseCommand):
    help = "This command make init data"

    def handle(self, *args, **options):
        users = [
            User(email='test1@test.com', password='qwer1234!'),
            User(email='test2@test.com', password='qwer1234!'),
            User(email='test3@test.com', password='qwer1234!'),
            User(email='test4@test.com', password='qwer1234!'),
            User(email='test5@test.com', password='qwer1234!'),
            User(email='test6@test.com', password='qwer1234!'),
            User(email='test7@test.com', password='qwer1234!'),
            User(email='test8@test.com', password='qwer1234!'),
            User(email='test9@test.com', password='qwer1234!'),
            User(email='test10@test.com', password='qwer1234!'),
            User(email='test11@test.com', password='qwer1234!'),
        ]
        User.objects.bulk_create(users)

        markets = [
            Market(name='market1', owner=User.objects.get(email='test1@test.com')),
            Market(name='market2', owner=User.objects.get(email='test2@test.com')),
            Market(name='market3', owner=User.objects.get(email='test3@test.com')),
            Market(name='market4', owner=User.objects.get(email='test4@test.com')),
            Market(name='market5', owner=User.objects.get(email='test5@test.com')),
            Market(name='market6', owner=User.objects.get(email='test6@test.com')),
            Market(name='market7', owner=User.objects.get(email='test7@test.com')),
            Market(name='market8', owner=User.objects.get(email='test8@test.com')),
            Market(name='market9', owner=User.objects.get(email='test9@test.com')),
            Market(name='market10', owner=User.objects.get(email='test10@test.com')),
            Market(name='market11', owner=User.objects.get(email='test11@test.com'))
        ]
        Market.objects.bulk_create(markets)
        categories = [
            Category(name='top'),
            Category(name='pants'),
            Category(name='one piece'),
            Category(name='outer'),
            Category(name='training'),
            Category(name='shoes'),
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS(f"Create init data successfully"))
