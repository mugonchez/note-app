from rest_framework import serializers
from .models import User
from .utils import CustomValidation, is_strong_password
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
        password = validated_data.pop('password')

        # check if passsword passes the strong password criteria
        is_password_strong = is_strong_password(password)

        # if it fails, then raise a validation error
        if not is_password_strong:
            raise CustomValidation("Password must be 8+ characters with uppercase, lowercase, digits, and special characters.", "password", status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(**validated_data, password=password)

        return user
