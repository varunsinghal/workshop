from django.http import HttpResponse
from django.shortcuts import render

from .forms import PostForm
from .models import Post


def index(request):
    return HttpResponse("Hello world")


def posts(request):
    posts = Post.objects.all()
    return render(request, "myapp/blog.html", {'posts': posts})


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.save()
        return HttpResponse("thanks!!")
    else:
        form = PostForm()
    return render(request, "myapp/new.html", {"form": form})
