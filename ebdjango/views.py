from django.shortcuts import render, redirect
import json
from ebdjango.settings import GOOGLE_RECAPTCHA_PUBLIC_KEY
from blog.models import BlogPost
from leads.models import AuditoriaLead
from .forms import ContactForm
from ebdjango.decorators import check_recaptcha
from django.urls import reverse

from guia_marketing.models import Capitulo


def home_page(request):
    blog_posts = BlogPost.objects.all()

    if len(blog_posts) > 3:
        blog_posts = blog_posts[:3]

    context = {
        "blog_posts": blog_posts,
    }

    return render(request, "home.html", context)


def inbound_page(request):
    print(request.user)

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


def audit_pre_page(request):
    context = {
    }

    return render(request, "audit_pre_page.html", context)


def audit_landing_page(request):
    context = {
    }

    return render(request, "audit_landing_page.html", context)


@check_recaptcha
def audit_page(request):
    questions_list = [
        # 11
        [
            'Dirección ha comprometido su apoyo a la creación de una estrategia de SEO a largo plazo. Se ha aprobado un '
            'plan y una hoja de ruta del proyecto y los indicadores clave de rendimiento están documentados y bien '
            'comprendidos.'],
        # 12
        [
            'La estrategia de SEO está claramente definida e incluye el uso de texto enriquecido con palabras clave y '
            'desarrollo de enlaces externos (external links).'
        ],
        # 13
        [
            'La empresa cuenta con recursos financieros y humanos necesarios para la implementación de esta iniciativa'
        ],
        # 14
        [
            'El equipo interno o proveedor que ejecutará el SEO cuenta con la capacitación y los talleres de SEO necesarios'
        ],
        # 15
        [
            'Las campañas de búsqueda orgánica y de pagada se integran con otros esfuerzos de marketing digital. Los nuevos '
            'clientes potenciales y/o ventas se rastrean con un sistema y se pueden atribuir a cierto esfuerzo'
        ],
        # 16
        [
            'Se está llevando a cabo un plan de mantenimiento de SEO  que incluye investigación de keywords y '
            'longtails de forma regular'
        ],
        # 21
        [
            'Los programas de análisis de sitios web como Webtrends y Google Analytics se utilizan para rastrear el número '
            'de visitantes, el tiempo promedio en el sitio, los marcadores, etc.'
        ],
        # 22
        [
            'Hay disponible un mapa del sitio con enlaces de texto a cada página y se ha creado una estructura de '
            'directorio plana en el sitio web de la empresa'
        ],
        # 23
        [
            'Los involucrados cuentan con la tecnología necesaria para la implementación exitosa de una estrategia SEO'
        ],
        # 24
        [
            'El proceso y la comunicación entre el Responsable del SEO y el desarrollador del sitio web están claro y los '
            'roles y responsabilidades están definidos.'
        ],
        # 25
        [
            'La fecha de vencimiento del dominio es más de 1 año y la disponibilidad del ISP del servicio es del 99.9%'
        ],
        # 26
        [
            'El sitio web se ha creado utilizando una arquitectura de sitio compatible con SEO y el diseño de la página '
            'se trabajo bajo una layout enfocado en SEO'
        ],
        # 31
        [
            'Los programas de análisis de sitios web como Webtrends y Google Analytics se utilizan para rastrear el '
            'número de visitantes, el tiempo promedio en el sitio, los marcadores, etc.'
        ],
        # 32
        [
            'Hay disponible un mapa del sitio con enlaces de texto a cada página y se ha creado una estructura de '
            'directorio plana en el sitio web de la empresa'
        ],
        # 33
        [
            'Los involucrados cuentan con la tecnología necesaria para la implementación exitosa de una estrategia SEO'
        ],
        # 34
        [
            'El proceso y la comunicación entre el Responsable del SEO y el desarrollador del sitio web están claro '
            'y los roles y responsabilidades están definidos.'
        ],
        # 35
        [
            'La fecha de vencimiento del dominio es más de 1 año y la disponibilidad del ISP del servicio es del 99.9%'
        ],
        # 36
        [
            'El sitio web se ha creado utilizando una arquitectura de sitio compatible con SEO y el diseño de la página '
            'se trabajo bajo una layout enfocado en SEO'
        ],
        # 41
        [
            'Estamos familiarizados con las métricas básicas de palabras clave y tenemos KPI documentados.'
        ],
        # 42
        [
            'Nuestros resultados se miden y se informan como mínimo trimestralmente'
        ],
        # 43
        [
            'Nuestros sistemas de medición automatizan el proceso de generación de informes'
        ],
        # 44
        [
            'Sabemos, en porcentaje, cuánto de nuestro tráfico proviene de manera orgánica frente al tráfico de pago.'
        ],
        # 45
        [
            'Los esfuerzos de SEO de los competidores se supervisan y revisan constantemente'
        ],
        # 46
        [
            'Continuamos rastreando las palabras clave y las páginas que generan tráfico a nuestro sitio, así como el crecimiento de SEO frente al crecimiento total del sitio.'
        ],

    ]

    current_page = questions_list[0]
    questions_titles = ['Estrategia y Habilidades',
                        'Definición de procesos, Automatización y Sistemas',
                        'Keyword Management',
                        'Informes y Resultados'
                        ]

    if request.POST:
        if request.recaptcha_is_valid:
            # json_post = json.dumps(request.POST)
            # print('AUDIT -> post: ', json.dumps(request.POST, indent=4))

            def average(lst):
                return round(sum(lst) / len(lst), 2)

            seo_list = [
                int(request.POST['audit_option_1_1']),
                int(request.POST['audit_option_2_1']),
                int(request.POST['audit_option_3_1']),
                int(request.POST['audit_option_4_1']),
                int(request.POST['audit_option_5_1']),
                int(request.POST['audit_option_6_1']),
            ]
            seo_ave = average(seo_list)

            sistemas_list = [
                int(request.POST['audit_option_7_1']),
                int(request.POST['audit_option_8_1']),
                int(request.POST['audit_option_9_1']),
                int(request.POST['audit_option_10_1']),
                int(request.POST['audit_option_11_1']),
                int(request.POST['audit_option_12_1']),
            ]
            sistemas_ave = average(sistemas_list)

            keyword_list = [
                int(request.POST['audit_option_13_1']),
                int(request.POST['audit_option_14_1']),
                int(request.POST['audit_option_15_1']),
                int(request.POST['audit_option_16_1']),
                int(request.POST['audit_option_17_1']),
                int(request.POST['audit_option_18_1']),
            ]
            keyword_ave = average(keyword_list)

            # print("seo_list", seo_list)
            # print("seo_ave", seo_ave)

            resultados_list = [
                int(request.POST['audit_option_19_1']),
                int(request.POST['audit_option_20_1']),
                int(request.POST['audit_option_21_1']),
                int(request.POST['audit_option_22_1']),
                int(request.POST['audit_option_23_1']),
                int(request.POST['audit_option_24_1']),
            ]
            resultados_ave = average(resultados_list)

            audit_ave = average([seo_ave, sistemas_ave, keyword_ave, resultados_ave])

            result = {
                "seo_list": seo_list,
                "seo_ave": seo_ave,
                "sistemas_list": sistemas_list,
                "sistemas_ave": sistemas_ave,
                "keyword_list": keyword_list,
                "keyword_ave": keyword_ave,
                "resultados_list": resultados_list,
                "resultados_ave": resultados_ave,
                "audit_ave": audit_ave,
            }

            # print('AUDIT -> result dict: ', json.dumps(result, indent=4))

            request.session['seo_audit_result'] = result

            name = request.POST['audit_name']
            lastname = request.POST['audit_last_name']
            company = request.POST['audit_company']
            email = request.POST['audit_email']
            company_size = request.POST['audit_company_size']
            role = request.POST['audit_position']

            lead = AuditoriaLead(
                name=name,
                lastname=lastname,
                company=company,
                email=email,
                company_size=company_size,
                role=role,
                results=result
            )

            lead.save()

            return redirect('audit_result')

    context = {
        'current_page': current_page,
        'range': range(5),
        'questions_list': questions_list,
        'public_key': GOOGLE_RECAPTCHA_PUBLIC_KEY,
        'questions_titles': questions_titles,
    }

    return render(request, "audit_page.html", context)


