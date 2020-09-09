from django.shortcuts import render

from django.http import HttpResponse
from listings.models import Listing

def index(request):
  listing = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
  context = {
    'listings':listing
  }
  return render(request,'pages/index.html',context)


def about(request):
  return render(request,'pages/about.html')