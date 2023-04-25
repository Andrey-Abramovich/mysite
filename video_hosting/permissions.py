from django.contrib.auth import get_user_model
from django.http import Http404

User = get_user_model()

class UserPermissionMixin:
    def has_permissions(self):
        return self.request.user in self.get_object().person

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            raise Http404
        return super().dispatch(request, *args, **kwargs)