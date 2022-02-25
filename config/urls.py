from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.contrib import admin
from django.urls import path
from acount.views import UsuariosViewSet, ListaUsuarios

router = routers.DefaultRouter()
router.register('cadastro', UsuariosViewSet, basename='Cadastrar Usuário')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-token-auth/", obtain_auth_token),
    path('cadastro/', ListaUsuarios.as_view())
]
