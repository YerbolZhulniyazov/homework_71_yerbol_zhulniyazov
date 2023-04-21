from rest_framework import permissions


class PermissionPost(permissions.BasePermission):
    @staticmethod
    def has_permission(request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        elif request.method in ('PUT', 'PATCH', 'DELETE'):
            return obj.author == request.user
        elif request.user.is_authenticated and request.method == "POST":
            return True


class PermissionAddLikeDelete(permissions.BasePermission):
    @staticmethod
    def has_permission(request, view, obj):
        if request.method in ("POST", 'DELETE'):
            return True
