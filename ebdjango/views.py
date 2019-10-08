import json
from django.shortcuts import render
from .forms import ContactForm


def home_page(request):
    context = {
    }

    return render(request, "home.html", context)


def inbound_page(request):

    context = {
    }

    return render(request, "inbound_page.html", context)


def contact_page(request):

    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    context = {
        "form": form
    }

    return render(request, "contact_page.html", context)
