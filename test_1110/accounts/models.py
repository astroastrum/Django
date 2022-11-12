from django.db import models
from products.models import Product

# Create your models here.
# 주문 정보
class Order(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  created = models.DateTimeField(auto_now_add=True)
  paid = models.BooleanField(default=False)

  class Meta:
    ordering = ['-created']

  def __str__(self):
    return 'Order {}'.format(self.id)

  def get_total_product(self):
    return sum(item.get_item_price() for item in self.items.all())

  def get_total_price(self):
    total_product = self.get_total_product()
    return total_product - self.discount

# 사용자가 주문한 제품
# 주문에 포함된 제품 정보
class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
  product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order_products')
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return '{}'.format(self.id)

  def get_item_price(self):
    return self.price * self.quantity

    



