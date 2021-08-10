from django.db import models

class Agenda(models.Model):
    hospede = models.CharField(max_length=200, blank=False)
    checkin =  models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(auto_now= False, null=True, blank=True)
    limpeza =  models.DateTimeField(auto_now =False)

    def __str__(self):
        return self.hospede
    
