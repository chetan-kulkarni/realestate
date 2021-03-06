from django.shortcuts import get_object_or_404,render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices

def index(request):
    listing = Listing.objects.order_by('-list_date').filter(is_published='True')

    paginator = Paginator(listing, 3)
    page = request.GET.get('page')
    paged_listing = paginator.get_page(page)

    context = {
        'listing': paged_listing
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        print(state)
        if state == 'Rent':
            queryset_list = queryset_list.filter(for_rent_only=True)
        else:
            queryset_list = queryset_list.filter(for_rent_only=False)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'listing': queryset_list,
        'values':request.GET

    }

    return render(request, 'listings/search.html', context)
