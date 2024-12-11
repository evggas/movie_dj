from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=200)  # Название фильма
    description = models.TextField()  # Описание фильма
    review = models.TextField()  # Отзыв о фильме

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
