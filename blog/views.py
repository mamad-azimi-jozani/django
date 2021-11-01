from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1)
    context = {"posts": posts}
    return render(request,"blog/blog-home.html",context)


def blog_single(request):
    return render(request,"blog/blog-single.html")
