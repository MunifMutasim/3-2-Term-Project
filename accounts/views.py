from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def register(request):
	registered=False;

	if request.method=="POST":
		user_form=UserForm(data=request.POST)
		profile_form=UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)#Hashing
			user.save()

			profile=profile_form.save(commit=False)
			profile.user=user

			profile.save()
			registered=True

		else :
			print(user_form.errors,profile_form.errors)

	else :
		user_form=UserForm()
		profile_form=UserProfileInfoForm()

	context={
		'user_form':user_form,
		'profile_form':profile_form,
		'registered':registered
	}

	return render(request,'accounts/registration.html',context)

def user_login(request):
	 if request.method=='POST':
	 	username=request.POST.get('username')
	 	password=request.POST.get('password')

	 	user=authenticate(username=username,password=password)

	 	if user:
	 		if user.is_active:
	 			login(request,user)
	 			return HttpResponseRedirect(reverse('home'))#HttpResponseRedirect(reverse('url_name'))


	 		else :
	 			return HttpResponse("Account not active")

	 	else :
	 		print("Some one tried")
	 		print(username)
	 		return HttpResponse("Invalid Login Detail")

	 else :
	 	return render(request,'accounts/login.html',{})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('home'))


