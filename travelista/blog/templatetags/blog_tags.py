from django import template
from django.db.models import Count
from blog.models import Post, Category
from datetime import datetime

register = template.Library()


@register.inclusion_tag('blog/include/side-bar/latest-posts.html')
def latest_posts(num_posts=4):
    posts = Post.objects.filter(status=1, publish_date__lte=datetime.now()).order_by(
        '-publish_date')[:num_posts]
    return {'posts': posts}


@register.inclusion_tag('blog/include/side-bar/categories.html')
def categories():
    cat_count_sorted = Category.objects.annotate(
        number_of_posts=Count("post")).order_by('-number_of_posts')

    return {'categories': cat_count_sorted}
