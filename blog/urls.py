from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path("", index, name="index"),
    path("<int:pid>", blog_single, name="single")

]