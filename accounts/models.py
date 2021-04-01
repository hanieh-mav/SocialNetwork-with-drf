from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d')
    bio = models.CharField(max_length=100,blank=True)
   

    def get_absolute_url(self):
        return reverse('accounts:profile',args=[self.pk,]) 


class Friend(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower',null=True)
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following',null=True)

