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


class TableAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableAPIList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
