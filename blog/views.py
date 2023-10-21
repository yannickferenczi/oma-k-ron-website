from django.shortcuts import render
from django.views import generic

from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = "blog/post_list.html"
