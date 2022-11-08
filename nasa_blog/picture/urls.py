from django.urls import path

from picture import views

app_name = "picture"
urlpatterns = [
    path("pictures/", views.PictureListView.as_view(), name="picture-list"),
    path("picture/add/", views.PictureCreateView.as_view(), name="picture-add"),
    path("picture/<int:pk>/detail/", views.PictureDetailView.as_view(), name="picture-detail"),
    path("picture/<int:pk>/update/", views.PictureUpdateView.as_view(), name="picture-update"),
    path("picture/<int:pk>/delete/", views.PictureDeleteView.as_view(), name="picture-delete"),
    path("comment/<int:pk>/add/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
]