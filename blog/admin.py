from django.contrib import admin

# Register your models here.
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'excerpt', 'category', 'tag', 'author']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)