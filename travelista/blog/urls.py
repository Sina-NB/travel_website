from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_index_view, name='index-page'),
    path('post/<int:pid>', views.blog_single_view, name='single-page'),
    path('category/<str:category_name>', views.blog_category_view, name='category_search')
]