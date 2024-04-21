from rest_framework import viewsets , permissions
from .models import PDFDocument
from .serializers import PDFDocumentCreateSerializer,TranslatePromptSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import translate_word


class PDFDocumentCreateViewSet(viewsets.ModelViewSet):
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentCreateSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.AllowAny()]
        
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.instance.save()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PDFDocument.objects.filter(user=user)
        else:
            return PDFDocument.objects.none()


class TranslateWordViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = TranslatePromptSerializer(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data['word']
            language = serializer.validated_data['language']
            sentence = serializer.validated_data.get('sentence')
            translation_data = translate_word(word, language, sentence)
            return Response(translation_data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)