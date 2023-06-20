from rest_framework.permissions import BasePermission


class AmI(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.account_name == obj.account_name