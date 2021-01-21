from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Your basket is empty")
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IC2RqE4pW1z533lXcF0guZWxdS41GkI8JyyyObnaZsmKvF7K4yWXi3bjmaNEKn6HPrh1mnuu2YywaJE66yRIQ1G00s7iBos9q',
    }

    return render(request, template, context)