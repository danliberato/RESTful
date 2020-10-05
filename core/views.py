from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializer import UserSerializer
import json


class UserView(APIView):
    def process_view(self, request):
        pass

    def get(self, request, document=None):
        try:
            if document:
                try:
                    u = {
                        "name": "Rest User",
                        "document": "12345678900",
                        "email": "rest.user@example.com"
                    }
                    return Response(UserSerializer(u).data, status=status.HTTP_200_OK)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': "Document not present in call"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            try:
                c = User.objects.get(document=request.data['document'])
                return Response({'error': 'Object already exists'}, status=status.HTTP_409_CONFLICT)
            except User.DoesNotExist:

                serialized = UserSerializer(request.data)
                if serialized.is_valid():
                    serialized.save()
                    return Response(UserSerializer(serialized.data).data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': serialized.errors}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, document=None):
        try:
            if document:
                try:
                    c = User.objects.get(document=document, active=True)

                    serialized = EditCustomerSerializer(c)
                    if serialized.is_valid():
                        serialized.save()
                        return Response(UserSerializer(serialized.data).data, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': serialized.errors}, status=status.HTTP_403_FORBIDDEN)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': "Document not present in call"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, document=None):
        try:
            if document:
                try:
                    c = User.objects.get(document=document)
                    c.active = False

                    serialized = EditCustomerSerializer(c)
                    if serialized.is_valid():
                        serialized.save()
                        return Response(UserSerializer(serialized.data).data, status=status.HTTP_200_OK)
                    else:
                        return Response({'error': serialized.errors}, status=status.HTTP_403_FORBIDDEN)
                except User.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': "Document not present in call"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)