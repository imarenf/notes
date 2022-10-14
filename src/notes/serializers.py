from rest_framework import serializers
from .models import Category, Note


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description')
