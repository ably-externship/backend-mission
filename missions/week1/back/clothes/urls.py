from django.urls import path
from . import views

app_name = "clothes"

urlpatterns = [
    path("uppers/", views.Uppers_views, name="upper_list"),
    path("outers/", views.Outers_views, name="outer_list"),
    path("onepieces/", views.Onepieces_views, name="onepiece_list"),
    path("uppers/int:<pk>/", views.Upper_detail, name="upper_detail"),
    path("outers/int:<pk>/", views.Outer_detail, name="outer_detail"),
    path("onepieces/int:<pk>/", views.Onepiece_detail, name="onepiece_detail"),
    path("search/", views.search, name="search"),
]
