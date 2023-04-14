from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Post(models.Model):
    author = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default= 'blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category, related_name='post')
    #tag
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField()
    publish_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
