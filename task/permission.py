from rest_framework import permissions

def is_admin_user(username):
    return username in ['xudongyi']


class IsAdminUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user is not None:
            return is_admin_user(request.user.username)