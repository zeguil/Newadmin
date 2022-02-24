from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, cpf,  password=None):
        if not cpf:
            raise ValueError('O usuário deve ter um CPF')
        user = self.model(cpf=cpf)
        user.save()
        return user

    def create_superuser(self, cpf, password=None):
        user = self.model(cpf=cpf)
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user



class User(AbstractBaseUser):
    
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'publicador'),
        (3, 'comun')
    )

    cpf = models.CharField(max_length=25,unique=True)
    tipo = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = MyUserManager()
    USERNAME_FIELD = 'cpf'

    @property
    def is_admin(self):
        return self.admin

    def has_perm(self, obj=None):
        return True

    def has_module_perms(self, obj=None):
        return True
    