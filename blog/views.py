from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"blog/blog-home.html")


def blog_single(request):
    return render(request,"blog/blog-single.html")
