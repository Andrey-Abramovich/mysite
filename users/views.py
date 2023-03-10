from django.shortcuts import render

def testview(request):
    template_name = 'main.html'
    return render(request, template_name)

def profileview(request):
    template_name = 'users/profile.html'
    return render(request, template_name)
