from django.http import HttpResponse


class StripeWH_Handler:
    """ Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Generic/ Unknown/ Unexpected webhook event
        """
        return HttpResponse(
        content=f'unhandled webhook recieved: {event["type"]}',
        status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Successful payment from Stripe
        """
        return HttpResponse(
        content=f'webhook recieved: {event["type"]}',
        status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Failed_intent_payment from Stripe
        """
        return HttpResponse(
        content=f'webhook recieved: {event["type"]}',
        status=200)