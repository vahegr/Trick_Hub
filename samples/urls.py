from django.urls import path
from . import views

app_name = 'samples'

urlpatterns = [
    path('', views.SamplesView.as_view(), name='samples')
]
