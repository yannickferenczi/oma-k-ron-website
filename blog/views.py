from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify


from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = "blog/post_list.html"


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        return render(request, "blog/post_detail.html", {"post": post})


class PostCreateView(SuccessMessageMixin, PermissionRequiredMixin, CreateView):
    """
    This class creates a Review instance.

    Users must be logged into their personal account to access this content.
    """

    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    permission_required = "blog.create_post"
    success_message = "Your post has been successfully added to the database!"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostEditView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    """
    This class update the selected Review instance.

    Users must be logged into their personal account to access this content.
    """

    model = Post
    form_class = PostForm
    template_name = "blog/edit_post.html"
    permission_required = "blog.update_post"
    success_message = "Your post has been successfully updated!"
