import json
from django.shortcuts import render


def home_page(request):
    context = {
    }

    return render(request, "home.html", context)


def inbound_page(request):
    context = {
    }

    return render(request, "inbound_page.html", context)
