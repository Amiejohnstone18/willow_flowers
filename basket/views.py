from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_basket(request):
    """ A view to return the shopping basket """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add items to basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """ Change items in the basket """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
    else:
        del basket[item_id]

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
