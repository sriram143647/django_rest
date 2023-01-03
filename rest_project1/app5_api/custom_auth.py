import imp
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class custom_authentication(BaseAuthentication):
    def authenticate(self, request):
        user_name = request.GET.get('username')
        if user_name is None:
            return None
        
        try:
            user = User.objects.get(username=user_name)
        except User.DoesNotExist:
            raise AuthenticationFailed("User Doesn't Exists")
        return (User,None)