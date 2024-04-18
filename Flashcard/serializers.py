from rest_framework import serializers
from .models import Flashcard
from Mazos.models import Deck

class FlashcardSerializer(serializers.ModelSerializer):
    mazo = serializers.PrimaryKeyRelatedField(
        queryset=Deck.objects.all(),
    )
    nombre_mazo = serializers.SerializerMethodField()
    class Meta:
        model=Flashcard
        fields=('id','user','mazo','nombre_mazo','fecha_Creacion','ultima_Revision','proxima_Revision','frente','reverso')
        read_only_fields=('id','user','fecha_Creacion')
        
    def get_nombre_mazo(self, obj):
        return obj.mazo.nombre if obj.mazo else None
    
    def create(self,validated_data):
        user=self.context['request'].user
        validated_data['user']=user
        return Flashcard.objects.create(**validated_data)