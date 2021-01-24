from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def contactview(request):
    """ A view to return the contact page """
    name = ''
    email = ''
    message = ''

# Code from- http://www.learningaboutelectronics.com/Articles/How-to-create-a-contact-form-for-website-in-Django.php

# A view to return the contact form

    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("comment")

        message = name + " with the email, " + email + ", sent the following message:\n\n" + message;
        send_mail(message, '', [email])


        context = {'form': form}

        return render(request, 'contact/contact.html', context)

    else:
        context = {'form': form}
        return render(request, 'contact/contact.html', context)