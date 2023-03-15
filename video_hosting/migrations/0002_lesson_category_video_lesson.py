# Generated by Django 4.1.7 on 2023-03-15 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video_hosting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('persons', models.ManyToManyField(db_index=True, related_name='persons', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='lesson', to='video_hosting.lesson'),
        ),
    ]