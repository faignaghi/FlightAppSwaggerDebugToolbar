from rest_framework import serializers, validators
from django.contrib.auth.models import User                                     # same
from django.conf import settings                                                # same
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators = [validators.UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True,
        required= True,
        validators = [validate_password],
        style = {"input_type": "password"}
    )
    
    password1 = serializers.CharField(
        write_only=True,
        required= True,
        validators=[validate_password],
        style={"input_type": "password"}
    )
    
    
    
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password1'
        )
        
        
        
    def validate(self, data):
        if data['password'] != data['password']:
            raise serializers.ValidationError(
                {"pasword: Password didn't match.... "}
            )
        return data
    
    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop('password1')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user