from django.db import models
from account.models import User
from django.contrib import humanize


class Conversation(models.Model):
    members = models.ManyToManyField(User, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_created_date(self):
        return humanize.naturaltime(self.created_at)

    def get_updated_date(self):
        return humanize.naturaltime(self.updated_at)


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_created_date(self):
        return humanize.naturaltime(self.created_at)

    def get_updated_date(self):
        return humanize.naturaltime(self.updated_at)
