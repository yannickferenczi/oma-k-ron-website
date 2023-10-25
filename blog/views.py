from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify


from .models import Post
from .forms import PostForm


class PostList(generic.ListView):
    """ A CBV to display a list of all published blog posts """
    model = Post
    queryset = Post.objects.filter(published=True)
    template_name = "blog/post_list.html"


class PostDetail(View):
    """ A CBV to display the details of a blog post """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(published=True)
        post = get_object_or_404(queryset, slug=slug)
        return render(request, "blog/post_detail.html", {"post": post})


class PostCreateView(
        SuccessMessageMixin,
        PermissionRequiredMixin,
        CreateView):
    """
    This class creates a Post instance.

    Users must have the permission to add post to access this content.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/create_post.html"
    permission_required = "blog.add_post"
    success_message = "Your post has been successfully added to the database!"

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class PostEditView(SuccessMessageMixin, PermissionRequiredMixin, UpdateView):
    """
    This class update the selected Post instance.

    Users must have the permission to change post to access this content.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/edit_post.html"
    permission_required = "blog.change_post"
    success_message = "Your post has been successfully updated!"


class PostDeleteView(SuccessMessageMixin, PermissionRequiredMixin, DeleteView):
    """
    This class delete the selected Post instance.

    Users must have the permission to delete post to access this content.
    """
    model = Post
    template_name = "blog/delete_post.html"
    permission_required = "blog.delete_post"
    success_url = reverse_lazy("post_list")
    success_message = "Your post has been successfully deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(
            request,
            *args,
            **kwargs,
        )
