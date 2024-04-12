from rest_framework import serializers
from .models import Note
from Documents.models import PDFDocument

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=('id','idDocumento','contenido','fecha_Creacion')
        read_only_fields=('id','idDocumento','fecha_Creacion')