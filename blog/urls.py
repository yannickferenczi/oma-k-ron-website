from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path("post_detail/<slug>/", views.PostDetail.as_view(), name="post_detail"),
]
