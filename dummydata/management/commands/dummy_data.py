from django.core.management.base import BaseCommand
from polls.models import ParkingSpace
import random


VEHICLE = [
        ('car', 'Car'),
        ('two wheeler', 'Two wheeler'),
        ('cycle', 'Cycle'),

    ]
class Command(BaseCommand):
    help = "Adds dummy parking spaces to the database"

    def random_area(self):
        area  =  random.randint(1,5)
        return area

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help="Number of parking spaces to create")

    def handle(self, *args, **kwargs):
        ParkingSpace.objects.all().delete()
        count = kwargs['count']
        created_spaces = []

        for i in range(1, count + 1):
            space, created = ParkingSpace.objects.get_or_create(number=f"P-{i}" ,
                defaults= {"is_available" : random.choice([True, False]),
                           "parking_area"  : self.random_area() ,
                           "vehicle" :random.choice([choice[0] for choice in VEHICLE]),
                           })
            
            created_spaces.append(F" {space.number} {space.is_available} {space.vehicle}")

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully added {len(created_spaces)} parking spaces!"))
