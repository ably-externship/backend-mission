from django.urls import path,include
"""
ENDPOINT : api/

"""
app_name = 'rest_api'
urlpatterns = [
    path('product/',include('product.api.urls')),
    path('account/',include('account.api.urls')),
    
]