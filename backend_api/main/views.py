from django.shortcuts import render
from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from . import models

# Create your views here.

class VendorList(generics.ListCreateAPIView):
      queryset= models.Vendor.objects.all()
      serializer_class=serializers.VendorSerializer
      # permission_classes=[permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset= models.Vendor.objects.all()
      serializer_class=serializers.VendorDetailSerializer
      # permission_classes=[permissions.IsAuthenticated]

class ProductList(generics.ListCreateAPIView):
      queryset= models.Product.objects.all()
      serializer_class=serializers.ProductListSerializer
      pagination_class=pagination.PageNumberPagination #pagination coustimisation
      # permission_classes=[permissions.IsAuthenticated]

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset= models.Product.objects.all()
      serializer_class=serializers.ProductDetailSerializer
      # permission_classes=[permissions.IsAuthenticated]

#customers
class CustomerList(generics.ListCreateAPIView):
      queryset= models.Customer.objects.all()
      serializer_class=serializers.CustomerSerializer
      # permission_classes=[permissions.IsAuthenticated]

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset= models.Customer.objects.all()
      serializer_class=serializers.CustomerDetailSerializer


#order
class OrderList(generics.ListCreateAPIView):
      queryset= models.Order.objects.all()
      serializer_class=serializers.OrderSerializer

#order_items
class OrderDetail(generics.ListAPIView):
      # queryset= models.OrderItems.objects.all()
      serializer_class=serializers.OrderDetailSerializer

      def get_queryset(self):
            order_id = self.kwargs['pk']
            order=models.Order.objects.get(id=order_id)
            order_items=models.OrderItems.objects.filter(order=order)
            return order_items
      

class CustomerAddressViewSet(viewsets.ModelViewSet):
      serializer_class=serializers.CustomerAddressSerializer
      queryset=models.CustomerAddress.objects.all()

class ProductRatingViewSet(viewsets.ModelViewSet):
      serializer_class=serializers.ProductRatingSerializer
      queryset=models.ProductRating.objects.all()



class CategoryList(generics.ListCreateAPIView):
      queryset= models.ProductCategory.objects.all()
      serializer_class=serializers.CategorySerializer
      # permission_classes=[permissions.IsAuthenticated]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
      queryset= models.ProductCategory.objects.all()
      serializer_class=serializers.CategoryDetailSerializer
      # permission_classes=[permissions.IsAuthenticated]