import json
from django.shortcuts import render
import json
from ebdjango.settings import GOOGLE_RECAPTCHA_SECRET_KEY, GOOGLE_RECAPTCHA_PUBLIC_KEY
from .forms import ContactForm


def home_page(request):
    print(request.user)
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

    if request.POST:
        # json_post = json.dumps(request.POST)
        print('AUDIT -> post: ', json.dumps(request.POST, indent=4))

    context = {
        'current_page': current_page,
        'range': range(10),
        'questions_list': questions_list,
        'public_key': GOOGLE_RECAPTCHA_PUBLIC_KEY,
    }

    return render(request, "audit_page.html", context)


def audit_result_page(request):
    labels = ['Content Marketing', 'Social Media', 'Paid Media', 'Search Marketing',
              'Email Marketing', 'Marketing Strategy', 'Data & Analytics', 'Conversion Optmization'
              ]

    importance_values = [8.5, 8, 7.5, 7.17, 7, 6, 4.67, 3]
    confidence_values = [3, 4, 3, 4, 3, 6, 7, 3]
    marketing_score = 40;
    total_values = [marketing_score, 100 - marketing_score]

    table_data = []
    for i in range(len(labels)):
        data_point = [labels[i], importance_values[i], confidence_values[i]]
        table_data.append(data_point)

    print('AUDIT RESULT table_data', table_data)

    context = {
        'marketing_score': marketing_score,
        'labels': labels,
        'importance_values': importance_values,
        'confidence_values': confidence_values,
        'total_values': total_values,
        'table_data': table_data,
    }

    return render(request, "audit_result_page.html", context)
