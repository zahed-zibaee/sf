# Generated by Django 3.0.1 on 2021-04-18 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210418_1211'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DeliveryFromCompany',
            new_name='DeliveryToCategory',
        ),
        migrations.RenameModel(
            old_name='DeliveryFromCategory',
            new_name='DeliveryToCompany',
        ),
    ]