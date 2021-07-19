from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    STYLES = [
        ("chinese", "Chinese"),
        ("korean", "Korean"),
        ("mexican", "Mexican")
    ]
    style = models.CharField(choices=STYLES, max_length=50)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="menus")
    TIMES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner")
    ]
    time = models.CharField(choices=TIMES, max_length=50)


class Dish(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return str(self.id)