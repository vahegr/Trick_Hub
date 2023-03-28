from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Article, Comment, Like


class ArticlesView(ListView):
    model = Article
    template_name = 'articles/articles.html'
    queryset = Article.objects.filter(allowing=True)


def article_detail(request, id, slug):
    article = Article.objects.get(id=id, slug=slug, allowing=True)
    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)
    if request.user.ip_address.likes.filter(article_id=id, ip_address=request.user.ip_address).exists():
        is_liked = True
    else:
        is_liked = False

    comments = article.comments.all()
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        comment = request.POST.get('comment')
        parent = request.POST.get('parent_id')
        Comment.objects.create(comment=comment, article=article, firstname=firstname, lastname=lastname, parent_id=parent)
    return render(request, 'articles/articlesdeatail.html', context={'article': article, 'is_liked': is_liked, 'comments': comments})


def article_like(request, id):
    user_ip = request.user.ip_address
    try:
        like = Like.objects.get(article_id=id, ip_address=user_ip)
        like.delete()
        return JsonResponse({'response': 'unliked'})
    except:
        Like.objects.create(article_id=id, ip_address=user_ip)
        return JsonResponse({'response': 'liked'})

