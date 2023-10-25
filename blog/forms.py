from django import forms
from .models import Post

from django_summernote.widgets import SummernoteWidget


class PostForm(forms.ModelForm):
    """ A custom form to create and update blog posts """
    class Meta:
        model = Post
        fields = ["title", "content", "featured_image", "published"]

    content = forms.CharField(widget=SummernoteWidget)
