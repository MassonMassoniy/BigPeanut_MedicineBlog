from django.db import models
from django.utils import timezone
from authorization.models import User

# Create your models here.

class Ip(models.Model):
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip


class Post(models.Model):
    
    RESEARCH, DISCUSSION, QUESTION = range(1,4)

    POSTS_TYPES = (
        (RESEARCH, 'Исследование'),                #1
        (DISCUSSION, 'Обсуждение'),                #2
        (QUESTION, 'Вопрос'),                      #3
    )

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь создавший пост', null=True, blank=True, related_name='post')
    title = models.CharField(verbose_name='Заголовок поста', max_length=255,default='', null=True, blank=True)
    description = models.TextField(verbose_name='Описание поста')
    text = models.TextField(verbose_name='Текст новости')
    post_type = models.IntegerField(verbose_name='Тип поста', default=DISCUSSION, choices=POSTS_TYPES)
    date_post = models.DateTimeField(default=timezone.now, verbose_name='Дата создания поста')
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
    
    def total_views(self):
        return self.views.count()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь оставивший комментарий', null=True, blank=True, related_name='comment_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост, к которому был оставлен комментарий', null=True, blank=True, related_name='comment_post')
    text = models.TextField(verbose_name='Текст комментария')
    date_comment = models.DateTimeField(default=timezone.now, verbose_name='Дата создания комментария')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self) -> str:
        return self.text