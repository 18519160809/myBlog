from django.http import JsonResponse

from blog.models import *
from django import template
register = template.Library()


@register.assignment_tag
# 最新文章
def get_recent_posts(num=5):
    posts = Post.objects.all().order_by('-created_time')[:num]
    print(posts)
    return posts


@register.assignment_tag
# 归档
def archives():
    # alist = Post.objects.dates('created_time', 'month', order='DESC')
    # return {'alist': alist}
    return Post.objects.datetimes('created_time', 'month', order='DESC')


@register.assignment_tag
# 分类
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()
