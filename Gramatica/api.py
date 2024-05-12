from .utils import grammar_phrase
from .serializers import GrammarPromptSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response 

class GrammarViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer =  GrammarPromptSerializer(data=request.data)
        if serializer.is_valid():
            issue = serializer.validated_data['issue']
            idiom = serializer.validated_data['idiom']
            grammar_exercise = grammar_phrase(issue,idiom)
            return Response(grammar_exercise,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
