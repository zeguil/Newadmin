from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-token-auth/", obtain_auth_token),
]
