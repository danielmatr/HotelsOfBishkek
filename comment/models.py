from django.db import models

from main.models import Post


class Created(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # для незаписи в базу данных


class Comment(Created):
    comment = models.TextField()
    author = models.ForeignKey('account.User', related_name='comments', on_delete=models.DO_NOTHING)
    abs = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ('-created', )
