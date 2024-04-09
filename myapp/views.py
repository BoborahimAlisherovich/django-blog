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
    print("---------create----------")
    if request.method == "POST":
        form = ArticleForm(request.POST,request.FILES)
        print("salom")
        print(form.cleaned_data)
        # if form.is_valid():
        #     return HttpResponseRedirect("/thanks/")

    else:
        form = ArticleForm()
    context = {"form":form}
    
    return render(request,"create_article.html",context)



