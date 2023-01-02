from rest_framework.permissions import BasePermission

class my_permission(BasePermission):
    def has_permission(self,request,view):
        if request.method == 'GET':
            return True
        return False