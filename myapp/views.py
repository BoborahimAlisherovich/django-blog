from django.shortcuts import render,HttpResponseRedirect
#300,301,302
from .models import Article
from django.contrib import messages  # new
from django.urls import reverse  # new

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

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            author = request.user
            article = Article(
                title=title,
                description=description,
                image=image,
                author=author  
            )
            article.save()
            messages.success(request, '🥳 Maqolangiz muvaffaqiyatli tarzda yaratildi.')
            return HttpResponseRedirect(reverse('articles-list'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    else:
        form = ArticleForm()
    context = {"form": form}
    
    return render(request, "create_article.html", context)