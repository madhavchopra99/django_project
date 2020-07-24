from django.urls import path
from .views import (PostListView, PostDetailView,
                    PostCreateView, PostUpdateView,
                    PostDeleteView, UserPostListView,
                    CommentListView, CommentCreateView,
                    CommentUpdateView, CommentDeleteView,
                    PostSearchListView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),

    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/search/', PostSearchListView.as_view(), name='post-search'),

    path('post/<int:id>/comments/',
         CommentListView.as_view(), name='post-comments'),

    path('post/<int:id>/comments/new',
         CommentCreateView.as_view(), name='post-comment-create'),
    path('post/<int:id>/comments/<int:pk>/update',
         CommentUpdateView.as_view(), name='post-comment-update'),

    path('post/<int:id>/comments/<int:pk>/delete',
         CommentDeleteView.as_view(), name='post-comment-delete'),



    path('about/', views.about, name='blog-about'),
]
