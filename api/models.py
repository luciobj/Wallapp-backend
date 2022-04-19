from django.db import models


class PostIt(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
      verbose_name = 'PostIt'
      verbose_name_plural = 'PostIts'

    def __str__(self):
        return self.title
