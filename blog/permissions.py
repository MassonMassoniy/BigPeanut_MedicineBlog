from rest_framework.permissions import BasePermission
from authorization.models import User

'--------------------------------------------------------------------------------------------------'
    
class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.ADMIN


class IsADoctor(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == User.DOCTOR


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user