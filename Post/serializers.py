from . models import Post
from rest_framework import serializers
from .utils import subir_image


class PostSerializer(serializers.ModelSerializer):
    image_file = serializers.FileField(write_only=True)
    class Meta:
        model = Post
        fields = ('id', 'Titulo', 'Fecha_publicacion','Autor','Imagen','Contenido','image_file')
        read_only_fields = ('id','Fecha_publicacion','Imagen')

    def create(self, validated_data):
            if self.context['request'].user.is_superuser:
                imagen_file = validated_data.pop('image_file', None)
                if imagen_file:
                     Image = subir_image(imagen_file)
                     validated_data['Imagen'] = Image
                return super().create(validated_data)
            else:
                raise serializers.ValidationError("Solo los superusuarios pueden crear posts.")

    def update(self, instance, validated_data):
        if self.context['request'].user.is_superuser:
            return super().update(instance, validated_data)
        else:
            raise serializers.ValidationError("Solo los superusuarios pueden actualizar posts.")
        
class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'Titulo', 'Fecha_publicacion','Autor','Imagen','Contenido')
        read_only_fields = ('id','Fecha_publicacion','Imagen')


    def update(self, instance, validated_data):
        if self.context['request'].user.is_superuser:
            return super().update(instance, validated_data)
        else:
            raise serializers.ValidationError("Solo los superusuarios pueden actualizar posts.")
