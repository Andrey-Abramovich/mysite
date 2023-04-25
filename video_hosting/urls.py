from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='hello'),
    path('about/', views.about, name='about'),
    path('otoskopia/', views.otoskopia, name='otoskopia'),
    path('sertificats/', views.sertificats, name='sertificats'),
    path('divers_first_aid/', views.divers_first_aid, name='divers_first_aid'),
    path('school_first/', views.school_first, name='school_first'),
    path('category/<slug:category_slug>/', views.get_list_lessons, name='lessons'),
    path('stream/<slug:video_slug>/', views.get_streaming_video, name='stream'),
    path('<slug:video_slug>/', views.get_video, name='video'),
    path('lesson/<slug:lesson_slug>/', views.get_video_lessons, name='video-lessons'),

    path('home/', views.get_list_video, name='home'),

    # path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    # path('<int:pk>/', views.get_video, name='video'),
]
