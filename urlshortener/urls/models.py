from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class URL(models.Model):
    url = models.URLField(verbose_name='URL')
    hash = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', related_name='urls')
    visits_count = models.IntegerField(default=0, verbose_name='Clicks count')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return f'{self.url} - {self.hash}'
