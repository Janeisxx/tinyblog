from django import template
from blogs.models import Post,Category,Tag
from django.db.models import Count
# Post是函数要用的model,换成你自己的.

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_post=Count('post')).filter(num_post__gt=0)

@register.simple_tag
def get_archives(num=5):
    return Post.objects.dates('created_time','month',order='DESC')[:num]

