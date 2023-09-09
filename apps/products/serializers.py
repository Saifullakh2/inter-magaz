from rest_framework import serializers
from apps.products.models import Product, Like


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'image', 'quantity', 'price', 'country', 'created_at', 'category']
