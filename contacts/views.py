from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contacts
from django.core.mail import send_mail

# Create your views here.
def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    listing = request.POST['listing']
    realtor_email = request.POST['realtor_email']
    
    
    #check to see if listing exit
    
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, "You have already make and enquire for this listing")
        return redirect('/accounts/dashboard')
    
    contact = Contacts(listing=listing, listing_id=listing_id, name=name,email=email,phone=phone, message=message, user_id=user_id)
    
    
    contact.save()
    
    #send mail
    send_mail(
      'Property listing',
      'There has been a listing enquary '+ listing +'. Sign in to your admin pannel and check',
      'ubntwin5050@gmail.com',
      [realtor_email,'edemrobin@gmail.com'],fail_silently=False
    )
    messages.success(request, "Your request has been submitted, a realtor will contact you shortly")
    
    return redirect('/listings/'+listing_id)
    
