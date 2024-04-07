from rest_framework import serializers
from .models import Deck

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model=Deck
        fields=('id','user','nombre','fecha_Creacion','ultima_Practica')
        read_only_fields=('id','user','fecha_Creacion')
    def create(self,validated_data):
        user=self.context['request'].user
        validated_data['user']=user
        return Deck.objects.create(**validated_data)