def audit_result_page(request):
    seo_audit_result = request.session.get('seo_audit_result', None)

    sistemas_list = seo_audit_result['sistemas_list']
    sistemas_ave = seo_audit_result['sistemas_ave']

    keyword_list = seo_audit_result['keyword_list']
    keyword_ave = seo_audit_result['keyword_ave']

    resultados_list = seo_audit_result['resultados_list']
    resultados_ave = seo_audit_result['resultados_ave']

    audit_ave = seo_audit_result['audit_ave']

    seo_list = seo_audit_result['seo_list']
    seo_ave = seo_audit_result['seo_ave']

    labels = ['Content Marketing', 'Social Media', 'Paid Media', 'Search Marketing',
              'Email Marketing', 'Marketing Strategy', 'Data & Analytics', 'Conversion Optmization'
              ]

    importance_values = [8.5, 8, 7.5, 7.17, 7, 6, 4.67, 3]
    confidence_values = [3, 4, 3, 4, 3, 6, 7, 3]
    marketing_score = 40
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
        'seo_audit_result': seo_audit_result,
        'seo_list': seo_list,
        'seo_ave': seo_ave,
        'sistemas_list': sistemas_list,
        'sistemas_ave': sistemas_ave,
        'keyword_list': keyword_list,
        'keyword_ave': keyword_ave,
        'resultados_list': resultados_list,
        'resultados_ave': resultados_ave,
        'audit_ave': audit_ave,
    }

    return render(request, "audit_result_page.html", context)


