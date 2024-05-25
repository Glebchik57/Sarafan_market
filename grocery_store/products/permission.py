from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Разрешение доступа к объекту только владельцу"""

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
