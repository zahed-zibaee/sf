# Generated by Django 3.0.14 on 2021-05-12 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210512_1501'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firewallchange',
            old_name='new_firewall',
            new_name='old_firewall',
        ),
    ]
