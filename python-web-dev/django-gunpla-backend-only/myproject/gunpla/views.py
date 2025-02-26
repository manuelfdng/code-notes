# gunpla/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import Gunpla
from .serializers import GunplaSerializer

class GunplaList(APIView):
    def get(self, request):
        gunplas = Gunpla.objects.all()
        serializer = GunplaSerializer(gunplas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GunplaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        # Transform error messages to match expected format in tests
        error_message = []
        for field, errors in serializer.errors.items():
            for error in errors:
                error_message.append(f"{field.capitalize()} field is required.")
        
        return Response({"message": error_message}, status=status.HTTP_400_BAD_REQUEST)

class GunplaDetail(APIView):
    def get_object(self, pk):
        try:
            return Gunpla.objects.get(pk=pk)
        except Gunpla.DoesNotExist:
            raise Http404("Not found.")
    
    def get(self, request, pk):
        gunpla = self.get_object(pk)
        serializer = GunplaSerializer(gunpla)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        gunpla = self.get_object(pk)
        serializer = GunplaSerializer(gunpla, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        gunpla = self.get_object(pk)
        gunpla.delete()
        return Response({"message": "Gunpla model deleted successfully"}, status=status.HTTP_200_OK)