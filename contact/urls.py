from django.conf.urls import url,include
from .import views

app_name = 'contact'

urlpatterns = [
	url(r'^$',views.ContactPage,name="contact"),
]