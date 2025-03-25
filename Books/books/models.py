from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=16)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return f"{self.title} ({self.author})"