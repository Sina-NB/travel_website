from django.shortcuts import render
from blog.models import Post
from datetime import datetime

# Create your views here.
def blog_index_view(request):
    posts = Post.objects.filter(status=1, publish_date__lte=datetime.now())
    context = {'posts': posts};
    return render(request, 'blog/blog-index.html', context)

def blog_single_view(request):
    return render(request, 'blog/blog-single.html')
