from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'author', 'category', 'content', 'status', 'publish_date']
    list_display = ('title', 'author' ,'counted_view', 'status', 'publish_date', 'created_date')
    list_filter = ['status', 'created_date']
    search_fields = ['title', 'content']
    ordering = ['-created_date']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']