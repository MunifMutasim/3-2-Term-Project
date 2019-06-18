from django.db import models
from cart_app.models import CItem
from shop.models import Product

# Create your models here.

class Order(models.Model):
	name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.CharField(max_length=250)
	mobileno = models.CharField(max_length=14)

	def __str__(self):
		return self.mobileno

class OrderItem(models.Model):
	order = models.ForeignKey(Order, related_name='items')
	product = models.ForeignKey(Product, related_name='order_items')
	price = models.PositiveIntegerField(blank=True,null=True)
	quantity = models.PositiveIntegerField(default=0)

	def __str__(self):
		return '{}'.format(self.id)

	def get_cost(self):
		return self.price * self.quantity





