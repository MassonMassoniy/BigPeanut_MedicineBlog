from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)
from .managers import UserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    ADMIN, DOCTOR, MODERATOR, BLOG_USER = range(1,5)

    ROLE_TYPES = (
        (ADMIN, 'Администратор'),             #1
        (MODERATOR, 'Модератор'),             #2
        (BLOG_USER, 'Читатель'),              #3
        (DOCTOR, 'Врач'),                     #4
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    account_name = models.CharField('Логин', max_length=50, default='', unique=True)
    username = models.CharField("ФИО", max_length=100, default='', blank=True, null=True)
    email = models.EmailField("Почта", default="email@mail.com", blank=True, null=True)
    role = models.IntegerField(verbose_name='Роль', default=BLOG_USER, choices=ROLE_TYPES)
    date_joined = models.DateTimeField("Дата присоединения", blank=True, null=True, default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default = True,
        verbose_name = 'Статус доступа',
    )

    USERNAME_FIELD = "account_name"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)