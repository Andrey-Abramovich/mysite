from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video, Category, Lesson
from .services import open_file

User = get_user_model()


def index(request):
    return render(request, 'video_hosting/index.html')

def about(request):
    return render(request, 'video_hosting/about.html')

def school_first(request):
    return render(request, 'video_hosting/school_first.html')

def divers_first_aid(request):
    return render(request, 'video_hosting/divers_first_aid.html')

def otoskopia(request):
    return render(request, 'video_hosting/otoskopia.html')

def sertificats(request):
    return render(request, 'video_hosting/sertificats.html')

@login_required
def get_list_video(request):
    if User.has_perm(request.user, 'video_hosting.view_video'):
        return render(request, 'video_hosting/home.html', {'video_list': Video.objects.all()})
    return render(request, 'users/profile.html')


@login_required
def get_video(request, video_slug):
    _video = get_object_or_404(Video, slug=video_slug)
    return render(request, "video_hosting/video.html", {"video": _video})


@login_required
def get_streaming_video(request, video_slug):
    file, status_code, content_length, content_range = open_file(request, video_slug)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

# получаем список уроков в данной категории
def get_list_lessons(request, category_slug):
    cat = Lesson.objects.filter(cat__slug=category_slug)
    cat_person = Category.objects.filter(slug=category_slug).values('persons__id') # получаем список пользователей для данной категории
    is_person = cat_person.filter(persons__id=request.user.id).exists() # проверка наличия пользователя в списке
    template_name = 'video_hosting/lessons.html'
    context = {
        'cat': cat,
        'is_person': is_person
    }
    return render(request, template_name, context=context)

# получаем список видео по конкретному уроку
def get_video_lessons(request, lesson_slug):
    lessons = Video.objects.filter(lesson__slug=lesson_slug)
    cat_person = Category.objects.filter(lesson__slug=lesson_slug).values('persons__id')
    is_person = cat_person.filter(persons__id=request.user.id).exists()
    context = {
        'lessons': lessons,
        'is_person': is_person
    }
    template_name = 'video_hosting/home.html'
    return render(request, template_name, context=context)

