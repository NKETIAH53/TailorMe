from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import UserProfile
from .serializers import UserProfileSerializer


class UserProfilesViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        instance = UserProfile.objects.get(id=pk)
        serializer = UserProfileSerializer(instance)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = UserProfileSerializer(data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"msg": "Profile created successfully"},
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        instance = get_object_or_404(UserProfile, pk)
        serializer = UserProfileSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Profile updated successfully"}, serializer.data)
