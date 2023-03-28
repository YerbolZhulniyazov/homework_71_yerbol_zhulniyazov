from django.contrib import admin
from posts.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'image', 'author']
    list_filter = ['id', 'description', 'image', 'author', 'likes']
    search_fields = ['id', 'description']
    fields = ['description', 'image', 'author']
    readonly_fields = ['id', 'likes']


admin.site.register(Post, PostAdmin)
