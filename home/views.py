from django.shortcuts import render
from django.views.generic import TemplateView
from plans.models import Plan, PlanFeature


class HomePage(TemplateView):
    template_name = 'home/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['wordpress_plans'] = Plan.objects.filter(simple=True)
        context['exclusive_plans'] = Plan.objects.filter(simple=False)
        return context

