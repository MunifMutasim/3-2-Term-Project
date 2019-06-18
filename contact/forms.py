from django import forms

class ContactForm(forms.Form):
	name = forms.CharField(label='Name', max_length=50)
	email = forms.EmailField()
	subject = forms.CharField(label="Subject", max_length=300)
	message = forms.CharField(label="Your message",widget=forms.Textarea)


