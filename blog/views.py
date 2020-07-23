from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse

import operator
from functools import reduce
from django.db.models import Q

from .models import Post, Comment
from django.contrib.auth.mixins import (LoginRequiredMixin as LRmixin,
                                        UserPassesTestMixin as UPTmixin)
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView,)


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostListView(ListView):
    """docstring for PostListView"""
    model = Post
    template_name = 'blog/home.html'  # <app-name>/<model-name>_<view-type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    """docstring for PostListView"""
    model = Post


class PostCreateView(LRmixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LRmixin, UPTmixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LRmixin, UPTmixin, DeleteView):
    """docstring for PostListView"""
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False


class PostSearchListView(ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    model = Post
    paginate_by = 5
    template_name = 'blog/post_search_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        result = super(PostSearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(content__icontains=q) for q in query_list))
            )
            # above result query will be converted as:
            # SELECT * FROM blog_table WHERE content LIKE '%first_word%' AND
            # content LIKE '%second_word%' AND content LIKE '%third_word%'
        return result.order_by('-date_posted')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'object'
    paginate_by = 10

    def access_id(self):
        id = self.kwargs.get('id')

    def get_queryset(self):
        post_ = get_object_or_404(Post, id=self.kwargs.get('id'))
        return Comment.objects.filter(post=post_).order_by('-date_posted')


class CommentCreateView(LRmixin, CreateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs.get('id'))
        return super().form_valid(form)


class CommentUpdateView(LRmixin, UPTmixin, UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, id=self.kwargs.get('id'))
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True

        return False


class CommentDeleteView(LRmixin, UPTmixin, DeleteView):
    """docstring for PostListView"""
    model = Comment

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True

        return False

    def get_success_url(self):
        id = 0
        id = self.kwargs.get('id')
        return reverse('post-detail', kwargs={'pk': id})
        pass


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
