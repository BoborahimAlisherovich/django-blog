from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Article/image")
    create_data = models.DateTimeField(auto_now=True)
    #4ta maydon qo'shish
    def __str__(self) -> str:
        return f"{self.title}"
