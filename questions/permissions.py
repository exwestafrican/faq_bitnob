from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    sets object-level permission to only allow owners 
    of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            # allow all users see data
            return True

        # returns True or false contigent on logic
        return bool(obj.user == request.user)
