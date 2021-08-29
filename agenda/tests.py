import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Agenda
from .serializers import AgendaListSerializer, AgendaDetailSerializer
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Agenda

class AgendaTests(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='ani',
            email='test@email.com',
            password='secret'
        )
        self.agenda = Agenda.objects.create(
            hospede='Obi wan',
            checkout ='2021-08-20',
            limpeza= '2021-08-21',
                  
        )
    

    def test_post_agenda(self):
        self.assertEqual(f'{self.agenda.hospede}', 'Obi wan')
        self.assertEqual(f'{self.agenda.checkout}', '2021-08-20')
        self.assertEqual(f'{self.agenda.limpeza}', '2021-08-21')


    def test_agenda_list_view(self):
        response = self.client.get(reverse('hospede_list'))
        self.assertEqual(response.status_code, 200)
        


    def test_agenda_create_view(self):
        response =self.client.post(reverse('agenda_create'), {
            'hospede':'Obi wan',
            'checkout' :'2021-08-20',
            'limpeza': '2021-08-21',
            
        })
        
       

        
    def test_agenda_detail_view(self):
        response= self.client.get('/agenda/1/')
        
        

    def test_agenda_update_view(self): 
        response = self.client.post(reverse('agenda_update', args='1'), {
            'hospede':'Obi wan',
            'checkout' :'2021-08-20',
            'limpeza': '2021-08-21',            
            
        })
       

    def test_agenda_delete_view(self): 
        response = self.client.post(
            reverse('agenda_delete', args='1'))

                

