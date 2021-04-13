from django.forms import ModelForm, HiddenInput
from .models import Post, Business, Essential, Hood


class PostCreateForm(ModelForm):

    class Meta:
        model = Post
        exclude = ['creator', 'hood', 'timestamp']


class BusinessCreateForm(ModelForm):

    class Meta:
        model = Business
        exclude = ['owner', 'hood', 'timestamp']


class EssentialCreateForm(ModelForm):

    class Meta:
        model = Essential
        exclude = ['timestamp']


class HoodCreateForm(ModelForm):

    class Meta:
        model = Hood
        exclude = ['timestamp']
