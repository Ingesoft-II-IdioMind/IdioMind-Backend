from rest_framework import viewsets, permissions
from .models import Note
from Documents.models import PDFDocument
from .serializers import NoteSerializer
from django.http import JsonResponse

class NoteViewset(viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class=NoteSerializer

    def get_permissions(self):
        if self.action=='create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]