from .utils import speakingExamples
from .serializers import ExamplesGramaticPromptSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response 

class  ExamplesViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = ExamplesGramaticPromptSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data['content']
            fonetic_examples= speakingExamples(content)
            return Response(fonetic_examples,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
