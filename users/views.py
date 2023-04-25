from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required

from users.forms import SendRespondForm
from users.models import Respond
from video_hosting.models import Category, Lesson

User = get_user_model()

def testview(request):
    template_name = 'base/main.html'
    return render(request, template_name)

@login_required
def profileview(request):
    categories = Category.objects.all().filter(persons__id=request.user.id)
    ears = categories.filter(id=2).exists()
    # print(ears)
    template_name = 'users/profile.html'
    context = {
        'categories': categories,
        'ears': ears,
        # 'cats': cats,
        # 'lesson': lesson
    }
    return render(request, template_name, context=context)


class RespondCreate(CreateView):
    model = Respond
    form_class = SendRespondForm
    template_name = 'users/respond.html'
    success_url = reverse_lazy('profile')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.respauthor = self.request.user
        self.object.save()
        return super().form_valid(form)

class Responds(ListView):
    model = Respond
    ordering = ['-dateCreation']
    template_name = 'users/responds.html'
    context_object_name = 'responds'
    paginate_by = 3