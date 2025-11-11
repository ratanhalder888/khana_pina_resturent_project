from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation

# Create your views here.
def home(req):
    dishes = [
        {
            'name' : 'Paneer Butter Masala',
            'description' : 'Creamy and rich, with a delightful blend of spices, perfect with naan or rice.',
            'image': 'core/images/paneer_butter_masala.png',
        },
        {
            'name' : 'Sushi',
            'description' : 'Sushi is a Japanese dish featuring seasoned rice, often combined with seafood (raw or cooked), vegetables, and sometimes wrapped in seaweed.',
            'image' : 'core/images/sushi.png',
        },
        {
            'name' : 'Butter Paneer',
            'description' : 'Creamy North Indian curry featuring soft paneer cheese in a tomato-based sauce with butter and spices.',
            'image' : 'core/images/paneer.png',
        },
        {
            'name' : 'Traditional Brazilian Food',
            'description' : 'Traditional Brazilian food is delicious, colorful, diverse, and exciting.',
            'image' : 'core/images/traditional_brazilian_food.png',
        },
        {
            'name' : 'Kacchi Biryani',
            'description' : 'Biryani is a mixed rice dish that originated in South Asia, featuring fragrant rice (typically basmati) cooked with meat (chicken, goat, lamb, beef, or fish) or vegetables, and a blend of aromatic spices.',
            'image' : 'core/images/biryani.png',
        },
        # Can add more dishes here
    ]

    return render(req, 'core/home.html', {'dishes': dishes})

def menu(req):
    return render(req, 'core/menu.html')

def tracking(req):
    return render(req, 'core/tracking.html')

def reservation(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')
        guest_number = request.POST.get('guest_number')
        mobile = request.POST.get('mobile')
        created_at = request.POST.get('created_at')

        # Create a new Reservation object and save it to the database
        Reservation.objects.create(
            name = name,
            date = date,
            time = time,
            guest_number = guest_number,
            mobile = mobile,
            created_at = created_at,
        )

        # Add a success message (optional)
        messages.success(request, 'Your table has been reserved successfully! ' \
                                    'We look forward to seeing you.')
        
        # Redirect to avoid form resubmission issues
        return redirect('reservation')
    return render(request, 'core/reservation.html')

def contact(req):
    return render(req, 'core/contact.html')