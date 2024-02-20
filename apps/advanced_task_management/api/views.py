from typing import Any
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
import requests
from .services.conection_rick_and_morty import conection_rick_and_morty

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
class AddTaskView(APIView):
    def __init__(self, **kwargs: Any) -> None:
        self.service=conection_rick_and_morty()

    def post(self, request, *args, **kwargs):
        return self.service.RickIsLive()

    


