from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.ArticlesView.as_view(), name='articles'),
    path('article_detail/<int:id>/<slug:slug>', views.article_detail, name='article_detail'),
    path('article_like/<int:id>', views.article_like, name='article_like'),
]
