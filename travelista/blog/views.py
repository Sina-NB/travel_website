from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime

# Create your views here.
def blog_index_view(request):
    posts = Post.objects.filter(status=1, publish_date__lte=datetime.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-index.html', context)

def blog_single_view(request, pid):
    post = get_object_or_404(Post, id=pid, status=1, publish_date__lte=datetime.now())
    if post is not None:
        post.counted_view += 1
        post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def blog_category_view(request, category_name):
    posts = Post.objects.filter(status=1, publish_date__lte=datetime.now(), category__name=category_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-index.html', context)