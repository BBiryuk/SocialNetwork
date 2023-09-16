from django.db import models
from post.models import Post
from account.models import User
from django.contrib import humanize


class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'System'), (2, 'CommentOnPost'), (3, 'Favorite'), (4, 'AddPostToFavorites'), (5, 'AddUserToConversation'))

    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextChoices()
    is_seen = models.BooleanField(default=False)
    type = models.IntegerField(choices=NOTIFICATION_TYPES)

    def get_created_date(self):
        return humanize.naturaltime(self.created_at)

    def get_preview(self):
        return self.content[:20]
    