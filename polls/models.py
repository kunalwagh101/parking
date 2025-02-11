from django.db import models

class ParkingSpace(models.Model):
    VEHICLE = [
        ('car', 'Car'),
        ('two wheeler', 'Two wheeler'),
        ('cycle', 'Cycle'),

    ]
    


    number = models.CharField(max_length=10, unique=True)
    is_available = models.BooleanField()
    parking_area =  models.IntegerField(null=True, blank=True)
    vehicle =  models.CharField(max_length=50 , choices= VEHICLE,blank=True  ,default="car")
    created_time = models.DateField(auto_now_add=True)  
    updated_time = models.DateField(auto_now=True)  
    
    def __str__(self):
        return f"Space {self.number} - {'Available' if self.is_available else 'Occupied'}"

class Booking(models.Model):
    parking_space = models.OneToOneField(ParkingSpace, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=15, unique=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Booking {self.vehicle_number} at Space {self.parking_space.number}"
