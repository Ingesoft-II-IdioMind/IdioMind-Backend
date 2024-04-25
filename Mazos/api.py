from rest_framework import viewsets, permissions
from .models import Deck
from .serializers import DeckSerializer

class DeckViewset(viewsets.ModelViewSet):
    queryset=Deck.objects.all()
    serializer_class=DeckSerializer

    
    def get_permissions(self):
        if self.action=='create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]
        
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Deck.objects.filter(user=user)
        else:
            return Deck.objects.none()
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
