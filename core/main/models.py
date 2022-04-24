import jsonfield
from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField('Book name', max_length=50)
    link = models.CharField('Book link', max_length=200)
    section=models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'