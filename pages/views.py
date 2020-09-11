from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor

#this page is for the index

def index(request):
  listing = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
  context = {
    'listings':listing
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

#this page is about listing
def listing(request,listing_id):
  listing = get_object_or_404(Listing,pk=listing_id)
  context = {
    'listing':listing
  }
  return render(request,'listings/listing.html',context)