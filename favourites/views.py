from django.shortcuts import render

# Create your views here.


def favourites(request):
    """ A view to return the user favourites """

    return render(request, 'favourites/favourites.html')
