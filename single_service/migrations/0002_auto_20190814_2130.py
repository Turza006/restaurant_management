# Generated by Django 2.0.2 on 2019-08-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('single_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single_service',
            name='single_service_price',
            field=models.IntegerField(null=True),
        ),
    ]