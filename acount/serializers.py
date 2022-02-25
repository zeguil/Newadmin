from .models import User
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Senha"
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label="Confirme a senha"
    )

    publisher = serializers.BooleanField(
        label="Membro da Equipe",
        help_text="Indica que usuário é publicador."
    )

    admin = serializers.BooleanField(
        label="SuperUsuário",
        help_text="Indica que este usuário tem todas as permissões sem atribuí-las explicitamente."
    )

    class Meta:
        model = User
        fields = ('cpf','password', 'password_confirm', 'publisher', 'admin','created_at', 'updated_at')
        extra_kwargs = {
            'password': {'write_only': True},
            'created_at' : {'write_only': True},
            'updated_at' :{'write_only': True}}

    def save(self):
        conta = User(
            username=self.validated_data['username'],
            publisher=self.validated_data['publisher'],
            admin=self.validated_data['admin']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password': 'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta