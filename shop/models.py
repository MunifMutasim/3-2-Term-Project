from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50, unique=True)

	class Meta:
		ordering = ['name',]
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
	category = models.ManyToManyField(Category)
	name = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=50, unique=True)
	image = models.ImageField(upload_to='images',blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	stock = models.PositiveIntegerField()
	available = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_at']
		index_together=["id","slug"]

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',args=[self.id,self.slug])

	@property
	def image_url(self):
		if self.image and hasattr(self.image, 'url'):
			return self.image.url



