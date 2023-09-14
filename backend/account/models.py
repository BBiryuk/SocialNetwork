from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Account(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        validators=[RegexValidator(r'^[a-zA-Z0-9_]+$', 'Имя пользователя может содержать символы a-Z, 0-9 и _')],
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.'
    )
    email = models.EmailField(unique=True, blank=False, null=False, help_text='Почта используется')
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    following = models.ManyToManyField()
    friends = models.ManyToManyField()
    bio = models.TextField()

