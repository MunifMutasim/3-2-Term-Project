from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
	class Meta():
		model = Order
		fields=('name','email','mobileno','address')

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['mobileno'].label='Mobile Number'
		self.fields['address'].label='Delivery Address'
