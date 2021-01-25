from django.shortcuts import render, redirect


def view_favourites(request):
    """ A view to return the favourites """
    
    return render(request, 'favourites/favourites.html')


def add_to_favourites(request, item_id):
    """ Add item to favourites """

    redirect_url = request.POST.get('redirect')
    favourites = request.session.get('favourites', {})

    request.session['favourites'] = favourites
    print(request.session['favourites'])
    return redirect(redirect_url)
