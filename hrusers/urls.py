from django.urls import path, include
from rest_framework import routers
from .views import RegisterView,gethrView

router = routers.DefaultRouter()

router.register('register', RegisterView, basename='RegisterView')
router.register('hrs', gethrView, basename='gethrView')

urlpatterns = [
    path('', include(router.urls)),
   
]