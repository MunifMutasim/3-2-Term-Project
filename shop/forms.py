from django import forms

class ProductAddToCartForm(forms.Form):
	quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2','value':'1','class':'quantity','maxlength':'5'}), error_messages={'invalid':'Please enter a valid quantity.'}, min_value=1)
	
	def __init__(self, request=None, *args, **kwargs):
		super().__init__(*args,**kwargs)
		self.request = request

	def clean(self):
		if self.request:
			if not self.request.session.test_cookie_worked():
				raise forms.ValidationError("Cookies must be enabled.")

		return self.cleaned_data