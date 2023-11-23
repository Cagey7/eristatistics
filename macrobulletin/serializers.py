from rest_framework import serializers
from .models import *


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class EconomicIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicIndex
        fields = "__all__"