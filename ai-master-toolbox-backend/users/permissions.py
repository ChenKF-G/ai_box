from rest_framework.permissions import BasePermission

from users.models import Feedback


class UserDetailViewPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True

        pk = view.kwargs.get('pk')
        if request.method == 'GET':
            return pk == 0

        if request.method == 'PUT':
            return False

        if request.method == 'DELETE':
            return False

        return False

class UserAssetsDetailViewPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        pk = view.kwargs.get('pk')
        if request.method == 'GET':
            return pk == 0

        if request.method == 'PUT':
            return False

        if request.method == 'DELETE':
            return False

        return False

class FeedBackPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        if request.method == 'POST':
            return True

        pk = view.kwargs.get('pk')
        feedback = Feedback.objects.get(pk=pk)

        if not feedback:
            return False

        return feedback.user.id == request.user.id

class FeedBackRepleyPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        if request.user.is_superuser:
            return True

        feedback_id = view.kwargs.get('feedback_id')
        feedback = Feedback.objects.get(id=feedback_id)
        if not feedback:
            return False

        return feedback.user.id == request.user.id

