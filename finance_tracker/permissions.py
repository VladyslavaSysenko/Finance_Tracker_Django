from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# # Basic class
# class IsOwnerOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, obj):
#         return bool(request.user and (obj.user == request.user or request.user.is_staff))

# Classes for Viewsets
class UserPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return bool(request.user and request.user.is_staff)
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False
        
    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return bool(request.user and (obj == request.user or request.user.is_staff))
        elif view.action in ['update', 'partial_update','destroy']:
            return bool(request.user and (obj == request.user or request.user.is_staff))
        else:
            return False
    