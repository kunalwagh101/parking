from django.test import TestCase
from django.core.management import call_command
from polls.models import ParkingSpace

class ParkingManagementTests(TestCase):
    
    def test_create_parking_spaces(self):
        """Test if the management command correctly creates parking spaces"""

        count = 10  
        call_command('dummy_data', count) 
        spaces = ParkingSpace.objects.all()

        self.assertEqual(spaces.count(), count) 

        for i, space in enumerate(spaces, start=1):
            self.assertEqual(space.number, f"P-{i}") 

        for space in spaces:
            self.assertIsInstance(space.parking_area, int)  
            self.assertGreaterEqual(space.parking_area, 1)  
            self.assertLessEqual(space.parking_area, 5)

        for space in spaces:
            self.assertIn(space.is_available, [True, False]) 

        print("\n✅ Test: Parking spaces created successfully!")
        print("📌 10 parking spaces were generated with valid numbers, zones, and availability statuses.")

    def test_parking_space_update(self):
        """Test if we can update parking space availability and vehicle type"""


        space = ParkingSpace.objects.create(
            number="P-99", 
            is_available=True, 
            vehicle="car", 
            parking_area=2  
        )

        print(f"\n🟡 Initially, parking space {space.number} is AVAILABLE in Zone {space.parking_area} for {space.vehicle}.")

      
        space.is_available = False
        space.vehicle = "two wheeler"
        space.parking_area = 5  
        space.save()

       
        updated_space = ParkingSpace.objects.get(number="P-99")

        self.assertFalse(updated_space.is_available)  
        self.assertEqual(updated_space.vehicle, "two wheeler")  
        self.assertEqual(updated_space.parking_area, 5)  

        print(f"✅ Parking space {updated_space.number} was successfully UPDATED:")
        print(f"   - Now OCCUPIED")
        print(f"   - Assigned to a {updated_space.vehicle}")
        print(f"   - Moved to Zone {updated_space.parking_area}")
