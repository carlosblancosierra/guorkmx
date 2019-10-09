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


def audit_page(request):
    questions_list = [
        [
            'How confident are you in your ability to design a conversion funnel that transforms cold visitors into customers?',
            'How confident are you in your ability to design a conversion funnel that transforms cold visitors into customers?',
        ],
        ['lorem ipsum2'],
        ['lorem ipsum3'],
        [
            'How confident are you in your ability to design a conversion funnel that transforms cold visitors into customers?',
            'How confident are you in your ability to design a conversion funnel that transforms cold visitors into customers?',
        ],
        ['lorem ipsum5'],
    ]

    current_page = questions_list[0]

    context = {
        'current_page': current_page,
        'range': range(10),
        'questions_list': questions_list,
    }

    return render(request, "audit_page.html", context)
