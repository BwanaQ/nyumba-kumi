from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.utils.timezone import utc
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
from .models import Post, Business, Essential, Hood
from django.urls import reverse_lazy
from .forms import PostCreateForm
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin


class PostListView(LoginRequiredMixin, ListView):
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


class BusinessListView(ListView):
    model = Business
    template_name = 'business_list.html'
    queryset = Business.objects.order_by('-timestamp')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Business.objects.filter(title__icontains=query)
        else:
            return Business.objects.order_by('-timestamp')


class BusinessCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Business
    success_url = '/'
    fields = ['title', 'email']
    success_message = "Business created successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.hood = self.request.user.profile.hood
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class BusinessUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Business
    success_url = '/'
    fields = ['title', 'email']
    success_message = "The Business updated successfully!"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.hood = self.request.user.profile.hood
        return super().form_valid(form)

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class BusinessDetailView(DetailView):
    model = Business
    success_url = '/'


class BusinessDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Business
    success_url = '/'
    success_message = "The Business %(title) was deleted successfully!"

    def test_func(self):
        business = self.get_object()
        if self.request.user == business.owner:
            return True
        return False


class EssentialListView(ListView):
    model = Essential
    template_name = 'essential_list.html'
    queryset = Essential.objects.order_by('-timestamp')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Essential.objects.filter(title__icontains=query)
        else:
            return Essential.objects.order_by('-timestamp')


class EssentialCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Essential
    success_url = '/'
    fields = ['title', 'officer', 'phone', 'email', 'location']
    success_message = "Essential created successfully!"


class EssentialUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Essential
    success_url = '/'
    fields = ['title', 'officer', 'phone', 'email', 'location']
    success_message = "The Essential updated successfully!"


class EssentialDetailView(DetailView):
    model = Essential
    success_url = '/'


class EssentialDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Essential
    success_url = '/'
    success_message = "The Essential %(title) was deleted successfully!"


class HoodListView(ListView):
    model = Hood
    template_name = 'hood_list.html'
    queryset = Hood.objects.order_by('title')

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Hood.objects.filter(title__icontaihoodns=query)
        else:
            return Hood.objects.order_by('title')


class HoodCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Hood
    success_url = '/'
    fields = ['title', 'location', 'admin']
    success_message = "Hood created successfully!"


class HoodUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Hood
    success_url = '/'
    fields = ['title', 'location', 'admin']
    success_message = "The Hood updated successfully!"


class HoodDetailView(DetailView):
    model = Hood
    success_url = '/'


class HoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Hood
    success_url = '/'
    success_message = "The Hood %(title) was deleted successfully!"
