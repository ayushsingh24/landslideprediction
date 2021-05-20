from rest_framework import serializers
from .models import images

class imagesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = images
        fields = ('moisture','slope','output')