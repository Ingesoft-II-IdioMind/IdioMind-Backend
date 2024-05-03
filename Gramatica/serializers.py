
from rest_framework import serializers


class GrammarPromptSerializer(serializers.Serializer):
    issue = serializers.CharField(max_length=120)
    idiom = serializers.CharField(max_length=50)