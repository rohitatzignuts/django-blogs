from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.
def postsList(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "posts/list.html", {"posts": posts})


def postPost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post.html", {"post": post})


@login_required(login_url="/users/login/")
def postNew(request):
    return render(request, "posts/new_post.html")
