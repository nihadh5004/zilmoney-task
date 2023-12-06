from django.urls import path
from .views import *
urlpatterns = [
    path('items/<int:item_id>/', ProductDetail.as_view(), name='product-list'),
    path('purchase/', PurchaseProduct.as_view(), name='product-purchase'),
    path('purchase-history/', PurchaseHistory.as_view(), name='purchase-history'),

]