from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

def user_file_path(instance, filename):
    return f'articles/{instance.article.key}/{instance.order}.jpg'


class Article(models.Model):
    key = models.CharField(default=get_random_string(length=11), max_length=11, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    save_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='save_articles')
    description = models.TextField()
    private = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class MediaFile(models.Model):
    order = models.IntegerField()
    media_file = models.ImageField(upload_to=user_file_path)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='files')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.CharField(max_length=300)
    main_comment = models.ForeignKey(
        'self',
        related_name='sub_comment',
        on_delete=models.CASCADE,
        null=True
    )

