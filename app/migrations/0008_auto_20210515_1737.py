# Generated by Django 3.0.14 on 2021-05-15 13:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210512_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: \'09XXXXXXXXX\'. "09" than 9 digit digits allowed.', regex='^09\\d{9}$')])),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deliverytocategory',
            name='category_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.CategoryPerson'),
        ),
        migrations.AddField(
            model_name='receivedfromcategory',
            name='category_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.CategoryPerson'),
        ),
    ]