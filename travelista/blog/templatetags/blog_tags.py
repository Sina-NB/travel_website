from django import template
from blog.models import Post
from datetime import datetime

register = template.Library()

@register.inclusion_tag('blog/include/side-bar/latest-posts.html')
def latest_posts(num_posts=4):
    posts = Post.objects.filter(status=1, publish_date__lte=datetime.now()).order_by('-publish_date')[:num_posts]
    return {'posts':posts}
