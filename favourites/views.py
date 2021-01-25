from django.shortcuts import render


def view_favourites(request):
    """ A view to return the favourites """
    return render(request, 'favourites/favourites.html')
