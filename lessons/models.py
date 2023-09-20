from django.db import models
from django.contrib.auth import get_user_model

CHOICES = (('Просмотрено', 'Просмотрено'),
           ('Не просмотрено', 'Не просмотрено')
           )


class Product(models.Model):
    owner = models.CharField(max_length=64)
    users = models.ManyToManyField(get_user_model())


class Lesson(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=512)
    length = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    users = models.ManyToManyField(get_user_model(), through='Progress')


class Progress(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)
    date_last = models.DateField(default=None)
    status = models.CharField(max_length=14, choices=CHOICES, default='Не просмотрено')

    def __str__(self):
        return self.lesson.name
