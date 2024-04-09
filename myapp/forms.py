from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(
     widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))
    image = forms.ImageField()
