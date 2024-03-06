from rest_framework import serializers
from .models import User
from rest_framework import status


# user serializer create
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'password',
        )

        extra_kwargs = {
            'password': {'write_only': True},
          
        }

    # create user from validated data
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
