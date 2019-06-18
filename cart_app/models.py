from django.db import models
from shop.models import Product

#The actual name would be CartItem..Due to some error i did this
class CItem(models.Model):
	cart_id = models.CharField(max_length=50)
	date_added = models.DateTimeField(auto_now_add=True)
	quantity = models.IntegerField(default=1)
	product = models.ForeignKey('shop.Product', unique=False)

	class Meta:
		ordering = ['date_added']

	def total(self):
		return self.quantity * self.product.price

	def name(self):
		return self.product.name

	def price(self):
		return self.product.price

	def get_absolute_url(self):
		return self.product.get_absolute_url()

	def augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()
