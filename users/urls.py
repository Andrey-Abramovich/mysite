from django.urls import path

from .views import testview, profileview

urlpatterns = [
    path('', testview, name='test'),
    path('profile/', profileview, name='profile'),
]
