from rest_framework import viewsets, permissions
from .models import Flashcard
from .serializers import FlashcardSerializer

class FlashcardViewset(viewsets.ModelViewSet):
    queryset=Flashcard.objects.all()
    serializer_class=FlashcardSerializer

    def get_permissions(self):
        if self.action=='create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]
        
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Flashcard.objects.filter(user=user)
        else:
            return Flashcard.objects.none()
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)