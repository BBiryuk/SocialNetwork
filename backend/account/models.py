from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.conf import settings


class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9_]+$', 'Имя пользователя может содержать символы a-Z, 0-9 и _')],
    )
    email = models.EmailField(unique=True, blank=False, null=False)
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    favorite_users = models.ManyToManyField('self')
    bio = models.TextField()

    def add_favorite_user(self, user):
        if not self.is_favorite_user(user):
            self.favorite_users.add(user)
            self.save()

    def remove_favorite_user(self, user):
        if not self.is_favorite_user(user):
            self.favorite_users.remove(user)
            self.save()

    def is_favorite_user(self, user):
        if user in self.favorite_users.all():
            return True
        return False
    
    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
