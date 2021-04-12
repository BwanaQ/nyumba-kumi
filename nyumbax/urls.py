from django.urls import path
from . import views
from .views import (
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,


    BusinessListView,
    BusinessCreateView,
    BusinessUpdateView,
    BusinessDeleteView,
    BusinessDetailView,

)

urlpatterns = [
    path('', PostListView.as_view(), name="nyumbax-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="nyumbax-detail"),
    path('post/new/', PostCreateView.as_view(), name="nyumbax-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="nyumbax-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="nyumbax-delete"),

    path('business/', BusinessListView.as_view(), name="business-home"),
    path('business/<int:pk>/', BusinessDetailView.as_view(), name="business-detail"),
    path('business/new/', BusinessCreateView.as_view(), name="business-create"),
    path('business/<int:pk>/update/',
         BusinessUpdateView.as_view(), name="business-update"),
    path('business/<int:pk>/delete/',
         BusinessDeleteView.as_view(), name="business-delete"),
]
