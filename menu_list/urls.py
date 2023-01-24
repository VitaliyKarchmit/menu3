from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'menu', views.MenuViewSet, basename='menu')

urlpatterns = [
    path('', include(router.urls)),
]
