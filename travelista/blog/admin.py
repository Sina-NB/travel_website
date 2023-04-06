from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'content', 'status', 'publish_date']
    list_display = ('title', 'counted_view', 'status', 'publish_date', 'created_date')
    list_filter = ['status', 'created_date']
    search_fields = ['title', 'content']
    ordering = ['-created_date']