from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path("", views.postsList, name="list"),
    path("<slug:slug>/", views.postPost, name="post"),
]
