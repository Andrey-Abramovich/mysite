# Generated by Django 4.1.7 on 2023-03-15 15:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_hosting', '0003_alter_category_persons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='persons',
            field=models.ManyToManyField(db_index=True, related_name='persons', to=settings.AUTH_USER_MODEL),
        ),
    ]
