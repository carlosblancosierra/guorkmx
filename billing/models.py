from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
# from django.core.urlresolvers import reverse

User = settings.AUTH_USER_MODEL

# abc@teamcfe.com -->> 1000000 billing profiles
# user abc@teamcfe.com -- 1 billing profile

# import stripe
#
# stripe.api_key = settings.


class BillingProfileManager(models.Manager):
    def new_or_get(self, request):
        user = request.user
        created = False
        obj = None
        if user.is_authenticated():
            'logged in user checkout; remember payment stuff'
            obj, created = self.model.objects.get_or_create(
                user=user, email=user.email)
        else:
            pass
        return obj, created


# Create your models here.
class BillingProfile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=120, null=True, blank=True)

    objects = BillingProfileManager()

    def __str__(self):
        return self.email

    # def charge(self, order_obj, card=None):
    #     return Charge.objects.do(self, order_obj, card)

    # def get_cards(self):
    #     return self.card_set.all()
    #
    # def get_payment_method_url(self):
    #     return reverse('billing-payment-method')
    #
    # @property
    # def has_card(self):  # instance.has_card
    #     card_qs = self.get_cards()
    #     return card_qs.exists()  # True or False
    #
    # @property
    # def default_card(self):
    #     default_cards = self.get_cards().filter(active=True, default=True)
    #     if default_cards.exists():
    #         return default_cards.first()
    #     return None
    #
    # def set_cards_inactive(self):
    #     cards_qs = self.get_cards()
    #     cards_qs.update(active=False)
    #     return cards_qs.filter(active=True).count()
