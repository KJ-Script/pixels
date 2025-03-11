from django.shortcuts import render
from rest_framework import generics
from .models import User, Image
from .Serializer import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.views import APIView
from .serializers import ImageSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class ImageUploadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            image_file = request.FILES.get('image')
            if not image_file:
                return Response({'error': 'No image provided'}, status=status.HTTP_400_BAD_REQUEST)

            image = Image.objects.create(
                user=request.user,
                file=image_file
            )

            serializer = ImageSerializer(image, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PublicImageListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)


class UserImageListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        images = Image.objects.filter(user=request.user)
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)


class ImageListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)


