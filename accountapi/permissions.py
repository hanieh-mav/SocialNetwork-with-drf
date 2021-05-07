from rest_framework.permissions import BasePermission , SAFE_METHODS


class UpdateOwnProfile(BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self , request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in SAFE_METHODS:
            return True

        return bool (
            request.user.is_authenticated or obj.id == request.user.id
        )