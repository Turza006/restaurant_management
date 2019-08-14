from django.db import models

# Create your models here.
class Features(models.Model):
    features_id = models.CharField(max_length=200,null=True)
    service_id = models.CharField(max_length=200,null=True)
    user_id = models.CharField(max_length=200,null = True)
    starting = models.CharField(max_length=20,null=True)
    ending = models.CharField(max_length=20,null=True)
    price = models.CharField(max_length=10,null=True)



    def __str__(self):
        return self.features_id
