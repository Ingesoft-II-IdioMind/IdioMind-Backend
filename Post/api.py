from .models import Post
from .serializers import PostSerializer,PostUpdateSerializer
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()

    def get_serializer_class(self):
        # Usar el serializer PostSerializer solo para solicitudes de escritura si el usuario es un superusuario
        if self.request.method == 'POST' and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear, actualizar o eliminar posts.")
        elif self.request.method in ['PUT', 'PATCH', 'DELETE'] and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear, actualizar o eliminar posts.")
        elif self.request.method == 'POST':
            return PostSerializer
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return PostUpdateSerializer
        else:
            return PostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden eliminar posts.")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostViewSetLast10(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_serializer_class(self):
        # Usar el serializer PostSerializer solo para solicitudes de escritura si el usuario es un superusuario
        if self.request.method in ['POST', 'PUT', 'PATCH','DELETE'] and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear o actualizar posts.")
        return PostSerializer
    
    def get_queryset(self):
        return Post.objects.order_by('-Fecha_publicacion')[:10]
