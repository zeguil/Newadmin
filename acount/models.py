from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from rest_framework.authtoken.models import Token

class MyUserManager(BaseUserManager):
    def create_user(self, cpf,  password, **extra_fields):
        if not cpf:
            raise ValueError('O usuário deve ter um CPF')
        user = self.model(cpf=cpf, **extra_fields)
        Token.objects.create(cpf=cpf)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, cpf, password, **extra_fields):
        
        user = self.model(
            cpf=cpf,
            is_staff=True,
            is_superuser=True,
            is_active=True,
            )
        Token.objects.create(cpf=cpf)
        user.set_password(password)
        user.save()
        return user
        


 
class User(AbstractUser):
    cpf = models.CharField(max_length=10,unique=True)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    publisher = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    

    def __str__(self):
        return self.cpf
    

