from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .utils import CustomValidation, is_strong_password
# Create your views here.

# Create your views here.
@api_view(['POST'])
def signup(request):
    """
    register user api view.
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            # check if passsword passes the strong password criteria
            is_password_strong = is_strong_password(password)
            # if it fails, then raise a validation error
            if not is_password_strong:
                return Response({'error': 'Password must be 8+ characters with uppercase, lowercase, digits, and special characters.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
