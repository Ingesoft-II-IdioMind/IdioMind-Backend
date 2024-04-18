from rest_framework import serializers
from .models import PDFDocument

class PDFDocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ('id', 'user', 'titulo','autor','fecha_subida','ultima_vez_abierto','base64')
        read_only_fields = ('id', 'user','fecha_subida','ultima_vez_abierto')

    def create(self,validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return PDFDocument.objects.create(**validated_data)
    

class PDFDocumentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = ('id', 'user', 'titulo','autor','fecha_subida','ultima_vez_abierto')
        read_only_fields = ('id', 'user', 'titulo','autor','fecha_subida','ultima_vez_abierto')
    def create(self,validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return PDFDocument.objects.create(**validated_data)
    


class TranslatePromptSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=30)
    language = serializers.CharField(max_length=30)
    sentence = serializers.CharField(required=False, allow_blank=True,max_length=255)

