from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView

class Index(TemplateView):
    template_name = "index.html"
