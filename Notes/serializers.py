from rest_framework import serializers
from .models import Note
from Documents.models import PDFDocument


class NoteSerializer(serializers.ModelSerializer):
    documento = serializers.PrimaryKeyRelatedField(
        queryset=PDFDocument.objects.all(),
    )

    class Meta:
        model = Note
        fields = ('id','user','documento', 'contenido', 'fecha_creacion', 'highlight_areas')
        read_only_fields = ('id','user','fecha_creacion')

    def create(self,validated_data):
        user=self.context['request'].user
        validated_data['user']=user
        return Note.objects.create(**validated_data)