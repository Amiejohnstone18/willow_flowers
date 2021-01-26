from django.shortcuts import render, redirect


def view_favourites(request):
    """ A view to return the favourites """

    return render(request, 'favourites/favourites.html')


def add_to_favourites(request, item_id):
    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', [])

    favourites.append(item_id)

    request.session['favourites'] = favourites
    return redirect(redirect_url)
