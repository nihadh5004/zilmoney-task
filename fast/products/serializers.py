from rest_framework import serializers
from .models import *



class ProductInfo(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class PurchaseInfo(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'


