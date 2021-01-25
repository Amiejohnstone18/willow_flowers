from django.conf import settings


def favourites_contents(request):

    favourites_items = []

    context = {
        'favourites_items': favourites_items,
    }

    return context
