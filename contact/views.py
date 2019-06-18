from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from . import forms

# Create your views here.
def ContactPage(request):
	if request.method=="POST":
		form = forms.ContactForm(request.POST)
		
		if form.is_valid():
			name = form.cleaned_data['name']
			from_email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			to_email = 	[settings.EMAIL_HOST_USER]
			temp = "\nThe message is sent from : "
			message +=temp+from_email
			send_mail(subject,message,from_email,to_email,fail_silently=False)
			messages.success(request,'Thanks for your feedback')


		else :
			print(form.errors)

	form = forms.ContactForm()
	return render(request,'contact/contact.html',{'form':form})



