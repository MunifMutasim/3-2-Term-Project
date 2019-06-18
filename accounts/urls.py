from django.conf.urls import url,include
from .import views

app_name='accounts'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^login/$',views.user_login,name='user_login'),
    # url(r'^profile/$',views.index,name='index'),
]