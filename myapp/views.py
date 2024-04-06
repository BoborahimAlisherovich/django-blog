from django.shortcuts import render
from django.http import HttpResponse #new
from .models import Article

def main(request):
    articles = Article.objects.all().order_by("-id")
    context = {"articles":articles}
    return render(request,"index.html",context)

