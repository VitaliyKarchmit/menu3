# Generated by Django 3.2.5 on 2023-01-24 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_list', '0003_alter_food_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppingfood',
            name='food_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppings', to='menu_list.food', verbose_name='Блюдо'),
        ),
        migrations.AlterField(
            model_name='toppingfood',
            name='topping_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='top', to='menu_list.topping', verbose_name='Ингредиент'),
        ),
    ]