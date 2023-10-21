from django.shortcuts import reverse
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    class Meta:
        ordering = ["-last_update", ]

    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = models.ImageField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_list")
