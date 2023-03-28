from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    description = models.CharField(
        verbose_name='Описание',
        null=False,
        blank=False,
        max_length=300
    )
    image = models.ImageField(
        verbose_name='Фото',
        null=False,
        blank=False,
        upload_to='posts'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE)

    likes = models.ManyToManyField(
        verbose_name='Лайк',
        to=get_user_model(),
        related_name='like_post',
        default=None
    )

    def count_likes(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='authors',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Публикация',
        to='posts.Post',
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='Текст',
        null=False,
        blank=False,
        max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    changed_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата изменения'
    )

    def __str__(self):
        return f'{self.text}'
