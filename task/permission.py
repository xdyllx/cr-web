from rest_framework import permissions

from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening



class IsAdminUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user is not None:
            return True
