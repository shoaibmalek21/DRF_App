from rest_framework.permissions import DjangoModelPermissions
from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

# Rights need only for CreateUpdateDelete actions.
class CRUDModelPermissions(DjangoModelPermissions):
  perms_map = {
      'GET': [],
      'OPTIONS': [],
      'HEAD': ['%(app_label)s.read_%(model_name)s'],
      'POST': ['%(app_label)s.add_%(model_name)s'],
      'PUT': ['%(app_label)s.change_%(model_name)s'],
      'PATCH': ['%(app_label)s.change_%(model_name)s'],
      'DELETE': ['%(app_label)s.delete_%(model_name)s'],
  }

class AdminsPermissions(BasePermission):
    allowed_user_roles = (User.SUPERVISOR, User.ADMINISTRATOR)

    def has_permission(self, request, view):
        is_allowed_user = request.user.role in self.allowed_user_roles
        return is_allowed_user
