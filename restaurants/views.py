from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Restaurant, Menu, Dish



class RestaurantListView(ListView):
    model = Restaurant
    template_name = "restaurants/restaurant_list.html"
    context_object_name = "info"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Restaurant List"
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurants/restaurant_detail.html"
    context_object_name = "i"
    pk_url_kwarg = "rest_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Restaurant Detail"
        return context


class MenuListView(ListView):
    model = Menu
    template_name = "restaurants/menu_list.html"
    context_object_name = "info"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Menu List"
        context["rest_id"] = self.kwargs["rest_id"]
        return context

    def get_queryset(self):
        rest_id = self.kwargs["rest_id"]
        return Menu.objects.filter(restaurant__id=rest_id)

class MenuDetailView(DetailView):
    model = Menu
    "restaurants/menu_detail.html"
    pk_url_kwarg = "menu_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Menu Detail"
        return context

    def get_object(self):
        menu_id = self.kwargs["menu_id"]
        Menu.objects.get(pk=menu_id)
        return Menu.objects.get(pk=menu_id)
    

class DishListView(ListView):
    model = Dish
    template_name = "restaurants/dish_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Dish List"
        context["rest_id"] = self.kwargs["rest_id"]
        context["menu_id"] = self.kwargs["menu_id"]
        return context

    def get_queryset(self):
        menu_id = self.kwargs["menu_id"]
        return Dish.objects.filter(menu__id=menu_id)


class DishDetailView(DetailView):
    model = Dish
    template_name = "restaurants/dish_detail.html"
    pk_url_kwarg = "dish_id"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Dish List"
        return context

    def get_object(self):
        dish_id = self.kwargs["dish_id"]
        return Dish.objects.get(pk=dish_id)

class DishCreateView(CreateView):
    model = Dish
    template_name = "restaurants/dish_create.html"
    fields = ("name", "price")

    def form_valid(self, form):
        form = form.save(commit=False)
        form.menu = Menu.objects.get(pk=self.kwargs["menu_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('dish_list', kwargs={"rest_id": self.kwargs['rest_id'], "menu_id": self.kwargs["menu_id"]})