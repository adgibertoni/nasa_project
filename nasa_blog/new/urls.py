from django.urls import path
from new import views

app_name = 'new'
urlpatterns =[
    path('news/',  views.NewListView.as_view(), name="new-list"),
    path('new/add/', views.NewCreateView.as_view(), name="new-add"),
    path("new/<int:pk>/detail/", views.NewDetailView.as_view(), name="new-detail"),
    path('new/<int:pk>/update/', views.NewUpdateView.as_view(), name="new-update"),
    path("new/<int:pk>/delete/", views.NewDeleteView.as_view(), name="new-delete"),
    path("commentnew/<int:pk>/add/", views.CommentNewCreateView.as_view(), name="commentnew-create"),
    path("commentnew/<int:pk>/delete/", views.CommentNewDeleteView.as_view(), name="commentnew-delete"),
    ]