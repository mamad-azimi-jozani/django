from django import template
from ..models import Post
register = template.Library()



@register.inclusion_tag("blog/popular-post.html")
def popular_post(arg=3):
    posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
    return {"posts": posts}
