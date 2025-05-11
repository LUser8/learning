from rest_framework import serializers
from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Product
        fields = ('category', 'name', 'price', 'stock')

    def create(self, validated_data):
        category_name = validated_data.pop('category').get("name")
        print(category_name)
        category_obj, created = Category.objects.get_or_create(name=category_name)
        product = Product.objects.create(category=category_obj, **validated_data)
        return product