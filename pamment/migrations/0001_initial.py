# Generated by Django 2.0.2 on 2019-08-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pamment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pamment_user_id', models.CharField(max_length=20, null=True)),
                ('Pamment_service_id', models.CharField(max_length=20, null=True)),
                ('Pamment_price', models.CharField(max_length=20, null=True)),
                ('Pamment_date', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
