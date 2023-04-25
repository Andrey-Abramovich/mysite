from django.urls import path

from .views import *

urlpatterns = [
    path('', testview, name='test'),
    path('profile/', profileview, name='profile'),
    path('sendmessage/', RespondCreate.as_view(), name='message'),
    path('messages/', Responds.as_view(), name='messages'),
]
