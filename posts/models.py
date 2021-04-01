from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from accounts.models import User
# Create your models here.

class PostManager(models.Manager):
    def published(self):
        return self.filter(status = 'p')


class Post(models.Model):
    STATUS_CHOISES = (
        ('d','Draft'),
        ('p','Publish')
    )
    image = models.ImageField(upload_to='post/%Y/%m/%d')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts',null=True)
    description = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS_CHOISES,default='d')
    like = models.ManyToManyField(User,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']    

    def __str__(self):
        return '{}-{}'.format(self.user,self.description)

    def image_tag(self):
        return format_html("<img src='{}' width =60 height=50>".format(self.image.url))    
    image_tag.short_description = 'image'    

    def get_absolute_url(self):
        return reverse('posts:post-list')

    objects = PostManager()



class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='ucomment')
    reply = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name='rcomment')
    post = models.ForeignKey(Post,on_delete=models.CASCADE,blank=True,null=True,related_name='pcomment')
    is_reply = models.BooleanField(default=False)
    body = models.CharField(max_length=300)

    def __str__(self):
        return '{}-{}'.format(self.user,self.body)


    def get_absolute_url(self):
        return reverse('posts:post-list')    