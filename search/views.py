from django.shortcuts import render

# Create your views here.


def search(request):
    """ A view to return the search page """

    return render(request, 'search/search.html')
