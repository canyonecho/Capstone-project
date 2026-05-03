from django.db import models
from django.utils import timezone

class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(default=6)
    BookingDate = models.DateField(default=timezone.now())

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(default=5)
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
