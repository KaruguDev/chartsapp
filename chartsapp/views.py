from django.shortcuts import render
from django.views.generic import TemplateView
import urllib2
import simplejson

class IndexView(TemplateView):
        template_name = "index.html"


