from django.shortcuts import (
    render, redirect, get_object_or_404, HttpResponse
)
from django.contrib.auth.decorators import login_required

from profiles.models import UserProfile
from products.models import Product


@login_required
def view_favourites(request):
    """ A view ro return the favourites"""
    if request.user.is_authenticated:
        template = 'favourites/favourites.html'
        return render(request, template)
    else:
        return redirect('.../accounts/login')


@login_required
def add_to_favourites(request, item_id):
    """ A item to favourites """
    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', [])

    favourites.append(item_id)

    request.session['favourites'] = favourites
    return redirect(redirect_url)


@login_required
def remove_from_favourites(request, item_id):
    """Remove the item from the favourites"""

    try:
        favourites = request.session.get('favourites', [])
        favourites.pop(item_id)

        request.session['favourites'] = favourites
        return redirect('favourites')

    except Exception as e:
        return HttpResponse(status=500)
