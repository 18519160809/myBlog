from django.contrib import admin

# Register your models here.
from comments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'created_time', 'post']

admin.site.register(Comment)

