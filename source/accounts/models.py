from django.contrib.auth.models import AbstractUser
from django.db import models
from accounts.managers import UserManager


class Account(AbstractUser):
    GENDER_CHOICES = (
        ('MAN', "Мужской"),
        ('WOMAN', "Женский"),
    )

    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        null=False,
        blank=False
    )
    username = models.CharField(
        verbose_name='Имя',
        max_length=50,
        null=False,
        blank=False,
        unique=True
    )
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    user_info = models.TextField(
        max_length=300,
        verbose_name="Информация о пользователе",
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name='Номер телефона'
    )
    gender = models.CharField(
        verbose_name='Пол',
        choices=GENDER_CHOICES,
        max_length=100,
    )

    subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Account', blank="True",
                                           related_name='subscribers')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
