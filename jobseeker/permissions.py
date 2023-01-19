from rest_framework.permissions import BasePermission

class IsJobSeeker(BasePermission):
    def has_permission(self, request, view):

        print("INISDE PERMISSION : ", request.user.is_authenticated)

        if  request.user.is_authenticated and not request.user.is_company:
            return True
        return False

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("INISDE PERMISSION2 : ", request.user.is_authenticated )
        if  request.user==obj.owner:
            return True
        else:
            return False
class IsOwnerForMedia(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("INISDE PERMISSION 3: ", request.user.is_authenticated )
        if  request.user==obj.owner:
            return True
        else:
            return False