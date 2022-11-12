from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    sold_count = models.IntegerField(default=0)  # 상품 팔린 갯수
    quantity = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])   # 구입할 상품 갯수
    hit = models.IntegerField(default=0)
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=20)
    