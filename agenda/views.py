from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import AgendaListSerializer, AgendaDetailSerializer
from .models import Agenda



class AgendaListAPIView(generics.ListAPIView):
    """
    Retorna uma lista de todos os hóspedes adicionados
    na API.
    A busca por algum hóspede pode ser feita pelo nome
    ou id.
    O checkin pode ser ordenado de modo ascendente ou
    decrescente.
    """     
    queryset = Agenda.objects.all()
    serializer_class = AgendaListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['checkin']
     
    search_fields = ['hospede', 'id']

class AgendaRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retorna os dados sobre um hóspede.
    """
    
    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaCreateAPIView(generics.CreateAPIView):
    """
    Cria um novo hóspede na API.
    """    
      
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaUpdateAPIView(generics.RetrieveUpdateAPIView):
    """
    Atualiza os dados de um hóspede na API.
    """
        
    lookup_field = "id"
    queryset = Agenda.objects.all()
    serializer_class = AgendaDetailSerializer

class AgendaDeleteAPIView(generics.DestroyAPIView):
    """
    Deleta um hóspede da API.
    """
      
    lookup_field = "id"
    queryset = Agenda.objects.all()
    


