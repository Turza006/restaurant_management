# Generated by Django 2.0.2 on 2019-08-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Single_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('single_service_name', models.CharField(max_length=250, null=True)),
                ('single_service_price', models.IntegerField(max_length=50, null=True)),
                ('single_service_specification', models.CharField(max_length=2000, null=True)),
                ('single_service_validity', models.DateTimeField(null=True)),
                ('single_service_id', models.IntegerField(null=True)),
            ],
        ),
    ]
