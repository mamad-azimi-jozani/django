from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request,"blog/blog-home.html",context)


def blog_single(request,pid):
    post = get_object_or_404(Post, id=pid, status=1)
    context = {"post": post}
    return render(request, "blog/blog-single.html", context)
