from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешение редактировать объект только Администратору"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
