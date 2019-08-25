from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDetailView().as_view, name='post_detail'),
    path('post/new', views.CreatePostView.as_view(), name='post_new'),
]