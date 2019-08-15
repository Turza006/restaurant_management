from django.db import models

# Create your models here.
class Pamment(models.Model):
    Pamment_user_id = models.CharField(max_length=20,null=True)
    Pamment_service_id = models.CharField(max_length=20,null=True)
    Pamment_price = models.CharField(max_length=20,null = True)
    Pamment_date = models.CharField(max_length=20,null= True)


    def __str__(self):
        return self.Pamment_user_id