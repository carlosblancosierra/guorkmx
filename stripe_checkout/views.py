from django.shortcuts import render
import stripe

STRIPE_PUB_KEY = 'pk_test_UTSbSt5W4QpVCHpCxa5K7nIw00FbA6R0K2'
STRIPE_SECRET_KEY = 'sk_test_KJ6abjyErxo9HcttWkkdIEGW00QGzanzow'


# Create your views here.
def charge_view(request):
    if request.POST:
        card_token = request.POST.get('stripeToken', None)

        if card_token is not None:
            print('STRIPE CHARGE: Card token = ', card_token)

            stripe.api_key = STRIPE_SECRET_KEY

            charge = stripe.Charge.create(
                amount=10001,
                currency="mxn",
                source=card_token,
                description="Test Charge",
            )

            print('STRIPE CHARGE: charge = ', charge)

    template_name = 'stripe/charge.html'
    context = {
    }

    return render(request, template_name, context)
