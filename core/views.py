from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'core/home.html')

def menu(req):
    return render(req, 'core/menu.html')

def tracking(req):
    return render(req, 'core/tracking.html')

def reservation(req):
    return render(req, 'core/reservation.html')

def contact(req):
    return render(req, 'core/contact.html')