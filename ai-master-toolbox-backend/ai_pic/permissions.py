from rest_framework.permissions import BasePermission
from users.models import UserAssets

class IdPhotoViewPermission(BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True

        if request.method == 'POST':
            return True
        if request.method == 'GET':
            return True