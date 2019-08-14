from django.db import models

# Create your models here.
class Single_service(models.Model):
    single_service_name = models.CharField(max_length=250,null = True)
    single_service_price = models.IntegerField(null=True)
    single_service_specification = models.CharField(max_length=2000,null=True)
    single_service_validity = models.DateTimeField(null=True)
    single_service_id = models.IntegerField(null=True)



    def __str__(self):
        return self.single_service_name