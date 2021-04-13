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


    EssentialListView,
    EssentialCreateView,
    EssentialUpdateView,
    EssentialDeleteView,
    EssentialDetailView,

    HoodListView,
    HoodCreateView,
    HoodUpdateView,
    HoodDeleteView,
    HoodDetailView,
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

    path('essential/', EssentialListView.as_view(), name="essential-home"),
    path('essential/<int:pk>/', EssentialDetailView.as_view(),
         name="essential-detail"),
    path('essential/new/', EssentialCreateView.as_view(), name="essential-create"),
    path('essential/<int:pk>/update/',
         EssentialUpdateView.as_view(), name="essential-update"),
    path('essential/<int:pk>/delete/',
         EssentialDeleteView.as_view(), name="essential-delete"),

    path('hood/', HoodListView.as_view(), name="hood-home"),
    path('hood/<int:pk>/', HoodDetailView.as_view(), name="hood-detail"),
    path('hood/new/', HoodCreateView.as_view(), name="hood-create"),
    path('hood/<int:pk>/update/',
         HoodUpdateView.as_view(), name="hood-update"),
    path('hood/<int:pk>/delete/',
         HoodDeleteView.as_view(), name="hood-delete"),

]
