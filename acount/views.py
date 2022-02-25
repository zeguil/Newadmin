from .models import User
from .serializers import UsuarioSerializer
from rest_framework import viewsets, generics
from .permissions import IsAdmin, IsPublisher, IsUser

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    # permission_classes = [IsAdmin]

    # permission_classes_by_action = {'create': [IsAdmin],
    #                                 'list': [IsPublisher, IsAdmin]}

class ListaUsuarios(generics.ListAPIView):

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset
    serializer_class = UsuarioSerializer