from django.shortcuts import render
from .models import Listing
from django.core.paginator import Paginator

def index(request):
  listing = Listing.objects.order_by('-list_date').filter(is_publish=True)
  
  #paginator
  paginator = Paginator(listing,6)
  page = request.GET.get('page')
  page_number = paginator.get_page(page)
  
  context = {'listings':page_number}
  return render(request,'listings/listings.html',context)

def listing(request,listing_id):
  return render(request,'listings/listing.html')

def search(request):
  return render(request,'listings/search.html')
