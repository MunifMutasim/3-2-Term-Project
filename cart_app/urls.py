from django.conf.urls import url,include
from .import views

app_name='cart'

urlpatterns = [
	url(r'^$',views.show_cart,name='show_cart_detail'),
]