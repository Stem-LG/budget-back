from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['POST'])
def login(request):
    if(request.data['username']):
        user = get_object_or_404(User, username=request.data['username'])
    else:
        user = get_object_or_404(User, email=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"message":"Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    token, created = Token.objects.get_or_create(user=user)

    return Response({"message":"Logged in","token":token.key, "user":UserSerializer(user).data})    



@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
   
    return Response(serializer.errors, status=status.HTTP_200_OK)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def logout(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]

    print("token: ",token)

    Token.objects.get(key=token).delete()
    
    return Response({"message":"Logged out"})
        
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response({"message":"logged_in", "user": UserSerializer(request.user).data})
