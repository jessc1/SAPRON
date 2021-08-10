from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import AgendaListSerializer, AgendaDetailSerializer
from .models import Agenda

class AgendaListAPIView(generics.ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    queryset = Agenda.objects.all()
    serializer_class = AgendaListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['hospede', 'id']

class AgendaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaCreateAPIView(generics.CreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaUpdateAPIView(generics.RetrieveUpdateAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaDeleteAPIView(generics.DestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,) 
    lookup_field = "id"
    queryset = Agenda.objects.all()
    


