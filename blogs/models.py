from django.db import models
# from django.contrib.auth.models import User
from users.models import User
import markdown



# Create your models here.
from django.urls import reverse
from django.utils.html import strip_tags


class Post(models.Model):
    author = models.ForeignKey(User)
    category = models.ForeignKey('Category')
    tag = models.ManyToManyField('Tag')


    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    content = models.TextField()
    excerpt = models.CharField(max_length=100,blank=True,null=True)
    title = models.CharField(max_length=20)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self,*args,**kwargs):
        if not self.excerpt:
            md=markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(md.convert(self.content))[:40]
        #     save方法创建新对象后才会生效
        super().save(*args, **kwargs)
        # super(Post,self).save(*args,**kwargs)
    def get_absolute_url(self):
        return reverse('blogs:detail',kwargs={'pk':self.pk})






class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name