
from rest_framework import serializers


class ExamplesGramaticPromptSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=64)


    
class FeedbackPromptSerializer(serializers.Serializer):
    audio_file = serializers.FileField()
    target_sentence  = serializers.CharField(max_length=1024)