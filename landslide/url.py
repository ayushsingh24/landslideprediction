from landslide.models import images
from django import urls
from . import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('images',views.imagesview,basename='Images')

urlpatterns = [
    path('',include(router.urls))
]