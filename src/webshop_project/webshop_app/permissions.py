# import django permissions
from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to only edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user edits their own profile"""

        #check if request is a safe request
        if request.method in permissions.SAFE_METHODS:
            return True

        # if it is not a safe method, the id should be same as the user id.
        return obj.id == request.user.id
