# Generated by Django 3.2.13 on 2022-11-11 17:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('sold_count', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('hit', models.IntegerField(default=0)),
                ('brand', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
    ]
