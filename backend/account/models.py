from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    bio = models.TextField()

