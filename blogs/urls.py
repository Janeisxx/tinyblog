from django.conf.urls import url,include
from .views import PostListView,PostDetailView,PostCateView
from .views import getPostByCate,getPostByTag,getPostByCreateMonth
from .views import search_post
from .feeds import  AllPostFeed
app_name = 'blogs'
urlpatterns = [

    url(r'^index',PostListView.as_view(),name='index'),
    url(r'^detail/(?P<pk>\d+)',PostDetailView.as_view(),name='detail'),
    url(r'^category/(?P<pk>\d+)',PostCateView.as_view(),name='cate'),
    url(r'^tag/(?P<id>\d+)', getPostByTag, name='tag'),
    url(r'^month/(?P<month>\d+)', getPostByCreateMonth, name='bymonth'),
    url(r'^all/rss/$',AllPostFeed(),name = 'rss'),

    # url(r'^search/$',search_post,name='search'),



]
