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
