from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ("title", "slug", "published", "last_update")
    search_fields = ["title", "content", ]
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("published", "last_update", )
    summernote_fields = ("content")
