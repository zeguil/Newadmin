from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, generics
# from .permissions import CustomAuthentication
# from rest_framework.permissions import TokenAuthentication


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = (CustomAuthentication,)

class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UserSerializer
    