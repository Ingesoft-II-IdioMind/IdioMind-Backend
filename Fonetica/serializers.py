
from rest_framework import serializers


class ExamplesGramaticPromptSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=64)