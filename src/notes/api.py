from rest_framework import viewsets, permissions

from .models import Category, Note
from .serializers import NotesSerializer, CategoriesSerializer


class NotesAPIViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NotesSerializer


class CategoriesAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriesSerializer
