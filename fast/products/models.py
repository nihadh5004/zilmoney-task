from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField(default=100)
    dixscount_percentage=models.IntegerField(default=10)
    def __str__(self):
        return self.name

class Purchase(models.Model):
    item=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    amount=models.IntegerField()
    
    def __str__(self):
        return self.item.name
