from rest_framework import viewsets , permissions
from .models import PDFDocument
from .serializers import PDFDocumentSerializer

class PDFDocumentViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

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