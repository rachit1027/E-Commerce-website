from dataclasses import fields
from rest_framework import serializers
from .models import *

class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
       model = QuantityVarient
       fields='__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model = Category
       fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'
        