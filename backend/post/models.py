from django.db import models
from account.models import User
from django.contrib.humanize.templatetags import humanize


class Comment(models.Model):
    body = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('created_at',)
    
    def get_date(self):
        return humanize.naturaltime(self.created_at)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name="blogpost", blank=True)
    comments = models.ManyToManyField(Comment, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def get_date(self):
        return humanize.naturaltime(self.created_at)

    def total_likes(self):
        return self.likes.count()
