from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import UserProfile
from products.models import Product


def view_favourites(request):
    """ A view to return the favourites """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        favourites.user_profile = profile
        favourites.objects.filter()
        favourites = get_object_or_404(UserProfile, user=request.user)
    else:
        return redirect('login.html')

    template = 'favourites.html'
    context = {
        'favourites': favourites,
    }

    return render(request, template, context)


def add_to_favourites(request, item_id):
    """ A view to add item to favourites """
    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', [])

    favourites.append(item_id)

    request.session['favourites'] = favourites
    return redirect(redirect_url)
