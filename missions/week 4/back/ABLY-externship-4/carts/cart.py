from django.conf import settings
from decimal import Decimal
from products.models import BaseMerchandise, Merchandise

# Create your views here.


class Cart(object):
    
    
    def __init__(self, request):
        
        self.session = request.session
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID] = {}
        self.cart = cart
    
    
    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())
    
    
    def __iter__(self):
        
        merchandises_ids = self.cart.keys()
        merchandises = Merchandise.objects.filter(id__in=merchandises_ids)
        for merchandise in merchandises:
            self.cart[str(merchandise.id)]['merchandise'] = merchandise
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * int(item['quantity'])
            yield item
    
    
    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True
    
    def add(self, merchandise, quantity=1, is_updated=False):
        
        merchandise_id = str(merchandise.id)
        basemerchandise = BaseMerchandise.objects.get(id=str(merchandise.basemerchandise))
        price = int(basemerchandise.standard_price) - int(basemerchandise.discounted_price)
        
        if merchandise_id not in self.cart:
            self.cart[merchandise_id] = {
                'quantity': 0,
                'color': str(merchandise.color),
                'price': str(price)
            }
        
        if is_updated:
            self.cart[merchandise_id]['quantity'] = int(quantity)
        else:
            self.cart[merchandise_id]['quantity'] += int(quantity)
        self.save()
    
    
    def update(self, merchandise_id, quantity):
        if merchandise_id in self.cart:
            self.cart[merchandise_id]['quantity'] = quantity
            self.save()
    
    
    def delete(self, merchandise_id):
        
        if merchandise_id in self.cart:
            del(self.cart[merchandise_id])
            self.save()
    
    
    def clear(self):
        
        self.session[settings.CART_ID] = {}
        self.session.modified = True
    
    
    def get_product_total(self):
        return sum(Decimal(item['price'])*int(item['quantity']) for item in self.cart.values())