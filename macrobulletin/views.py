from rest_framework import generics
from .models import *
from .serializers import *


class TopicAPIList(generics.ListCreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class TopicAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class EconomicIndexAPIList(generics.ListCreateAPIView):
    queryset = EconomicIndex.objects.all()
    serializer_class = EconomicIndexSerializer


class EconomicIndexAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EconomicIndex.objects.all()
    serializer_class = EconomicIndexSerializer
