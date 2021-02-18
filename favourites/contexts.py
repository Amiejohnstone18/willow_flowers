from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def favourites_contents(request):

    favourite_items = []
    favourites = request.session.get('favourites', [])

    for item_id in favourites:
        product = get_object_or_404(Product, pk=item_id)
        favourite_items.append({
            'item_id': item_id,
            'product': product,
        })

    context = {
        'favourite_items': favourite_items,
    }

    return context
