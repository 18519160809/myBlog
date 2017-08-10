from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from comments.models import Comment
from comments.forms import CommentForm


# Create your views here.


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    # path = request.path
    if request.method == 'POST':
        # 用户提交的数据存在 request.POST 中，这是一个类字典对象。
        # 我们利用这些数据构造了 CommentForm 的实例，这样 Django 的表单就生成了。
        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.post = post

            comment.save()

            return redirect(post)

        else:

            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)
