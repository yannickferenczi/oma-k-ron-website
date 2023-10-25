from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostList.as_view(), name="post_list"),
    path(
        "post_detail/<slug>/",
        views.PostDetail.as_view(),
        name="post_detail",
    ),
    path("create_post/", views.PostCreateView.as_view(), name="create_post"),
    path("edit_post/<slug>/", views.PostEditView.as_view(), name="edit_post"),
    path(
        "delete_post/<slug>/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
]
