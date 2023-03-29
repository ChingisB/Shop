from django.contrib.auth.models import Permission

class StaffPermission(Permission):
    def has_permission(self, request, view):
        user = request.user
        return user.is_staff