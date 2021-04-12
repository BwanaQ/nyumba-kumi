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
from .forms import PostCreateForm
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    queryset = Post.objects.order_by('-timestamp')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.order_by('-timestamp')


class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    success_url = '/'
    fields = ['title', 'body']
    success_message = "The Post created successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.hood = self.request.user.profile.hood
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    success_url = '/'
    fields = ['title', 'body']
    success_message = "The Post updated successfully!"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        form.instance.hood = self.request.user.profile.hood
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False


class PostDetailView(DetailView):
    model = Post
    success_url = '/'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    success_message = "The Post %(title) was deleted successfully!"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False
