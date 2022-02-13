from django.core.management.base import BaseCommand
from cart.models import Order
from sales.models import MarketDailySales,ProductDailySales
from datetime import datetime
from collections import defaultdict
import datetime as dt
class Command(BaseCommand):
    
    def handle(self, *args, **options) :
        # 전 날 목록 
        yesterday = datetime.now().date()-dt.timedelta(days=1)
        
        # start_date : 어제, end_date:오늘
        start_date ,end_date = datetime.now().date(),datetime.now().date()+dt.timedelta(days=1)
        # orders = Order.objects.select_related('product','realproduct').filter(purchase_date__range = [yesterday,datetime.now().date()])
        test_orders = Order.objects.select_related('product','realproduct').filter(purchase_date__range = [start_date,end_date]).filter(is_checked=False)
        # 기본값 0
        D_product = defaultdict(int) # 상품 갯수
        D_sales = defaultdict(int) # 팔린 상품 매출
        market_product = defaultdict(int)
        market_sales = defaultdict(int)
        for order in test_orders:
            # 전체 제품별
            D_product[order.product] += order.product_num
            D_sales[order.product] += order.total_price
            # 마켓별
            market_product[order.market] += order.product_num
            market_sales[order.market]  += order.total_price
            order.is_checked = True
            order.save()
        
        for product in D_product:
            ProductDailySales.objects.create(
                date = start_date,
                product = product,
                sales = D_sales[product],
                sales_num = D_product[product],
            )


        for market in market_product:
            MarketDailySales.objects.create(
                date = start_date,
                sales = market_sales[market],
                sales_num = market_sales[market],
            )



            