def events_list_page(request):
    context = {
    }

    return render(request, "events_list_page.html", context)


def experts_list_page(request):
    expert_list = range(8)

    context = {
        'expert_list': expert_list,
    }

    return render(request, "experts_list_page.html", context)


def audio_visual_page(request):
    context = {
    }

    return render(request, "audio_visual_page.html", context)


def soluciones_page(request):
    context = {
    }

    return render(request, "soluciones_page.html", context)


def programas_estrategicos_page(request):
    blog_posts = BlogPost.objects.all()[:3]

    context = {
        "blog_posts": blog_posts,
    }

    return render(request, "soluciones_programas_estrategicos_page.html", context)


def soporte_tactico_page(request):
    blog_posts = BlogPost.objects.all()[:3]

    context = {
        "blog_posts": blog_posts,
    }

    return render(request, "soluciones_soporte_tactico_page.html", context)


def proyectos_page(request):
    blog_posts = BlogPost.objects.all()[:3]

    context = {
        "blog_posts": blog_posts,
    }

    return render(request, "soluciones_proyectos_page.html", context)


def nosotros_page(request):
    context = {
    }

    return render(request, "nosotros_page.html", context)


def aviso_de_privacidad_page(request):
    context = {
    }

    return render(request, "aviso_de_privacidad_page.html", context)


capitulos = [
    {
        'title': 'La Guía Definitiva del Marketing Digital',
        'url': '/guia_marketing_digital'
    },
    {
        'title': 'Desarrolla tu Estrategia de Marketing Digital',
        'url': '/guia_marketing_digital/1'
    },
    {
        'title': 'Desarrollando una Estrategia de Marketing de Contenido',
        'url': '/guia_marketing_digital/2'
    },
    {
        'title': 'Elaboración de un Plan de Publicidad Digital',
        'url': '/guia_marketing_digital/3'
    },
    {
        'title': 'Desarrolla una Estrategia de Redes Sociales',
        'url': '/guia_marketing_digital/4'
    },
    {
        'title': 'Seguir las mejores prácticas de Marketing por correo electrónico',
        'url': '/guia_marketing_digital/5'
    },
    {
        'title': 'Diseña tu Estrategia para Motores De Búsqueda',
        'url': '/guia_marketing_digital/6'
    },
    {
        'title': 'Utiliza los analíticos en tu Marketing Digital',
        'url': '/guia_marketing_digital/7'
    },
    {
        'title': 'Aprovechar la optimización de la tasa de conversión para impulsar el crecimiento',
        'url': '/guia_marketing_digital/8'
    },
    {
        'title': '¿Que sigue?',
        'url': '/guia_marketing_digital/9'
    },
]