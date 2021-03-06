"""tinyblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blogs.urls')),
    url(r'^comments/',include('comments.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^users/',include('django.contrib.auth.urls')),
    url(r'^users/',include('users.urls',namespace='users')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# 上传媒体文件需要加上这句 +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

'''
url(r'^users/', include('django.contrib.auth.urls')),
这将包含以下的 URL 模式：
^users/login/$ [name='login']
^users/logout/$ [name='logout']
^users/password_change/$ [  name='password_change']
^users/password_change/done/$ [name='password_change_done']
^users/password_reset/$ [name='password_reset']
^users/password_reset/done/$ [name='password_reset_done']
^users/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^users/reset/done/$ [name='password_reset_complete']

'''