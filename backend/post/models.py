from django.db import models
from account.models import User
from django.contrib.humanize.templatetags import humanize


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=False)
    likes = models.ManyToManyField(Like, blank=True)

    class Meta:
        ordering = ('-created_at',)

    def get_date(self):
        return humanize.naturaltime(self.created_at)
