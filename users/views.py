from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm,EditForm

# Create your views here.


'''
表单如何传递next想了一会儿,避免后面忘记,把这个过程剖析一下.

第一步:
从注册链接点击,交给href="{% url 'users:register' %}?next={{ request.path }}"处理
http://127.0.0.1:8000/users/register?next=/index(假设从index页面点击)
get 请求

第二步
url 'users:register'对应views.register 处理get请求
从get请求获取next
渲染到users/register.html页面--传递的上下文变量是{form:未填写的空form,next(next-1):从get请求获取}

第三步
用户第一次打开注册页面users/register页面
页面中存在的 <input type="hidden" name="next" value="{{ next }}">
其中,这个input的值value="{{ next }}",就是上面第二步渲染而传过来的next(next-2)

第四步
用户填写form表单后提交,同时把页面的next提交上去
提交的内容是{form:用户填写好的,next(next-3),从第三步获取的next(next-3))

第五步
form的action属性,action="{% url 'users:register' %}"
表单提交后还是交给views.register处理,这次是处理post请求
再次获取next(post请求传递的next)

'''
def register(request):
    # form = UserCreationForm()
    redirect_to = request.POST.get('next', request.GET.get('next',''))
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            if redirect_to:
                return redirect(redirect_to)
            else:

                return redirect(reverse('blogs:index'))
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {"form":form, 'next':redirect_to})

@login_required(login_url='/users/login/')
def edit(request,pk):
    # 判断request的请求方法，如果是post方法，那么就处理数据
    if request.method == 'POST':
        # 获取前台传过来的数据，用来生成form对象
        form = EditForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            # 如果用户不修改头像,request.FILES无法获取头像,就用原来的
            user.headshot = request.FILES.get('headshot',request.user.headshot)
            user.save()
            # 保存成功,提示用户
            messages.success(request,'用户信息修改成功')
    form = EditForm(instance=request.user)
    # 如果是get方法,返回用户信息修改页面
    return render(request,'users/edit_form.html',{'form':form})







