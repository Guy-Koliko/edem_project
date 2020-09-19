from django.shortcuts import render

from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import bedroom_choices,price_choices,state_choices

#this page is for the index

def index(request):
  listing = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
  context = {
    'listings':listing,
    'state_choices':state_choices,
    'price_choices':price_choices,
    'bedroom_choices':bedroom_choices
  }
  return render(request,'pages/index.html',context)

#this page is for the about us

def about(request):
  #get all realtors
  realtor = Realtor.objects.order_by('hire_date')
  is_mvp = Realtor.objects.all().filter(is_mvp=True)
  context = {
    'realtors':realtor,
    'is_mvp':is_mvp
  }
  return render(request,'pages/about.html',context)
