from rest_framework import serializers
from .models import Flashcard

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flashcard
        fields=('id','user','mazo','fecha_Creacion','contenido','ultima_Revision','proxima_Revision','comentario')
        read_only_fields=('id','user','fecha_Creacion')
    def create(self,validated_data):
        user=self.context['request'].user
        validated_data['user']=user
        return Flashcard.objects.create(**validated_data)