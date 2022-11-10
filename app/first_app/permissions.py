from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

class IsStaffOrAny(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user.is_superuser or request.user.is_staff:
            return True


