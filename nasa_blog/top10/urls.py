from django.urls import path
from top10 import views

app_name = 'top10'
urlpatterns =[
    path('top10s/',  views.Top10ListView.as_view(), name="top10-list"),
    path("top10/<int:pk>/detail/", views.Top10DetailView.as_view(), name="top10-detail"),
    ]