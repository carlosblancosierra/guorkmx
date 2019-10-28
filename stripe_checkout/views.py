from django.shortcuts import render
from django.conf import settings
from billing.models import BillingProfile

STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY
STRIPE_PUB_KEY = settings.STRIPE_PUB_KEY
import stripe


# Create your views here.
def charge_view(request):
    if request.POST:
        card_token = request.POST.get('stripeToken', None)

        if card_token is not None:
            print('STRIPE CHARGE: Card token = ', card_token)

            stripe.api_key = STRIPE_SECRET_KEY

            email = 'carlosblancosierra@gmail.com'

            customer = stripe.Customer.create(
                email=email,
            )

            card = card = stripe.Customer.create_source(
                customer.id,
                source=card_token
            )

            print('STRIPE CHARGE: customer = ', customer)

            charge = stripe.Charge.create(
                customer=customer.id,
                amount=10001,
                currency="mxn",
                source=card.id,
                description="Test Charge",
            )

            print('STRIPE CHARGE: charge = ', charge)

    template_name = 'stripe/charge.html'
    context = {
        'pub_key': STRIPE_PUB_KEY,
    }

    return render(request, template_name, context)
