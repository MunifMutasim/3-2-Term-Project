from django.shortcuts import render
from django.http import HttpResponse
from .forms import OrderForm
from cart_app import cart
from cart_app.models import CItem
from shop.models import Product
from .models import Order,OrderItem
import decimal


# Create your views here.
def index(request):
	cart_products = cart.get_cart_items(request)
	total_cost = cart.cart_subtotal(request)

	if request.method=="POST":
		print("post")
		order_form = OrderForm(request.POST)

		if order_form.is_valid():
			order = order_form.save()
			name = order_form.cleaned_data['name']

			for cart_item in cart_products:
				OrderItem.objects.create(order=order,product=cart_item.product,price=(cart_item.product.price*cart_item.quantity),quantity=cart_item.quantity)


			cart.clear(request)
			return render(request,'order/success.html',{'name':name,'total_cost':total_cost})

		else :
			print("Error"+order_form.errors)


		
	else :
		order_form = OrderForm()
		print("Get")


	context = {'order_form':order_form}
	return render(request,'order/index.html',context)


		

