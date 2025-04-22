from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.


class Contact(models.Model):
    
    name = models.CharField(max_length=500)
    email = models.EmailField()
    reservation_datetime = models.DateTimeField()
    service = models.CharField(max_length=100, choices = [
        ('option1', 'Haircuts & Styling'),
        ('option2', 'Hair Treatment & Repair'),
        ('option3', 'Spa & Relaxation Therapies'),
        ('option4', 'Nails & Manicure'),
        ('option5', 'Pedicure & Foot Spa'),
    ])


    def __str__(self):
        return f"{self.name} - {self.service} at {self.reservation_datetime}"
    