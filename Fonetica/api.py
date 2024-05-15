from .utils import speakingExamples,evaluate_pronunciation
from .serializers import ExamplesGramaticPromptSerializer,FeedbackPromptSerializer
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
        

class FeedbackViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer =FeedbackPromptSerializer(data=request.data)
        if serializer.is_valid():
            audio_file_base64 = serializer.validated_data['audio_file_base64']
            target_sentence = serializer.validated_data['target_sentence']
            fonetic_feedback = evaluate_pronunciation(audio_file_base64,target_sentence)
            return Response(fonetic_feedback,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

