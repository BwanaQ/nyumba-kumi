from django.forms import ModelForm, HiddenInput
from .models import Post, Business


class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['creator', 'hood', 'timestamp']


class BusinessCreateForm(ModelForm):

    class Meta:
        model = Business
        exclude = ['owner', 'hood', 'timestamp']
