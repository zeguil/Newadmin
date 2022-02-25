from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
   def has_permission(self, request, view):
      return request.user.admin

class IsPublisher(BasePermission):
   def has_permission(self, request, view):
      return request.user.publisher

class IsUser(BasePermission):
   def has_permission(self, request, view):
      if request.user.admin != True and request.user.publisher != True:
         return True