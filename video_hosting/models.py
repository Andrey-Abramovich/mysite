from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField()
    image = models.ImageField(upload_to='image/')
    file = models.FileField(
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# class Category(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name