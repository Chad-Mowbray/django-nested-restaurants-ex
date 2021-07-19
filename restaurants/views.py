from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Restaurant, Menu, Dish



class RestaurantListView(ListView):
    pass

class RestaurantDetailView(DetailView):
    pass




class MenuListView(ListView):
    pass

class MenuDetailView(DetailView):
    pass




class DishListView(ListView):
    pass


class DishDetailView(DetailView):
    pass

class DishCreateView(CreateView):
    pass