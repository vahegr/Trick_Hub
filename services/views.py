from django.shortcuts import render
from django.views.generic import TemplateView


class ServicesView(TemplateView):
    template_name = 'services/ourservices.html'
