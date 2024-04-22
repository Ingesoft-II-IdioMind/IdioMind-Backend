from rest_framework import serializers
from .models import Note
from Documents.models import PDFDocument


class NoteSerializer(serializers.ModelSerializer):
    documento = serializers.PrimaryKeyRelatedField(
        queryset=PDFDocument.objects.all(),
    )
    titulo = serializers.SerializerMethodField()
    class Meta:
        model = Note
        fields = ('id','user','documento','titulo','contenido', 'fecha_creacion', 'highlight_areas')
        read_only_fields = ('id','user','fecha_creacion')

    def get_titulo(self,obj):
        return obj.documento.titulo if obj.documento else None

    def create(self,validated_data):
        user=self.context['request'].user
        validated_data['user']=user
        return Note.objects.create(**validated_data)