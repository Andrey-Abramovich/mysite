from django.urls import path
from . import views


urlpatterns = [
    path('stream/<slug:video_slug>/', views.get_streaming_video, name='stream'),
    path('<slug:video_slug>/', views.get_video, name='video'),
    path('', views.get_list_video, name='home'),

    # path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    # path('<int:pk>/', views.get_video, name='video'),
]
