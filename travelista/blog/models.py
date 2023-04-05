from django.db import models

# Create your models here.
class Post(models.Model):
    #author = models.CharField(max_length=255)
    #image
    title = models.CharField(max_length=255)
    content = models.TextField()
    #category
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
        verbose_name_plural = 'Posts '