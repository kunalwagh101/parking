from django.shortcuts import render, redirect,get_object_or_404
from .models import ParkingSpace, Booking
from .forms import BookingForm

def parking_list(request):
    spaces = ParkingSpace.objects.all()
    return render(request, 'parking_list.html', {'spaces': spaces})

def book_parking(request, space_id):
    space = ParkingSpace.objects.get(id=space_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.parking_space = space
            booking.save()
            space.is_available = False
            space.save()
            return redirect('parking_list')
    else:
        form = BookingForm()
    return render(request, 'book_parking.html', {'form': form, 'space': space})

def release_parking(request, space_id):
  
    space = get_object_or_404(ParkingSpace, id=space_id)
    Booking.objects.filter(parking_space=space).delete()
    space.is_available = True
    space.save()


    return redirect('parking_list')
