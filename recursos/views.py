from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Recurso


def home_page(request):
    data = [
        {
            "title": "Email Marketing",
            "id": "emailmarketing",
            "resources": [
                {
                    "title": "Capacidad de entrega del email",
                    "desc": "5 tácticas avanzadas de capacidad de entrega del correo electrónico para ayudarte a llegar "
                            "a la bandeja de entrada y aumentar la participación.",
                    "url": "/recursos/capacidad-de-entrega-del-email",
                    "image": "images/recursos/icons/Email-Campaign-Creation.png"
                },
                {
                    "title": "Creación de Campañas de Emailing",
                    "desc": "Asegúrate de que tus campañas de emailing se envíen, reciban clics, proporcionen valor y "
                            "vendan.",
                    "url": "/recursos/creacion-de-campanas-de-email",
                    "image": "images/recursos/icons/Email-Deliverability.png"
                },

            ]
        },
        {
            "title": "Publicidad Pagada",
            "id": "PublicidadPagada",
            "resources": [
                {
                    "title": "Retargeting",
                    "desc": "Una vez que desarrolles campañas de retargeting basadas en el comportamiento anterior de "
                            "los usuarios, generar mayores ingresos será muy sencillo.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Estrategias de Facebook Ads",
                    "desc": "Como marketero, debes pensar en Facebook de manera diferente. Los consumidores no están en "
                            "Facebook para ver anuncios y es importante recordar que sigue siendo una plataforma social.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },
        {
            "title": "Marketing de Contenido",
            "id": "Contenido",
            "resources": [
                {
                    "title": "Estrategias de Marketing de Blogs",
                    "desc": "El blog debe aportar valor a tus clientes ayudandolos a resolver sus problemas. Hay muchas "
                            "formas de hacer esto, aquí te ayudaremos a crear una estrategia paso a paso. ",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Distribución de Contenido",
                    "desc": "El reto más grande es atraer tráfico a tus contenidos. Para ello, debes distribuirlos a "
                            "través de los canales adecuados, ya sea de forma orgánica o con publicidad pagada. ",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Redacción de Contenidos",
                    "desc": "El objetivo de una buena redacción es generar una cierta expectativa o interés en la "
                            "audiencia para que puedas vender más. Aquí te decimos cómo.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Contenido para el Top of the Funnel",
                    "desc": "Aprende a captar la atención de nuevos usuarios y comienza a generar más clientes "
                            "potenciales para tu negocio.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },
        {
            "title": "Search Marketing",
            "id": "Search",
            "resources": [
                {
                    "title": "SEO On-Site",
                    "desc": "Si cada pieza de contenido que produces está optimizada y es valiosa para tus usuarios, "
                            "la clasificación en los motores de búsqueda será un problema menor.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Auditoría SEO",
                    "desc": "Nadie quiere informar sobre métricas irrelevantes. Descubre el cómo y el por qué de los "
                            "informes de SEO.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Herramientas de Investigación de Palabras Clave",
                    "desc": "Aprende a hacer una investigación de palabras clave y crear contenido que sea importante "
                            "para tus clientes.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "SEO Backlinks",
                    "desc": "Con más backlinks, conducirás más y mejor tráfico a tu sitio, ¡lo que significa más dinero!",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },
        {
            "title": "Copywriting",
            "id": "Copywriting",
            "resources": [
                {
                    "title": "Persuade a Prospectos",
                    "desc": "Con las herramientas y estrategias correctas puedes persuadir a los prospectos para que "
                            "compren más y más rápido. ",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "¿Qué es Copywriting?",
                    "desc": "Cuando se trata de alcanzar más clientes, no hay nada más importante que el mensaje.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Copywriting Efectivo",
                    "desc": "Una investigación efectiva y el conocimiento de la voz de tu marca te ayudarán a producir "
                            "un ‘copy’ efectivo",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Propuesta Única de Venta",
                    "desc": "Tu propuesta única de venta debe ser sólida y debe ser clara en cualquier ‘copy’ de ventas.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },
        {
            "title": "Growth Marketing",
            "id": "GrowthMarketing",
            "resources": [
                {
                    "title": "Social Listening",
                    "desc": "Social Listening es la clave del éxito cuando se trata de Redes Sociales. "
                            "Te explicamos porque",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Community Management",
                    "desc": "La función del Community Manager es crear un entorno saludable para que los miembros se "
                            "conecten e interactúen.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Construir una Comunidad Digital",
                    "desc": "Descubre cómo trabajar en equipo puede llevar tus estrategias de Marketing Digital "
                            "al siguiente nivel.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "Qué es un Plan de Ejecución",
                    "desc": "Haz crecer tu negocio a medida que sigues el paso a paso que te llevarán a ser más "
                            "productivo.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },
        {
            "title": "Optimización de Tasas de Conversión",
            "id": "tasasconversion",
            "resources": [
                {
                    "title": "Personalización del Website",
                    "desc": "El objetivo final de la personalización es convertir tu sitio web en tu mejor vendedor.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },
                {
                    "title": "A/B Testing",
                    "desc": "Descubre por qué los A/B Test son una de las mejores formas de saber qué resuena con tus "
                            "clientes.",
                    "url": "#",
                    "image": "images/recursos/placeholder.png"
                },

            ]
        },

    ]

    context = {
        "data": data
    }

    return render(request, "recursos/recursos_page.html", context)


def recurso_detail_view(request, slug):
    obj = get_object_or_404(Recurso, slug=slug)
    template_name = 'recursos/detail.html'

    context = {
        "object": obj,
    }

    return render(request, template_name, context)
