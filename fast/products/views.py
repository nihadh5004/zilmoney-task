from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class ProductDetail(APIView):
    def get(self,request,item_id):
        try:
            apply_discount = request.query_params.get('apply_discount')      
            
            products=Products.objects.get(id=item_id)
            productslist = ProductInfo(products)
            if apply_discount:
                discount_price=products.price - (products.price * 10/100)
            else:
                discount_price = products.price
                
            product_data ={
                "productlist": productslist.data,
                "discount_price": discount_price
            }

            return Response(product_data, status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    {"error": "An error occurred while fetching product."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    
class PurchaseProduct(APIView):
    
    permission_classes = [IsAuthenticated]

    def post(self,request):
        try:
            item_id=request.data.get('item_id')
            quantity=request.data.get('quantity')
            
            
            
            product=Products.objects.filter(id=item_id)
            product.quantity =product.quantity - quantity
            return Response({'message': 'purchase done successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    {"error": "An error occurred while purchasing product."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    

class PurchaseHistory(APIView):

    def get(self,request):
        try:  
            purchase_history=Purchase.objects.all()
            serializer=PurchaseInfo(purchase_history, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
                return Response(
                    {"error": "An error occurred while fetching purchase history."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
    


        
