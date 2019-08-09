from django.db import models

class Restaurant_description(models.Model):
    restaurant_name = models.CharField(max_length=100)
    restaurant_email = models.EmailField(max_length=150)
    restaurant_Address = models.CharField(max_length=500)
    restaurant_photo_link = models.CharField(max_length=250)
    restaurant_number = models.CharField(max_length=50)
    restaurant_owner_name = models.CharField(max_length=100)
    restaurant_owner_phone_number = models.CharField(max_length=50)
    restaurant_Details = models.CharField(max_length=2000)



    def __str__(self):
        return self.restaurant_name
