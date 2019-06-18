from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from .models import Product,Category
from .forms import ProductAddToCartForm
from cart_app import cart

# Create your views here.
def product_list(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		products = products.filter(category=category)

	context = {'category':category,'categories':categories,'products':products}
	return render(request,'shop/list.html',context)


# def product_detail(request,id,slug):
# 	product = get_object_or_404(Product,id=id,slug=slug,available=True)
# 	cart_product_form = CartAddProductForm()
# 	context = {'product':product,'cart_product_form':cart_product_form}
# 	return render(request,'shop/detail.html',context)

def product_detail(request,id,slug):
	product = get_object_or_404(Product,id=id,slug=slug,available=True)
	if request.method=="POST":
		cart_product_form = ProductAddToCartForm(data=request.POST)
		
		if cart_product_form.is_valid():
			postdata = request.POST.copy()
			cart.add_to_cart(request,id,slug)
			print("After adding in view")
			# if test cookie worked, get rid of it
			if request.session.test_cookie_worked():
				request.session.delete_test_cookie()

		else :
			print(cart_product_form.errors)

		return HttpResponseRedirect(reverse('cart:show_cart_detail'))

	else :
		cart_product_form = ProductAddToCartForm()
		# set the test cookie on our first GET request
		request.session.set_test_cookie()
		context = {'product':product,'cart_product_form':cart_product_form}
		return render(request,'shop/detail.html',context)



