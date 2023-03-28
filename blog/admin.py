from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on', 'like_count')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

    def like_count(self, obj):
        return obj.likes.count()
    like_count.short_description = 'Number of Likes'

admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')