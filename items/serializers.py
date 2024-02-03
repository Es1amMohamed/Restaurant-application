from rest_framework import serializers
from .models import *

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        exclude = ['slug']
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'