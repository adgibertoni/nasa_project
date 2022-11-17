from django.urls import path
from new import views

app_name = 'new'
urlpatterns =[
    path('news/',  views.NewListView.as_view(), name="new-list"),
    path("news/<int:pk>/detail/", views.NewDetailView.as_view(), name="new-detail"),
    ]