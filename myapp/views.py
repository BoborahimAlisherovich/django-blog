from django.shortcuts import render
from django.http import HttpResponse #new
from .models import Article
from .forms import ArticleForm
def main(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"index.html",context)

def article_detail(request,id):
    article = Article.objects.get(id=id)
    context = {"article":article}
    return render(request,"article.html",context)


def create_article(request):
    form = ArticleForm()
    context = {"form":form}
    
    return render(request,"create_article.html",context)



