from django import template
from ..models import Post,Category
register = template.Library()



@register.inclusion_tag("blog/popular-post.html")
def popular_post(arg=3):
    posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
    return {"posts": posts}


@register.inclusion_tag("blog/post-category.html")
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()

    return {"categories": cat_dict}