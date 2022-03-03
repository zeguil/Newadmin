from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BasePermission):
   def authenticate(self, request):
      user = request.GET.get('cpf')
      if user is None:
         return None
      
      try:
         user = User.objects.get(cpf=self.request.user)
      except User.DoesNotExist:
         raise AuthenticationFailed('usuario não encontrado')
      return (user, None)
