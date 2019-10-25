from django.urls import path

from .views import (
    charge_view
)

app_name = 'checkout'

urlpatterns = [

    path('charge', charge_view),
]
