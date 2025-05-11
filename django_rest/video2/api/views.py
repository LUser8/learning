from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer


class ProductAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        category_name = request.query_params.get('category', None)
        if category_name is not None:
            category = get_object_or_404(Category, name__iexact=category_name)
            products = products.filter(category=category)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        print(data)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




