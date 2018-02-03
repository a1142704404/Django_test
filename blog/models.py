from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
from django.core.urlresolvers import reverse

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)  #CharField指定了name类型为字符型
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField() #文章正文可能是大段文字，用textfield

    created_time = models.DateTimeField() #创建的时间
    modified_time = models.DateTimeField() #修改的时间

    excerpt = models.CharField(max_length=200,blank=True) #文章摘要

    category = models.ForeignKey(Category)   #分类
    tags = models.ManyToManyField(Tag,blank=True)   #标签

    author = models.ForeignKey(User) #作者

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})




