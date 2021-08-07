from django.shortcuts import get_object_or_404, render

from .models import Article

def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles': articles
    })

def detail(request, article_id):
    article = get_object_or_404(Article, pk = article_id)
    return render(request, 'articles/detail.html', {
        'article': article
    })
