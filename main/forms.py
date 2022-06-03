from django.forms import ModelForm

from main.models import Post, Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'category', 'body']
