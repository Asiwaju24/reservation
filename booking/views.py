from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import Contact
# Create your views here.

def index(request):
    
    if request.method == "POST":
        form = ContactForm(request.POST) 
        if form.is_valid():
            print('Form Is Valid')
            service = form.cleaned_data['service']
            reservation_datetime = form.cleaned_data['reservation_datetime']
            if Contact.objects.filter(service=service, reservation_datetime=reservation_datetime).exists():
                messages.error(request, "This service is already booked for the selected time. Please choose another slot.")
            else:
                form.save()
                print('booking Saved')        
        else:
            form.save()
            print('Form saved')
            messages.success(request, "Your Booking Has Been Confirmed")
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, "contact.html", {'form': form})
        