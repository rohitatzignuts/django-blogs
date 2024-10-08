from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def postsList(request):
    search_q = request.GET.get("search", "")
    post_list = Post.objects.all().order_by("-date")

    # If there is a search query, filter posts based on title or body
    if search_q:
        post_list = post_list.filter(
            Q(title__icontains=search_q) | Q(body__icontains=search_q)
        )
    paginator = Paginator(post_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "posts/list.html",
        {
            "posts": page_obj.object_list,
            "page_obj": page_obj,
            "search_q": search_q,
        },
    )


def postPost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post.html", {"post": post})


@login_required(login_url="/users/login/")
def postNew(request):
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect("/")
    else:
        form = forms.CreatePost()
    return render(request, "posts/new_post.html", {"form": form})
