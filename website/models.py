from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from tinymce.models import HTMLField


class User(AbstractUser):
    nickname = models.CharField(verbose_name="昵称", max_length=32, null=True, blank=True)

    def __str__(self):
        return self.nickname or self.username


class Plate(models.Model):
    title = models.CharField(verbose_name="版块", max_length=32)
    users = models.ManyToManyField(to=User, related_name='plates')

    def __str__(self):
        return '版块: {}'.format(self.title)


class Article(models.Model):
    title = models.CharField(max_length=64)
    content = HTMLField()
    create_time = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, related_name='articles')
    column = models.ForeignKey(to=Plate, related_name='articles')

    def comment_this(self, user: User, content: str):
        comment = Comment.objects.create(article=self, user=user, content=content)
        return comment

    def __str__(self):
        return '帖子: {}'.format(self.title)


class Comment(models.Model):
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(to=User, related_name='comments')
    article = models.ForeignKey(to=Article, related_name='comments')

    def __str__(self):
        return '回复: {}'.format(self.content)
