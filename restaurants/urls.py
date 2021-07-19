from django.urls import path
from .views import *

urlpatterns = [
    path('', RestaurantListView.as_view(), name="rest_list"),
    path('<int:rest_id>/', RestaurantDetailView.as_view(), name="rest_detail"),

    path('<int:rest_id>/menus/', MenuListView.as_view(), name="menu_list"),
    path('<int:rest_id>/menus/<int:menu_id>/', MenuDetailView.as_view(), name="menu_detail"),

    path('<int:rest_id>/menus/<int:menu_id>/dishes/', DishListView.as_view(), name="dish_list" ),
    path('<int:rest_id>/menus/<int:menu_id>/dishes/<int:dish_id>/', DishDetailView.as_view(), name="dish_detail" ),
    path('<int:rest_id>/menus/<int:menu_id>/dishes/new/', DishCreateView.as_view(), name="dish_create" ),
]