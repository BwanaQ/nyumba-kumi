from django.forms import ModelForm, HiddenInput
from .models import Post


class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['creator', 'hood', 'timestamp']
