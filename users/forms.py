
from allauth.socialaccount.forms import SignupForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm

from users.models import Respond

User = get_user_model()


class SendRespondForm(ModelForm):
    class Meta:
        model = Respond
        fields = ['upload', 'text']

class MyCustomSocialSignupForm(SignupForm):
    class Meta:
        model = User
        fields = ['username', ]
    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSocialSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

