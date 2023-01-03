from django.shortcuts import render, redirect
from .data.questions import QUESTIONS
from leads.models import SocialMediaAssesmentLead
import json


QUESTIONS_AREAS = [
    {
        'title': 'Compromiso con el Proyecto',
        'questions': [1, 6],
        'ponderacion': '15'
    },
    {
        'title': 'Conocimiento de Redes Sociales',
        'questions': [6, 12],
        'ponderacion': '20'
    },
    {
        'title': 'Engagement',
        'questions': [12, 18],
        'ponderacion': '15'
    },
    {
        'title': 'Competitividad',
        'questions': [18, 23],
        'ponderacion': '10'
    },
    {
        'title': 'Staff & Recursos',
        'questions': [23, 29],
        'ponderacion': '10'
    },
    {
        'title': 'Canal',
        'questions': [29, 35],
        'ponderacion': '15'
    },
    {
        'title': 'Documentación',
        'questions': [35, 39],
        'ponderacion': '5'
    },
    {
        'title': 'Governance & Medición',
        'questions': [39, 43],
        'ponderacion': '10'
    },
]

# Create your views here.
def assesment_page(request):
    if request.POST:
        if True:
            print('AUDIT -> post: ', json.dumps(request.POST, indent=4))

            answers = []
            for i in range(len(QUESTIONS)):
                answers.append(int(request.POST['assesment_q{}'.format(i + 1)]))

            request.session['social_media_answers'] = answers

            name = request.POST['audit_name']
            lastname = request.POST['audit_last_name']
            company = request.POST['audit_company']
            email = request.POST['audit_email']
            company_size = request.POST['audit_company_size']
            role = request.POST['audit_position']
            phone = request.POST['audit_phone']

            lead = SocialMediaAssesmentLead(
                name=name,
                lastname=lastname,
                company=company,
                email=email,
                company_size=company_size,
                role=role,
                phone=phone,
                results=answers
            )

            lead.save()

            return redirect('social_media_assesments:results')

    context = {
        'questions_list': QUESTIONS,
        'range': range(5),
        # 'public_key': GOOGLE_RECAPTCHA_PUBLIC_KEY,
    }

    return render(request, "social_media_assesments/assesment_page.html", context)


def results_page(request):
    answers = request.session.get('social_media_answers', None)
    table_data = []

    averages = []

    for area in QUESTIONS_AREAS:
        # print("area: ", area)
        start = area['questions'][0] - 1
        end = area['questions'][1] - 1
        area_answers = answers[start:end]
        # print("area_answers: ", area_answers)
        average = sum(area_answers) / len(area_answers)
        averages.append({**area, **{
            'average': float("{:.2f}".format(average))
        }})

    total = 0
    for obj in averages:
        subtotal = obj['average'] * int(obj['ponderacion']) / 100
        # print('subtotal: ', subtotal)
        total += subtotal

    total = float("{:.2f}".format(total))

    for i in range(len(QUESTIONS)):
        answer = {'answer': answers[i]}
        data = {**QUESTIONS[i], **answer}
        table_data.append(
            data
        )

    context = {
        'answers': answers,
        'QUESTIONS': QUESTIONS,
        'table_data': table_data,
        'averages': averages,
        'json_averages': json.dumps(averages),
        'total': total,
    }

    return render(request, "social_media_assesments/results_page.html", context)
