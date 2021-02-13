from django.shortcuts import render, redirect, get_object_or_404
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


def add_to_favourites(request, item_id):
    """ A view to add item to favourites """
    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', [])

    favourites.append(item_id)

    request.session['favourites'] = favourites
    return redirect(redirect_url)
