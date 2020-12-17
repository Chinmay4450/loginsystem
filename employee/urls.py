from django.urls import path, include
from rest_framework import routers
from .views import empcreateView

router = routers.DefaultRouter()

router.register('', empcreateView, basename='Register')

urlpatterns = [
    path('', include(router.urls)),
   
]