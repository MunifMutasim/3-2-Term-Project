from .models import CItem
from shop.models import Product
from django.shortcuts import get_object_or_404 
from django.http import HttpResponseRedirect
import decimal
import random

CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
	if not request.session.get(CART_ID_SESSION_KEY) :
		request.session[CART_ID_SESSION_KEY] = _generate_cart_id()

	return request.session[CART_ID_SESSION_KEY]

#This random function is taken from net and modified to use for generating cart id
def _generate_cart_id():
	cart_id = ''
	characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
	cart_id_length = 50
	
	for y in range(cart_id_length):
		cart_id += characters[random.randint(0, len(characters)-1)]

	return cart_id

def get_cart_items(request):
	return CItem.objects.filter(cart_id=_cart_id(request))

def add_to_cart(request,id,slug):
	p = get_object_or_404(Product,id=id,slug=slug)
	postdata = request.POST.copy()
	
	#get quantity added,return 1 if empty
	quantity = postdata.get('quantity',1)
	
	#get products in the cart
	cart_products = get_cart_items(request)
	
	# check to see if item is already in cart
	product_in_cart = False
	for cart_item in cart_products:
		if p.id == cart_item.product.id:
			# update the quantity if found
			cart_item.augment_quantity(quantity)
			product_in_cart = True

	# for cart_item in cart_products:
	# 	print("Name : "+cart_item.product.name)

	if not product_in_cart:
		#Create new CItem and save
		ci = CItem()
		ci.product = p
		ci.quantity = quantity
		ci.cart_id = _cart_id(request)
		ci.save()

# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
	return get_cart_items(request).count()

def remove_from_cart(request):
	postdata = request.POST.copy()
	item_id = postdata['item_id']
	cart_item = get_object_or_404(CItem,id=item_id,cart_id=_cart_id(request))
	if cart_item:
		cart_item.delete()


def update_cart(request):
	postdata = request.POST.copy()
	item_id = postdata['item_id']
	quantity = postdata['quantity']
	cart_item = get_object_or_404(CItem,id=item_id,cart_id=_cart_id(request))

	if cart_item:
		if int(quantity)>0:
			cart_item.quantity = int(quantity)
			cart_item.save()
	else :
		remove_from_cart(request)


# gets the total cost for the current cart
def cart_subtotal(request):
	cart_total = decimal.Decimal('0.00')
	cart_products = get_cart_items(request)
	for cart_item in cart_products:
		cart_total += cart_item.product.price * cart_item.quantity

	return cart_total

def clear(request):
	request.session[CART_ID_SESSION_KEY] = {}
	request.session.modified = True





	

