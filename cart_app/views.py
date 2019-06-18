from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .import cart

def show_cart(request):
	if request.method=="POST":
		postdata = request.POST.copy()
		
		if postdata['submit'] == 'Remove':
			cart.remove_from_cart(request)

		if postdata['submit'] == 'Update':
			cart.update_cart(request)

		if postdata['submit'] == 'Order':
			return HttpResponseRedirect(reverse('order:index'))




	cart_items = cart.get_cart_items(request)
	cart_subtotal = cart.cart_subtotal(request)
	context = {'cart_items':cart_items,'cart_subtotal':cart_subtotal}

	return render(request,'cart_app/detail.html',context)








