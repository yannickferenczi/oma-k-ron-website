from django.shortcuts import render, get_object_or_404
from django.views import generic, View

from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = "blog/post_list.html"


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        return render(request, "blog/post_detail.html", {"post": post})
