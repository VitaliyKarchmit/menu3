from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import (
    FoodCategory,  Food, Topping, ToppingFood
)
from .views import MenuViewSet



class MenuViewSetTest(APITestCase):
   '''  Тест API MenuViewSet   '''

   def test_menu_list(self):
      
      # формируем данные
      category = FoodCategory.objects.create(name='Категория ТЕСТ')
      food = Food.objects.create(category_id = category,
                                 name = 'Блюдо ТЕСТ',
                                 description = 'Описание блюда ТЕСТ',
                                 price = 100)

      topping = Topping.objects.create(name='Ингридиент ТЕСТ')
      ToppingFood.objects.create(food_id = food,
                                 topping_id = topping)         

      # получаем данные для проверки
      url = reverse('menu-list')
      request = self.client.get(url, format='json')
      self.assertEqual(request.status_code, status.HTTP_200_OK)

      # проверяем данные
      self.assertEqual(request.data[0]['id'], 1) 
      self.assertEqual(request.data[0]['name'], 'Категория ТЕСТ') 
      self.assertEqual(request.data[0]['is_publish'], True) 

      self.assertEqual(request.data[0]['foods'][0]['id'], 1) 
      self.assertEqual(request.data[0]['foods'][0]['category_id'], 1) 
      self.assertEqual(request.data[0]['foods'][0]['name'], 'Блюдо ТЕСТ') 
      self.assertEqual(request.data[0]['foods'][0]['description'], 'Описание блюда ТЕСТ') 
      self.assertEqual(request.data[0]['foods'][0]['is_publish'], True) 
      self.assertEqual(request.data[0]['foods'][0]['is_special'], False) 
      self.assertEqual(request.data[0]['foods'][0]['is_vegan'], False)       
      self.assertEqual(request.data[0]['foods'][0]['price'], 100)

      self.assertEqual(request.data[0]['foods'][0]['toppings'][0]['id'], 1) 
      self.assertEqual(request.data[0]['foods'][0]['toppings'][0]['name'], 'Ингридиент ТЕСТ') 
