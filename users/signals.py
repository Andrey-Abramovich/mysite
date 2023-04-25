from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import redirect


User = get_user_model()


# Сигнал на создание пользователя
@receiver(post_save, sender=User)
def user_register(sender, instance, created, **kwargs):
    user = instance
    if created:
        send_mail('Кто-то зарегистрировался',
                  f'Пользователь {user} зарегистрировался',
                  'andrey-abtest@yandex.ru',
                  ['andrey-abtest@yandex.ru'])
        return redirect('profile')