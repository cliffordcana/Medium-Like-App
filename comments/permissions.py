from rest_framework import permissions

class IsFacebookUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        obj.user = not request.user

        if obj.user:
            return True
        return True