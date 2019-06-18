from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic import TemplateView

class HomePage(TemplateView):
	template_name = "index.html"

class AboutPage(TemplateView):
	template_name = "about.html"
