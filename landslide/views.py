from django.shortcuts import render
from rest_framework import viewsets
from .models import images
from .serializers import imagesSerializers

class imagesview(viewsets.ModelViewSet):
    queryset = images.objects.all()
    serializer_class = imagesSerializers