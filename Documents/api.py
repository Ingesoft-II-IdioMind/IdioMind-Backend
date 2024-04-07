from rest_framework import viewsets , permissions
from .models import PDFDocument
from .serializers import PDFDocumentCreateSerializer,PDFDocumentListSerializer

class PDFDocumentListViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentListSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Solo permitir la creación de PDFs a usuarios autenticados
            return [permissions.IsAuthenticated()]
        else:
            # Permitir todas las demás operaciones a cualquier usuario
            return [permissions.AllowAny()]
    

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PDFDocument.objects.filter(user=user)
        else:
            return PDFDocument.objects.none()
        
class PDFDocumentCreateViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            # Solo permitir la creación de PDFs a usuarios autenticados
            return [permissions.IsAuthenticated()]
        else:
            # Permitir todas las demás operaciones a cualquier usuario
            return [permissions.AllowAny()]
        
        
    def perform_create(self, serializer):
        # Asignar automáticamente el usuario autenticado al crear el PDF
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PDFDocument.objects.filter(user=user)
        else:
            return PDFDocument.objects.none()