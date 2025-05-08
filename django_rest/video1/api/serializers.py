from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock'
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Product price should be greater than 0.'
            )
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='product.price')

    class Meta:
        model = OrderItem
        fields = ('product_name', 'product_price', 'quantity', 'item_subtotal')

    def get_product_name(self, obj):
        return obj.product.name
    
    def get_product_price(self, obj):
        return obj.product.price


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()
    user = serializers.CharField(source='user.username')
    
    class Meta:
        model = Order
        fields = ('order_id', 'created_at', 'user', 'status', 'items', 'total_price')

    def get_total_price(self, obj):
        total = sum([item.item_subtotal for item in obj.items.all()])
        return total
    
class ProductInfoSerializer(serializers.Serializer):
    products = ProductSerializer(many=True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()