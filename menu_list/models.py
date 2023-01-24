from django.db import models

class FoodCategory(models.Model):
    ''' Категория блюда '''

    name = models.CharField(max_length=500, verbose_name='Название категории блюда')
    is_publish = models.BooleanField(verbose_name='Публикуемые', default=True)
    
    class Meta:
        verbose_name = 'Категория блюда'
        verbose_name_plural = 'Категории блюд'
    
    def __str__(self):
        return str(self.id) + ' -- ' + str(self.name) + ' -- ' + str(self.is_publish)



class Topping(models.Model):
    ''' Ингредиенты '''

    name = models.CharField(max_length=500, verbose_name='Название ингредиента')
    
    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
    
    def __str__(self):
        return str(self.id) + ' -- ' + str(self.name) 



class Food(models.Model):
    ''' Блюдо '''

    category_id = models.ForeignKey(FoodCategory, verbose_name='Категория блюда',
                                    related_name='food', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=500, verbose_name='Название блюда')
    description = models.CharField(max_length=2000, verbose_name='Описание блюда')
    price = models.IntegerField(verbose_name='Цена блюда')
    is_special = models.BooleanField(verbose_name='Особое блюдо', default=False)
    is_vegan = models.BooleanField(verbose_name='Вегитарианское блюдо', default=False)
    is_publish = models.BooleanField(verbose_name='Публикуемое блюдо', default=True)
    topping = models.ManyToManyField(Topping, verbose_name='Ингредиенты')
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
    
    def __str__(self):
        return str(self.category_id) + ' -- ' + str(self.name) + ' -- ' + str(self.price) + ' -- ' +\
               str(self.is_special) + ' -- ' + str(self.is_vegan) + ' -- ' + str(self.is_publish)
        