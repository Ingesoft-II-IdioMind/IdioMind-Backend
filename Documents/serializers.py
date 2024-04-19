from rest_framework import serializers
from .models import PDFDocument
from .utils import subir_pdf
class PDFDocumentCreateSerializer(serializers.ModelSerializer):
    archivo_pdf = serializers.FileField(write_only=True)  # Campo para el archivo PDF

    class Meta:
        model = PDFDocument
        fields = ('id', 'user', 'titulo', 'autor', 'fecha_subida', 'ultima_vez_abierto', 'archivo_pdf','archivo_url')
        read_only_fields = ('id', 'user', 'fecha_subida', 'ultima_vez_abierto','archivo_url')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        # Extrae el archivo PDF de los datos validados
        archivo_pdf = validated_data.pop('archivo_pdf', None)
        # Llama a la función subir_pdf para subir el archivo PDF a Firebase Storage
        url_archivo = subir_pdf(archivo_pdf)
        # Agrega la URL del archivo en Firebase Storage a los datos validados
        validated_data['archivo_url'] = url_archivo

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

