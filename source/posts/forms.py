from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('description', 'image')


class CommentForm(forms.Form):
    text = forms.CharField(max_length=50, required=True, label='Комментарий')
    