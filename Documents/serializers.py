from rest_framework import serializers
from .models import PDFDocument
from .utils import subir_pdf
class PDFDocumentCreateSerializer(serializers.ModelSerializer):
    archivo_pdf = serializers.FileField(write_only=True)  # Campo para el archivo PDF

    class Meta:
        model = PDFDocument
        fields = ('id', 'user', 'titulo', 'autor', 'fecha_subida', 'ultima_vez_abierto', 'archivo_pdf','archivo_url','portada_url')
        read_only_fields = ('id', 'user', 'fecha_subida', 'ultima_vez_abierto','archivo_url','portada_url')

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        # Extrae el archivo PDF de los datos validados
        archivo_pdf = validated_data.pop('archivo_pdf', None)
        # Llama a la función subir_pdf para subir el archivo PDF a Firebase Storage
        if archivo_pdf:
            url_archivo, url_portada = subir_pdf(archivo_pdf,user.email)
            if url_archivo and url_portada:
                # Agrega la URL del archivo en Firebase Storage a los datos validados
                validated_data['archivo_url'] = url_archivo
                validated_data['portada_url'] = url_portada
                return PDFDocument.objects.create(**validated_data)
            else:
                raise serializers.ValidationError("Error al subir el archivo PDF a Firebase Storage")
        else:
            raise serializers.ValidationError("Archivo PDF no proporcionado")
    


class TranslatePromptSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=30)
    language = serializers.CharField(max_length=30)
    sentence = serializers.CharField(required=False, allow_blank=True,max_length=255)

