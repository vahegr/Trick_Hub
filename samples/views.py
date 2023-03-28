from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from samples.models import Sample


class SamplesView(ListView):
    model = Sample
    template_name = 'samples/nemoonekarha.html'
    queryset = Sample.objects.all()


