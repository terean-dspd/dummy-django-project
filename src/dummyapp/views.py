from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class DummyView(TemplateView):
    template_name = "dummyapp/home.html"
