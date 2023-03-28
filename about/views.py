from django.shortcuts import render
from django.views.generic import TemplateView
from .models import About
from account.models import User


class AboutView(TemplateView):
    template_name = 'about/aboutus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_items'] = About.objects.all()
        context['developers'] = User.objects.filter(is_admin=True)
        return context

