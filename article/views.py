from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost
# Create your views here.

def article_list(request):
    articles = ArticlePost.objects.all()
    # 传递给模板
    context = {'articles':articles}
    # 载入模板返回context
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    context = {'article':article}
    return render(request, 'article/detail.html', context)