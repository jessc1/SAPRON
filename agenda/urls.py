from django.urls import path
from . import views

urlpatterns = [
    path('agenda', views.AgendaListAPIView.as_view(), name="hospede_list"),
    path('agenda/<int:id>/', views.AgendaRetrieveAPIView.as_view(), name='agenda_hospede_detail'),
    path('agenda/create', views.AgendaCreateAPIView.as_view(), name='agenda_create'),
    path('agenda/update/<int:id>/', views.AgendaUpdateAPIView.as_view(), name='agenda_update'),
    path('agenda/delete/<int:id>/', views.AgendaDeleteAPIView.as_view(), name='agenda_delete'),
     

    ]
