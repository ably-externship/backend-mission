from itertools import product
from django.conf import settings
from django_elasticsearch_dsl import Document, Index
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl.registries import registry
from products.models import BaseMerchandise, Merchandise


# @registry.register_document
# class MerchandiseDocument(Document):
#     class Index:
#         pass
#     class Django:
#         pass