from .models import Post
from .serializers import PostSerializer,PostUpdateSerializer
from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer  # Usar PostSerializer como clase de serializador predeterminada

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return PostUpdateSerializer
        return self.serializer_class  # Devolver la clase de serializador predeterminada para otros métodos HTTP

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden eliminar posts.")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return []
        return super().get_permissions()


class PostViewSetLast10(viewsets.ModelViewSet):
    serializer_class = PostSerializer

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE'] and not self.request.user.is_superuser:
            raise PermissionDenied("Solo los superusuarios pueden crear o actualizar posts.")
        return self.serializer_class

    def get_queryset(self):
        return Post.objects.order_by('-Fecha_publicacion')[:10]

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            return []
        return super().get_permissions()