from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.timezone import utc
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Business, Hood, Essential, Location, Post
from django.urls import reverse_lazy
#from .forms import RatingCreateForm
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    ordering = ['-timestamp']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.all()


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'body', 'link']
    success_message = "The Post %(title) was created successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
