from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='image/', null=True)

    def __str__(self):
        return '{}'.format(self.title)



class Respond(models.Model):
    respauthor = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Ваше сообщение')
    status = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(upload_to='uploads/', null=True, verbose_name='Загрузите Ваше фото')

    def __str__(self):
        return '{}'.format(self.text)
