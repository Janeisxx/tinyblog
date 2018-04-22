from django.shortcuts import render, redirect
from blogs.models import Post
from.models import Comment
from django.shortcuts import get_object_or_404
from .forms import  CommentForm

# Create your views here.


# 这里这样写提交评论后到comments/post1路径了,为什么没到detail呢
# def post_comment(request,id):
#     post = get_object_or_404(Post, id=id)
#     # 先获取评论列表.即使新的评论没有提交,博文原来的评论仍能展示
#     comment_list = post.comment_set.all()
#     if request.method == 'POST':
#         name = request.POST.get('name','')
#         email = request.POST.get('email','')
#         url = request.POST.get('url','')
#         text = request.POST.get('text','')
#         comment = Comment(post=post,
#                           name=name,
#                           email=email,
#                           url=url,
#                           text=text,
#                           )
#         comment.save()
#         # 新提交了comment,更新comment_list
#         comment_list = post.comment_set.all()
#         return render(request, 'blogs/detail.html', {
#             'post':post,
#             'comment_list':comment_list,
#         })
#     return render(request,'blogs/detail.html',locals())


# 另一种,用ModelForm
# 重写犯了一个错误,就是点进去发现form表单的输入框根本就没有展示出来
# 原因是:blogs/detail.html这个界面,不光这个函数渲染,还有PostDetailView在渲染
# form是默认get请求的时候就传过去的,因为即使没有人评论,也是可以展示那个评论框的
# 所以用ModelForm来生成form表单,也需要在PostDetaiView给detail页面传入form

def post_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # 这里redirect的post和最后一行比,多了这个存起来的comment
            return redirect(post)
        else:
            # 渲染表单的错误
            # 到这里不能直接redirect(post),传入的变量要手动写
            comment_list = post.comment_set.all()
            context={
                'post':post,
                'form':form,# 渲染这个错误表单
                'comment_list':comment_list,
            }

            return render(request,'blogs/detail.html',context)
    return redirect(post)







