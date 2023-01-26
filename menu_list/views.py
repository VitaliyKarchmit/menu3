
from rest_framework import (
    viewsets
)
from django_filters import rest_framework as filters

from .models import (
    FoodCategory, Food, Topping,
)
from .serializers import (
    FoodCategorySerializer,
)    

import operator
from django.db.models import Q
from functools import reduce



class MenuViewSet(viewsets.ModelViewSet):
    """  Список меню, выдает JSON   """

    class MenuFilter(filters.FilterSet):
        is_vegan = filters.CharFilter(method='filter_is_vegan')
        is_special = filters.CharFilter(method='filter_is_special')
        topping_name = filters.CharFilter(method='filter_topping_name')

        def filter_is_vegan(self, queryset, name, value):
            is_vegan = self.request.query_params.get('is_vegan')
            return queryset.filter(food__is_vegan = is_vegan).distinct()

        def filter_is_special(self, queryset, name, value):
            is_special = self.request.query_params.get('is_special')
            return queryset.filter(food__is_special = is_special).distinct()

        def filter_topping_name(self, queryset, name, value):
            topping_name = self.request.query_params.getlist('topping_name')
            query = reduce(operator.or_, (Q(food__topping__name = item) for item in topping_name))
            return queryset.filter(query).distinct()    

        class Meta:
            model = FoodCategory
            fields = '__all__'         

    queryset = FoodCategory.objects.filter(is_publish = True)
    serializer_class = FoodCategorySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = MenuFilter
    







        
    
