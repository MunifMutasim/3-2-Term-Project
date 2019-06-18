from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput())
	confirmation_password=forms.CharField(widget=forms.PasswordInput())
	# username = forms.CharField(help_text=False) eikhane dileo hobe abr __init__ e dileo hobe.

	class Meta():
		model=User
		fields=('username','email','password')

	def clean(self):
		all_clean_data=super().clean()
		passw=all_clean_data['password']
		con_pass=all_clean_data['confirmation_password']

		if passw!=con_pass:
			raise forms.ValidationError("Password don't match")

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].label='Username'
		self.fields['username'].help_text=False
		self.fields['email'].required=True
		self.fields['confirmation_password'].label='Confirm Password'
		


class UserProfileInfoForm(forms.ModelForm):
	class Meta():
		model=UserProfileInfo
		fields =('address1','address2','city','post_code','region')
