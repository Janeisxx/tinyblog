from django.contrib.syndication.views import  Feed
from .models import Post
class AllPostFeed(Feed):
    title = '秀秀写的博客'
    link = '/index/'
    description = '博客项目展示'

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s]%s'%(item.category,item.title)

    def item_description(self, item):
        return item.content



