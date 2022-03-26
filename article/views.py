from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import ArticlePost
from .forms import ArticlePostForm

import markdown
# Create your views here.


def article_safe_delete(request, id):
    if request.method == "POST":
        article = ArticlePost.objects.get(id=id)
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")

def article_create(request):
    if request.method == "POST":
        # 将网页提交的数据赋值到表单实例
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            # 保存数据但不提交到数据库
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            # 保存到数据库
            new_article.save()

            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)

def article_list(request):
    articles = ArticlePost.objects.all()
    # 传递给模板
    context = {'articles':articles}
    # 载入模板返回context
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    #   渲染markdown语法
    article.body = markdown.markdown(article.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
    ])
    context = {'article':article}
    return render(request, 'article/detail.html', context)