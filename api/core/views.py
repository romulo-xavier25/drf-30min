from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Category, Product
from .serializers import ProductSerializer, CategorySerializer


"""
API PRODUCTS
"""
class ProductAPIView(APIView):
    
    def get(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    
    def get(self, request, id):
        queryset = get_object_or_404(Product.objects.all(), id=id)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)
    
    def put(self, request, id):
        queryset = get_object_or_404(Product.objects.all(), id=id)
        serializer = ProductSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = get_object_or_404(Product.objects.all(), id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

    

"""
API CATEGORY
"""
class CategoryAPIView(APIView):
    
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class CategoryDetail(APIView):
    
    def get(self, request, id):
        queryset = get_object_or_404(Category.objects.all(), id=id)
        serializer = CategorySerializer(queryset)
        return Response(serializer.data)
    
    def put(self, request, id):
        queryset = get_object_or_404(Category.objects.all(), id=id)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        queryset = get_object_or_404(Category.objects.all(), id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)