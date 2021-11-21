from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from rest_framework.settings import import_from_string
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'