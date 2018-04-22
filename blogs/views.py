from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.utils.text import slugify
from django.db.models import Q

import markdown
from markdown.extensions.toc import TocExtension

from .models import Post,Category,Tag
from comments.forms import CommentForm
from utils import custom_paginator

from django.db.models import F

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    context_object_name = 'post_list'
    # ListView通过paginate_by开启分页,每页两条数据
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().order_by('-created_time')

    def get_context_data(self, **kwargs):
        # 先调用父类方法,获取默认的context
        context = super().get_context_data()
        # ListView传递了和分页有关的模板变量
        # paginator是Paginator的实例,is_paginated是否已分页
        # page_obj 当前请求页面的分页对象
        # object_list 请求页面的对象列表.和post_list等价,注意是请求页
        pagiator = context.get('paginator')
        page = context.get('page_obj')
        start,end = custom_paginator(page.number,pagiator.num_pages,4)
        context.update({
            'page_range':range(start,end+1)
        })
        return context



def getPostByCate(request,id):
    # cate = Category.objects.get(id=id)
    cate = get_object_or_404(Category,id=id)
    post_list = cate.post_set.all()
    return render(request,'blogs/index.html',locals())
class PostCateView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(Category,pk = self.kwargs.get('pk'))
        return super().get_queryset().filter(category=cate)

def getPostByTag(request,id):
    tag = get_object_or_404(Tag,id=id)
    post_list = tag.post_set.all()
    return render(request,'blogs/index.html',locals())
def getPostByCreateMonth(request,month):
    post_list = Post.objects.filter(created_time__month=month)
    return render(request,'blogs/index.html',locals())


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/detail.html'
    context_object_name = 'post'

    # 因为要调用增加阅读量方法,重写get方法
    # 能否使用F对象替换模型的increase_views()方法,怎样调用,在哪里^*-*^
    # self.objects.update(views=F('views')+1)

    # get方法返回的是一个HttpResponse
    def get(self,*args,**kwargs):
        response = super().get(*args,**kwargs)
        # 调用get方法才会获得object实例
        self.object.increase_views()
        # 这个函数必须返回一个HttpResponse对象
        return response


    def get_object(self, queryset=None):
        post = super().get_object()
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.content = md.convert(post.content)
        post.toc = md.toc
        return post



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = context['post']
        comment_list = post.comment_set.all()
        form = CommentForm()
        context.update({
            'comment_list':comment_list,
            'form':form,
        })
        return context




def search_post(request):
    # q = request.POST.get('q',request.GET.get('q',''))
    q = request.GET.get('q')
    # err_msg = ''
    if not q:
        err_msg = '请输入关键字'
        return  render(request,'blogs/index.html',{'err_msg':err_msg})
    post_list = Post.objects.filter(Q(title__icontains=q)|
                                    Q(content__icontains=q))
    return render(request,'blogs/index.html',{'post_list':post_list})
