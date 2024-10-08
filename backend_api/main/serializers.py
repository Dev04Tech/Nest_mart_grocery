from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.Vendor
            fields=['id','user','address']
      
      def __init__(self , *args, **kwargs):
            super(VendorSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

class VendorDetailSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.Vendor
            fields=['id','user','address']

      def __init__(self , *args, **kwargs):
            super(VendorDetailSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

class ProductListSerializer(serializers.ModelSerializer):
      product_rating=serializers.StringRelatedField(many=True,read_only=True) 
      class Meta:
            model=models.Product
            fields=['id','category','vendor','title','detail','price','product_rating']

      def __init__(self , *args, **kwargs):
            super(ProductListSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

class ProductDetailSerializer(serializers.ModelSerializer):
      product_rating=serializers.StringRelatedField(many=True,read_only=True) 
      class Meta:
            model=models.Product
            fields=['id','category','vendor','title','detail','price','product_rating']

      def __init__(self , *args, **kwargs):
            super(ProductDetailSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

#CUSTOMER
class CustomerSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.Customer
            fields=['id','user','mobile']
      
      def __init__(self , *args, **kwargs):
            super(CustomerSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

class CustomerDetailSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.Customer
            fields=['id','user','mobile']

      def __init__(self , *args, **kwargs):
            super(CustomerDetailSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

#ORDER
class OrderSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.Order
            fields=['id','customer']
      
      def __init__(self , *args, **kwargs):
            super(OrderSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

#ORDER_ITEMS

class OrderDetailSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.OrderItems
            fields=['id','order','product']
      
      def __init__(self , *args, **kwargs):
            super(OrderDetailSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

#customer address
class CustomerAddressSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.CustomerAddress
            fields=['id','customer','address','default_address']  
      
      def __init__(self , *args, **kwargs):
            super(CustomerAddressSerializer,self).__init__(*args, **kwargs)
            self.Meta.depth=1
# 

class ProductRatingSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.ProductRating
            fields=['id','customer','product','rating','reviews','add_time']  
      
      def __init__(self , *args, **kwargs):
            super(ProductRatingSerializer,self).__init__(*args, **kwargs)
            self.Meta.depth=1

class CategorySerializer(serializers.ModelSerializer):
      class Meta:
            model=models.ProductCategory
            fields=['id','title','detail']
      
      def __init__(self , *args, **kwargs):
            super(CategorySerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1

class CategoryDetailSerializer(serializers.ModelSerializer):
      class Meta:
            model=models.ProductCategory
            fields=['id','title','detail']

      def __init__(self , *args, **kwargs):
            super(CategoryDetailSerializer,self).__init__(*args, **kwargs)
            # request=self.context.get('request')
            # self.Meta.depth=1