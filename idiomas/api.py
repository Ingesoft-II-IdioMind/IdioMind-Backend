from rest_framework import viewsets , permissions
from .models import Idiom
from .serializers import IdiomSerializer

class IdiomCreateViewSet(viewsets.ModelViewSet):
    queryset = Idiom.objects.all()
    serializer_class = IdiomSerializer