from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.main,name="articles-list"),
    path('create/',views.create_article,name="create-article"),
    path('<int:id>/',views.article_detail,name="article-detail"),

] 
