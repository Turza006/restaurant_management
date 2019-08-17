from django.db import models

# Create your models here.
class Restaurant_package(models.Model):
    restaurant_package_name = models.CharField(max_length=250,null = True)
    restaurant_package_price = models.IntegerField(null=True)
    restaurant_package_specification = models.CharField(max_length=2000,null=True)
    restaurant_package_validity = models.DateTimeField(null=True)
    restaurant_package_id = models.IntegerField(null=True)



    def __str__(self):
        return self.restaurant_package_name