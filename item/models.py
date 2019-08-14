from django.db import models

# Create your models here.
class Item(models.Model):
    item_restaurant_id = models.CharField(max_length=200,null=True)
    item_id = models.CharField(max_length=10,null= True)
    item_name= models.CharField(max_length=20,null=True)
    item_detail = models.CharField(max_length=200,null=True)
    item_price = models.CharField(max_length=20,null = True)


    def __str__(self):
        return self.item_restaurant_id