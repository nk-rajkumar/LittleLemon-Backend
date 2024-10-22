from django.db import models
from django.utils import timezone  # Import timezone

class Booking(models.Model):
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)
    booking_date = models.DateField(default=timezone.now)  # Add default value
    booking_time = models.TimeField(null=True)  # Assuming you want this field to be nullable

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 

   def __str__(self):
      return self.name