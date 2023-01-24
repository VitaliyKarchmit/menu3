from django.contrib import admin
from . import models

admin.site.register(models.FoodCategory)
admin.site.register(models.Topping)
admin.site.register(models.Food)

