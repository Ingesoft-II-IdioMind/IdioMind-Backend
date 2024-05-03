from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        # Usar el serializer PostSerializer solo para solicitudes de escritura si el usuario es un superusuario
        if self.request.method in ['POST', 'PUT', 'PATCH'] and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear o actualizar posts.")
        return PostSerializer
    


class PostViewSetLast10(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_serializer_class(self):
        # Usar el serializer PostSerializer solo para solicitudes de escritura si el usuario es un superusuario
        if self.request.method in ['POST', 'PUT', 'PATCH'] and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear o actualizar posts.")
        return PostSerializer
    
    def get_queryset(self):
        return Post.objects.order_by('-Fecha_publicacion')[:10]

