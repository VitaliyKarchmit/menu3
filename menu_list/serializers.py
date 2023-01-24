from rest_framework import serializers

from .models import (
    FoodCategory,
)

class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = ['id', 'name', 'is_publish', 'food'] 
        depth = 2       