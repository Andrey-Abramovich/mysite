from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models

User = get_user_model()


class Video(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])],
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    lesson = models.ForeignKey('Lesson', db_index=True, on_delete=models.PROTECT, related_name='lesson', blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    persons = models.ManyToManyField(User, db_index=True, related_name='persons')
    image = models.ImageField(upload_to='image/', blank=True, null=True, default='../static/images/first_aid_divers.jpg')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    cat = models.ForeignKey(Category, db_index=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

