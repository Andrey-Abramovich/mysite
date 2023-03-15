from django.contrib.auth import get_user_model
from django.shortcuts import render
from video_hosting.models import Category, Lesson

User = get_user_model()

def testview(request):
    template_name = 'main.html'
    return render(request, template_name)

def profileview(request):
    # cats = Category.objects.all()
    # lesson = Lesson.objects.all()
    categories = Category.objects.all().filter(persons__id=request.user.id)
    # categories = Category.objects.all()
    print(categories)
    template_name = 'users/profile.html'
    context = {
        'categories': categories,
        # 'cats': cats,
        # 'lesson': lesson
    }
    return render(request, template_name, context=context)
