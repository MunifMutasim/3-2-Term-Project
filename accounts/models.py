from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
	states_choices=(
		('Dhaka','Dhaka'),
		('Chittagong','Chittagong'),
		('Rangpur','Rangpur'),
		('Khulna','Khulna'),
		('Mymensingh','Mymensingh'),
		('Rajshahi','Rajshahi'),
		('Barisal','Barisal'),
	)

	user=models.OneToOneField(User)

	#Additional Features our user will have.
	address1=models.CharField(max_length=100)
	address2=models.CharField(max_length=100,blank=True)
	city=models.CharField(max_length=100)
	post_code=models.IntegerField()
	region=models.CharField(max_length=100,choices=states_choices)

	def __str__(self):
		return self.user.username
