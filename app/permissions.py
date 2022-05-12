from django.contrib.auth.models import Permission

class IsOwnwerOrReadOnly(Permission.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in Permission.SAFE_METHODS:
            return True
        return obj.user == request.user