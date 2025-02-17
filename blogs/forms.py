from django import forms

from .models import Blog, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['text', 'public']
        labels = {'text':'', 'public':'Make blog public? (Default = private)'}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =['text']
        labels={'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}