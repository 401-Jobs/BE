from rest_framework.permissions import BasePermission

class IsJobSeeker(BasePermission):
    def has_permission(self, request, view):

        print("INISDE PERMISSION : ", request.user.is_authenticated)
        print("IS COMPANY : ", request.user.is_company) 

        if  request.user.is_authenticated and not request.user.is_company:
            return True
        return False

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("IS OWNER  : ", request.user==obj.owner )

        if  request.user==obj.owner:
            return True
        else:
            return False
