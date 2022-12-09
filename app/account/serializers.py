from enum import unique
from rest_framework import serializers
from .models import User, Player, AdminUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from drf_writable_nested import WritableNestedModelSerializer
from django.utils.translation import gettext_lazy as _


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "password", "password2"]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(_('Пароли должны совпадать'))
        return data


    def save(self):
        user = User(username=self.validated_data['username'],
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]
        read_only_fields = ['username',]

    # def validate_email(self, value):
    #         user = self.context['request'].user
    #         if User.objects.exclude(pk=user.pk).filter(email=value).exists():
    #             raise serializers.ValidationError(_({"email": "Этот email уже используется"}))
    #         return value


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
        read_only_fields = ['user',]


class PlayerProfileSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Player
        fields = "__all__"

    

class PlayerCreateSerializer(UserCreateSerializer):
    player = PlayerSerializer()

    class Meta:
        model = User
        fields = ['player', 'username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True}
        }
    

    def save(self):
        user = User(username=self.validated_data['username'],
                    email=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    is_staff=self.validated_data['is_staff'],
                    is_superuser=self.validated_data['is_superuser']
                    )
        user.set_password(self.validated_data['password'])
        user.save()
        player = Player(
            user=user, 
            city=self.validated_data['player']['city'],
            birthdate=self.validated_data['player']['birthdate'],
            gender=self.validated_data['player']['gender'],
            phone_number=self.validated_data['player']['phone_number']
            )
        player.save()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(_({"password": "Пароли не совпадают"}))
        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(_({"old_password": "Старый пароль неправильный"}))
        return value


    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.pk != instance.pk:
            raise serializers.ValidationError(_({'authorize': "You don't have permission for this user"}))
        instance.set_password(validated_data['password'])
        instance.save()

        return instance

    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token
