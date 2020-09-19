from django.shortcuts import render,get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from .choices import bedroom_choices,price_choices,state_choices



def index(request):
  listing = Listing.objects.order_by('-list_date').filter(is_publish=True)
  
  #paginator
  paginator = Paginator(listing,6)
  page = request.GET.get('page')
  page_number = paginator.get_page(page)
  
  context = {'listings':page_number}
  return render(request,'listings/listings.html',context)

def listing(request,listing_id):
  listing = get_object_or_404(Listing,pk=listing_id)
  context = {
    'listing':listing
  }
  return render(request,'listings/listing.html',context)

# def my_newSearch(tag,request,queryset):
#   if tag in request.GET:
#     tags = request.GET[tag]
#     quaryset = quaryset.objects.filter(tags__iexact=tags)

def search(request):
       
   quaryset = Listing.objects.order_by('-list_date')
   
   #keywords
   if 'keywords' in request.GET:
     keywords = request.GET['keywords']
     if keywords:
       quaryset = quaryset.filter(description__icontains=keywords)
    
        
   #city
   if 'city' in request.GET:
     city = request.GET['city']
     if city:
       quaryset = quaryset.filter(city__iexact=city)

      
  #state
   if 'state' in request.GET:
     state = request.GET['state']
     if state:
       quaryset = quaryset.filter(state__iexact=state)
  #Bedroom
   if 'bedrooms' in request.GET:
     bedrooms_size = request.GET['bedrooms']
     if bedrooms_size:
       quaryset = quaryset.filter(bedrooms_size__lte=bedrooms_size)
  
    #Bedroom
   if 'price' in request.GET:
     price = request.GET['price']
     if price:
       quaryset = quaryset.filter(price__lte=price)
        
   context = {
    'state_choices':state_choices,
    'price_choices':price_choices,
    'bedroom_choices':bedroom_choices,
    'listings':quaryset,
    'values':request.GET
  }
   return render(request,'listings/search.html', context)
