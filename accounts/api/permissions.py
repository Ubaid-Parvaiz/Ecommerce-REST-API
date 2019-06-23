from rest_framework import permissions

class Allow_UA(permissions.BasePermission):
    """
    Global permission check for blacklisted IPs.
    """

    def has_permission(self, request, view):
        
        return not request.user.is_authenticated()