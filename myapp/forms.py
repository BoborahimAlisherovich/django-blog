from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Maqola matnini kiriting'}))
    image = forms.ImageField()
