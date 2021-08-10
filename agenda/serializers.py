from rest_framework import serializers
from .models import Agenda

class AgendaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = [
            'id',
            'hospede',
            'checkin',
            'checkout',
            'limpeza',
        ]

class AgendaDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = [
            'id',
            'hospede',
            'checkin',
            'checkout',
            'limpeza',

        ]
