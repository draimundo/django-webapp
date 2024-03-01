from django.shortcuts import redirect, render, get_object_or_404
from django.core.mail import send_mail
from listings.models import Band, Listing
from listings.forms import BandForm, ContactUsForm, ListingForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})

def band_detail(request, band_id):
    band = get_object_or_404(Band, pk=band_id)
    return render(request, "listings/band_detail.html", {"band": band})

def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band_id=band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})

def about(request):
    return render(request, "listings/about.html")

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})

def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})

def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing_id=listing.id)
    else:
        form = ListingForm()
    return render(request, "listings/listing_create.html", {"form": form})

def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})

def email_sent(request):
    return render(request, "listings/email_sent.html")