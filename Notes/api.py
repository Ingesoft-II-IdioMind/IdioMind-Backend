from rest_framework import viewsets, permissions
from .models import Note
from Documents.models import PDFDocument
from .serializers import NoteSerializer
from django.http import JsonResponse

class NoteViewset(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]
        
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(user=user)
        else:
            return Note.objects.none()
        

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return JsonResponse(serializer.data, status=201, headers=headers)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user,highlight_areas=self.request.data.get('highlight_areas', []))

class DocumentListViewset(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    def get_queryset(self):
        documento_id = self.kwargs.get('documento_id')
        if documento_id:
            return Note.objects.filter(documento_id=documento_id, documento__user=self.request.user)
        else:
            return Note.objects.none()