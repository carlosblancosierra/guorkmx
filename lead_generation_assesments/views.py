from django.shortcuts import render, redirect
from leads.models import LeadManagementReadinessLead
import json

# Create your views here.


QUESTIONS_DATA = {
    1: {
        'title': 'Estrategia, Procesos y Habilidades',
        'questions': [
            'Nuestra estrategia de generación de leads esta documentada, de manera clara y concisa y esta aprobada por el CEO',
            'Los esfuerzos de generación de leads se priorizan para garantizar la asignación adecuada de recursos.',
            'Actualmente el proceso de generación de leads esta definido- Además, es repetible y medible',
            'Dirección comprende claramente el Inbound Marketing y cómo puede beneficiar a la empresa',
            'Tenemos las habilidades necesarias internamente para implementar nuestra estrategia de generación de leads',
        ]
    },
    2: {
        'title': 'Marketing Automation y Lead Management',
        'questions': [
            'Los leads que reciben se puntúan por su calidad según criterios explícitos con base en un Buyer Persona',
            'Los leads se nutren con campañas de marketing para alinear los ciclos de compra y ventas.',
            'Los leads se envían automáticamente al ejecutivo adecuado según  reglas de asignación de clientes potenciales.',
            'El equipo comercial recibe una alerta cuando los prospectos dan una señal de compra (visita el sitio web, descarga del documento, etc.).',
            'Los correos electrónicos de respuesta automática se envían cuando un cliente potencial interactúa (completa un formulario, etc.).',
            'Existen reglas de automatización para agilizar y automatizar los procesos y las comunicaciones clave.',
        ]
    },
    3: {
        'title': 'Gestión de Base de Datos',
        'questions': [
            'Las campañas de email marketing se pueden ejecutar con enlaces que rastrean las actividades de los clientes potenciales (aperturas, clics).',
            'Las variables dinámicas, como el nombre del prospecto, se pueden insertar automáticamente en las campañas de email marketing.',
            'Se pueden crear listas de contactos, importar y actualizar en una base de datos centralizada.',
            'Puedes evitar la duplicación de prospectos y clientes con un identificador único. Ejemplo: correo electrónico.',
            'Se pueden medir fácilmente los resultados de las campañas de email marketing ya que hay códigos de trackeo en el sitio web o landing page .',
            'Hemos desarrollado esfuerzos digitales para crecer el tamaño de la base de datos de la empresa',
        ]
    },
    4: {
        'title': '"Website, Blog & Comunidad"',
        'questions': [
            'Nuestro sitio web es el punto principal de nuestra estrategia de generación de leads',
            'Hemos comparado nuestro sitio web con la competencia y nuestro sitio web ofrece una ventaja competitiva.',
            'Tenemos una estrategia SEO claramente definida con metas, objetivos, medidas y metas.',
            'Los clientes pueden interactuar con nuestra empresa a través del blog que se mantiene actualizado constantemente',
            'Tenemos una comunidad digital en donde nuestros clientes pueden interactuar con la marca. ',
            'Nuestro sitio web es fácil de usar y tiene rutas de navegación claras.',
        ]
    },
    5: {
        'title': 'Conversión & Landing Pages',
        'questions': [
            'Los formularios se pueden crear directamente por el área de marketing',
            'En las landing pages es posible identificar si los prospectos clientes potenciales son generados por redes sociales, email marketing, publicidad pagada u otros canales.',
            'Conocemos las tasas de conversión de cada una de nuestras landing pages.',
            'Tenemos campañas de publicidad pagada especificamente creadas para aquellos visitantes que entraron a la landing page pero no llenaron el formulario',
            'Los formularios identifican correo electrónico no válidos / gratuitas (hotmail, yahoo, gmail, etc.)',
            'Los campos del formulario se pueden personalizar y configurar para capturar información adicional durante las visitas web posteriores.',
        ]
    },
    6: {
        'title': '"Analíticos, SEO & SEM"',
        'questions': [
            'Se realiza un seguimiento de la actividad del sitio web',
            'Los informes diarios de actividad de los visitantes del sitio web se generan automáticamente y se envían a los responsables de marketing y ventas.',
            'El tráfico orgánico / pagado se rastrea y se compara con los ingresos reales generados para medir el ROI.',
            'Las consultas de búsqueda dentro del sitio web se rastrean y vinculan al historial de actividad de prospectos y clientes.',
            'Los visitantes del sitio web no registrados / no convertidos son identificados la tecnología WHOIS para determinar el nombre de la empresa.',
            'Aparecemos en las primeras 2 páginas de resultados de búsqueda para nuestras palabras clave principales.',
        ]
    },
    7: {
        'title': 'Alianzas y Canales ',
        'questions': [
            'Nos hemos unido a todas las asociaciones relevantes para nuestra industria y nos relacionamos regularmente con empresas afiliadas.',
            'Podemos monitorear la cantidad de clientes potenciales / negocios que ingresan por el canal de aliados.',
            'Los esfuerzos de aliados están bien respaldados con documentación, capacitación en ventas y soporte continuo.',
            'Hemos formado asociaciones estratégicas para proporcionar a nuestros clientes valor y recursos adicionales.'
        ]
    },
    8: {
        'title': 'Integración de Sistemas',
        'questions': [
            'Nuestros esfuerzos de marketing (emailing, marketing automation, landing pages, SEM, etc.) y CRM estan integrados.',
            'La fuente de donde provienen los leads es un campo obligatorio en nuestro CRM para garantizar que podamos medir el ROI de los esfuerzos digitales. ',
            'Las actividades de los prospectos(visitas a la página del sitio web, apertura de correos electrónicos, descargas) se pueden ver fácilmente en el sistema CRM.',
            'Los prospectos que no son perseguidos activamente por  ventas después de 60 días entran en una campaña de nutrición.',
            'El sistema permite automáticamente calificar a los prospectos en el CRM',
        ]
    },
    9: {
        'title': 'Métricas y Reporteo',
        'questions': [
            "Los KPI's de marketing son establecidos antes de la ejecución de la campaña.",
            'Podemos determinar los ingresos generados y el ROI para todos los esfuerzos de marketing.',
            'Existen puntos de referencia (benchmarks) para definir métricas clave de marketing (CPC, CPL, ROI, tasas de conversión, etc.).',
            'Nuestros sistemas de generación de leads se integran con el CRM para vincular los costos a las oportunidades ganadas (ROI).',
            'Contamos con un dashboard de marketing para comunicar las métricas a dirección.',

        ]
    }
}

QUESTIONS_LIST = [
    # 1
    'Nuestra estrategia de generación de leads esta documentada, de manera clara y concisa y esta aprobada por el CEO',
    'Los esfuerzos de generación de leads se priorizan para garantizar la asignación adecuada de recursos.',
    'Actualmente el proceso de generación de leads esta definido- Además, es repetible y medible',
    'Dirección comprende claramente el Inbound Marketing y cómo puede beneficiar a la empresa',
    'Tenemos las habilidades necesarias internamente para implementar nuestra estrategia de generación de leads',

    # 2
    'Los leads que reciben se puntúan por su calidad según criterios explícitos con base en un Buyer Persona',
    'Los leads se nutren con campañas de marketing para alinear los ciclos de compra y ventas.',
    'Los leads se envían automáticamente al ejecutivo adecuado según  reglas de asignación de clientes potenciales.',
    'El equipo comercial recibe una alerta cuando los prospectos dan una señal de compra (visita el sitio web, descarga del documento, etc.).',
    'Los correos electrónicos de respuesta automática se envían cuando un cliente potencial interactúa (completa un formulario, etc.).',
    'Existen reglas de automatización para agilizar y automatizar los procesos y las comunicaciones clave.',

    # 3
    'Las campañas de email marketing se pueden ejecutar con enlaces que rastrean las actividades de los clientes potenciales (aperturas, clics).',
    'Las variables dinámicas, como el nombre del prospecto, se pueden insertar automáticamente en las campañas de email marketing.',
    'Se pueden crear listas de contactos, importar y actualizar en una base de datos centralizada.',
    'Puedes evitar la duplicación de prospectos y clientes con un identificador único. Ejemplo: correo electrónico.',
    'Se pueden medir fácilmente los resultados de las campañas de email marketing ya que hay códigos de trackeo en el sitio web o landing page .',
    'Hemos desarrollado esfuerzos digitales para crecer el tamaño de la base de datos de la empresa',

    # 4
    'Nuestro sitio web es el punto principal de nuestra estrategia de generación de leads',
    'Hemos comparado nuestro sitio web con la competencia y nuestro sitio web ofrece una ventaja competitiva.',
    'Tenemos una estrategia SEO claramente definida con metas, objetivos, medidas y metas.',
    'Los clientes pueden interactuar con nuestra empresa a través del blog que se mantiene actualizado constantemente',
    'Tenemos una comunidad digital en donde nuestros clientes pueden interactuar con la marca. ',
    'Nuestro sitio web es fácil de usar y tiene rutas de navegación claras.',

    # 5
    'Los formularios se pueden crear directamente por el área de marketing',
    'En las landing pages es posible identificar si los prospectos clientes potenciales son generados por redes sociales, email marketing, publicidad pagada u otros canales.',
    'Conocemos las tasas de conversión de cada una de nuestras landing pages.',
    'Tenemos campañas de publicidad pagada especificamente creadas para aquellos visitantes que entraron a la landing page pero no llenaron el formulario',
    'Los formularios identifican correo electrónico no válidos / gratuitas (hotmail, yahoo, gmail, etc.)',
    'Los campos del formulario se pueden personalizar y configurar para capturar información adicional durante las visitas web posteriores.',

    # 6
    'Se realiza un seguimiento de la actividad del sitio web',
    'Los informes diarios de actividad de los visitantes del sitio web se generan automáticamente y se envían a los responsables de marketing y ventas.',
    'El tráfico orgánico / pagado se rastrea y se compara con los ingresos reales generados para medir el ROI.',
    'Las consultas de búsqueda dentro del sitio web se rastrean y vinculan al historial de actividad de prospectos y clientes.',
    'Los visitantes del sitio web no registrados / no convertidos son identificados la tecnología WHOIS para determinar el nombre de la empresa.',
    'Aparecemos en las primeras 2 páginas de resultados de búsqueda para nuestras palabras clave principales.',

    # 7
    'Nos hemos unido a todas las asociaciones relevantes para nuestra industria y nos relacionamos regularmente con empresas afiliadas.',
    'Podemos monitorear la cantidad de clientes potenciales / negocios que ingresan por el canal de aliados.',
    'Los esfuerzos de aliados están bien respaldados con documentación, capacitación en ventas y soporte continuo.',
    'Hemos formado asociaciones estratégicas para proporcionar a nuestros clientes valor y recursos adicionales.',

    # 8
    'Nuestros esfuerzos de marketing (emailing, marketing automation, landing pages, SEM, etc.) y CRM estan integrados.',
    'La fuente de donde provienen los leads es un campo obligatorio en nuestro CRM para garantizar que podamos medir el ROI de los esfuerzos digitales. ',
    'Las actividades de los prospectos(visitas a la página del sitio web, apertura de correos electrónicos, descargas) se pueden ver fácilmente en el sistema CRM.',
    'Los prospectos que no son perseguidos activamente por  ventas después de 60 días entran en una campaña de nutrición.',
    'El sistema permite automáticamente calificar a los prospectos en el CRM',

    # 9
    "Los KPI's de marketing son establecidos antes de la ejecución de la campaña.",
    'Podemos determinar los ingresos generados y el ROI para todos los esfuerzos de marketing.',
    'Existen puntos de referencia (benchmarks) para definir métricas clave de marketing (CPC, CPL, ROI, tasas de conversión, etc.).',
    'Nuestros sistemas de generación de leads se integran con el CRM para vincular los costos a las oportunidades ganadas (ROI).',
    'Contamos con un dashboard de marketing para comunicar las métricas a dirección.',

]
QUESTIONS_TITLES = [
    'Estrategia, Procesos y Habilidades',
    'Marketing Automation y Lead Management',
    'Gestión de Base de Datos',
    'Website, Blog & Comunidad',
    'Conversión & Landing Pages',
    'Analíticos, SEO & SEM',
    'Alianzas y Canales',
    'Integración de Sistemas',
    'Métricas y Reporteo',
]

RESULT_DATA = [
    {
        "title": "Estrategia de Generación de Leads",
        "description": "Utiliza la Herramienta Lead Generation Scorecard para conseguir la aprobación de Dirección General",
        "resource": "Lead Generation Scorecard",
        "url": ""
    },
    {
        "title": "Priorización del Programa",
        "description": "Usa la herramienta Priorización de Proyectos para evaluar la viabilidad y el valor real del proyecto para la empresa.",
        "resource": "Priorizaciónd de Proyectos",
        "url": ""
    },
    {
        "title": "Definición de Procesos",
        "description": "Usa la herramienta Lead Model Acquisition para documentar el proceso de generación de leads.",
        "resource": "Lead Model Acquisition",
        "url": ""
    },
    {
        "title": "Medición y Seguimiento de KPI's",
        "description": "Haz de la herramientaLead Generation Scorecard un documento vivo para comunicar los resultados de manera constante.",
        "resource": "Lead Generation Scorecard",
        "url": ""
    },
    {
        "title": "Habilidades y Recursos para Ejecución",
        "description": "Determina las habilidades/recursos y contrata o subcontrata según sea necesario.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Lead Scoring",
        "description": "Construye un índice de Lead Scoring para clasificar prospectos basados en su perfil y actividad con la marca.",
        "resource": "Lead Scoring",
        "url": ""
    },
    {
        "title": "Lead Nurturing",
        "description": "Diseña y ejecuta una campaña de email-marketing de 'goteo' para nutrir clientes potenciales a lo largo del tiempo.",
        "resource": "Campañas de Email Marketing Efectivas",
        "url": ""
    },
    {
        "title": "Asignación de Leads",
        "description": "Establece una regla de negocio para asignar clientes potenciales y automatiza este proceso si es posible.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Alertas para Equipo de Ventas",
        "description": "Busca una tecnología que permita alertarte cuando recibas leads calificados en tus canales digitales.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Mensajes de Auto-Respuesta",
        "description": "Configura mensajes de auto-respuesta que puedan enviarse automáticamente a los visitantes del sitio web",
        "resource": "",
        "url": ""
    },
    {
        "title": "Reglas de Automatización",
        "description": "Crea reglas para tu sistema de lead scoring para cada uno de tus flujos de trabajo (workflows)",
        "resource": "Lead Scoring",
        "url": ""
    },
    {
        "title": "Sistema de Email Marketing",
        "description": "Asegúrate de que tu email marketing puedan enviar mensajes con un enlace trackeable.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Variable Dinámica",
        "description": "Asegúrate de que tu sistema de email marketing pueda enviar mensajes personalizados.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Lista de Contactos Centralizada",
        "description": "Cree una base de datos que se pueda administrar fácilmente.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Duplicación de Contactos",
        "description": "Configura tu CRM para que no duplique data",
        "resource": "",
        "url": ""
    },
    {
        "title": "Medición de Resultados de esfuerzos offline",
        "description": "Configura un número único para darle seguimiento a los resultados de campañas off-line",
        "resource": "",
        "url": ""
    },
    {
        "title": "Tamaño y Calidad de la Lista",
        "description": "Audita tus programas de generación de leads y considera campañas de generación de leads (MQL's)",
        "resource": "Programa: Lead Generation",
        "url": ""
    },
    {
        "title": "Efectividad del Sitio Web",
        "description": "Aprovecha la capacidad del sitio web para comunicar a tus 'stakeholders' información 24/7",
        "resource": "",
        "url": ""
    },
    {
        "title": "Ranking de Competitividad del Sitio Web",
        "description": "Realiza un análisis de sitios web para identificar tu lugar entre tus competidores.",
        "resource": "Análisis Sitio Web",
        "url": ""
    },
    {
        "title": "Estrategia del Sitio Web",
        "description": "Utiliza la herramienta Estrategia de Marketing en Sitio Web para documentar tus objetivos estratégicos",
        "resource": "Estrategia de Marketing en Sitio Web",
        "url": ""
    },
    {
        "title": "Blog",
        "description": "Agrega un blog a tu sitio web para actualizar tu contenido y comunicar ultimas noticias.",
        "resource": "Programa: Blogging para Negocios",
        "url": ""
    },
    {
        "title": "Atención al Cliente (Comunidad - Foro)",
        "description": "Consider usar un portal o foro de soporte al cliente",
        "resource": "",
        "url": ""
    },
    {
        "title": "Usabilidad del Sitio Web",
        "description": "Asegúrate de que la navegación en tu sitio web sea fáciles e intuitiva.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Administración de Formularios en Website",
        "description": "Integra los formularios de tu sitio web con un CRM.",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Micrositios",
        "description": "Investiga cómo las landing pages y los URL's personalizados pueden mejorar las tasas de conversión.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Landing Pages",
        "description": "Prueba las tasas de conversión de la landing page con diferentes formatos y estilos.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Formularios Incompletos",
        "description": "Determina si tus formularios  tienen la capacidad de capturar información parcial.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Discriminación de Datos",
        "description": "Utiliza una tecnología que permita crear formularios para bloquear direcciones de correo electrónico gratuitas (que no sean corporativas).",
        "resource": "",
        "url": ""
    },
    {
        "title": "Personalización de Formulario",
        "description": "Investiga la elaboración de perfiles progresivos como técnicas para recopilar información adicional sobre los prospectos.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Analíticos Web por Usuario",
        "description": "Utiliza un sistema de Marketing Automation para conocer información adicional sobre los visitantes de tu sitio web.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Reporte diario de Visitantes",
        "description": "Configura reportes diarios de las actividades de los visitantes y envialos a los representantes de ventas de manera diaria",
        "resource": "",
        "url": ""
    },
    {
        "title": "Reporteo y Analíticos del Sitio Web",
        "description": "Asegúra que sea fácil conocer la fuente de clientes potenciales en el CRM para rastrear el ROI por canal",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Monitoreo de Consulta de Búsqueda",
        "description": "Pregunta al departamento de TI si pueden trabajar reportes personalizados de tu sitio web.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Bloqueo de Emailing Personal",
        "description": "Utiliza tecnología para identificar a los usuarios no registrados por su dirección IP",
        "resource": "Auditoría Contenido Sitio Web",
        "url": ""
    },
    {
        "title": "Lookup Reversible de IP (WHOIS)",
        "description": "Realiza un ejercicio de análisis de palabras clave para determinar el posicionamiento SEO del sitio web",
        "resource": "",
        "url": ""
    },
    {
        "title": "Asociaciones & Networking",
        "description": "Evalua las asociaciones que se pueden unir a la empresa y que puedan crear oportunidades de negocio en un corto plazo.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Seguimiento de Leads (Alianzas)",
        "description": "Crea un proceso que te permita identificar que aliado generó cada prospecto",
        "resource": "",
        "url": ""
    },
    {
        "title": "Soporte",
        "description": "Examina los programas y materiales de soporte de ventas y modifícalos si es necesario.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Alianzas Estratégicas Formadas",
        "description": "Piensa en posibles asociaciones que puedan agregar valor a tus clientes.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Integración CRM/Marketing",
        "description": "Determina si tu sistema de CRM y marketing pueden integrarse.",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Campo Fuente/Canal del Prospecto",
        "description": "Personaliza tu CRM y asegúrarte de que exista un campo obligatorio que explique la Fuente/Canal de los clientes potenciales",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Actividades del Prospecto visibles en el CRM",
        "description": "Integra tu sistema de automatización de marketing con el CRM.",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Recalificación de Clientes Potenciales",
        "description": "Evalua las oportunidades estancadas",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Lead Scoring en el CRM",
        "description": "Trabaja para integrar lead scoring en tu CRM.",
        "resource": "Programa: CRM",
        "url": ""
    },
    {
        "title": "Identificación de KPI's & Monitoreo",
        "description": "Establece los KPI's obligatorios de cada esfuerzo previo al lanzamiento del mismo.",
        "resource": "",
        "url": ""
    },
    {
        "title": "Habilidad para Medir ROI",
        "description": "Encuentra cualquier laguna en el proceso de generación de reportes para hacerlos realmente efectivos",
        "resource": "",
        "url": ""
    },
    {
        "title": "Benchmarks de Métricas Clave",
        "description": "Recoplia métricas para establecer 'benchmarks' y medir el desempeño de tus esfuerzos digitales",
        "resource": "",
        "url": ""
    },
    {
        "title": "Informes",
        "description": "Crea reportes sobre los costos totales de la camapña y los ingresos generados para determinar el ROI",
        "resource": "",
        "url": ""
    },
    {
        "title": "Dashboard Marketing",
        "description": "Crea un dashboard para tener visibilidad y facilitar el reporteo a dirección.",
        "resource": "Métricas Lead Geneartion",
        "url": ""
    }
]

QUESTIONS_AREAS = [
    {
        'title': 'Estrategia, Procesos y Habilidades',
        'questions': [1, 6],
        'ponderacion': '20'
    },
    {
        'title': 'Marketing Automation y Lead Management',
        'questions': [6, 12],
        'ponderacion': '15'
    },
    {
        'title': 'Gestión de Base de Datos',
        'questions': [12, 18],
        'ponderacion': '5'
    },
    {
        'title': 'Website, Blog & Comunidad',
        'questions': [18, 24],
        'ponderacion': '0'
    },
    {
        'title': 'Conversión & Landing Pages',
        'questions': [24, 30],
        'ponderacion': '10'
    },
    {
        'title': 'Analíticos, SEO & SEM',
        'questions': [30, 36],
        'ponderacion': '10'
    },
    {
        'title': 'Alianzas y Canales',
        'questions': [36, 40],
        'ponderacion': '20'
    },
    {
        'title': 'Integración de Sistemas',
        'questions': [40, 45],
        'ponderacion': '10'
    },
    {
        'title': 'Métricas y Reporteo',
        'questions': [45, 50],
        'ponderacion': '10'
    },
]


def landing_page(request):
    context = {
    }

    return render(request, "landing_page.html", context)


# @check_recaptcha
def assesment_page(request):
    if request.POST:
        if True:
            print('AUDIT -> post: ', json.dumps(request.POST, indent=4))

            answers = []
            for i in range(len(QUESTIONS_LIST)):
                answers.append(int(request.POST['lead_assesment_q{}'.format(i + 1)]))

            request.session['lead_generation_answers'] = answers

            name = request.POST['audit_name']
            lastname = request.POST['audit_last_name']
            company = request.POST['audit_company']
            email = request.POST['audit_email']
            company_size = request.POST['audit_company_size']
            role = request.POST['audit_position']
            phone = request.POST['audit_phone']

            lead = LeadManagementReadinessLead(
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

            return redirect('lead_generation_assesments:results')

    context = {
        'questions_titles': QUESTIONS_TITLES,
        'questions_list': QUESTIONS_LIST,
        'range': range(5),
        # 'public_key': GOOGLE_RECAPTCHA_PUBLIC_KEY,
    }

    return render(request, "lead_generation_assesments/assesment_page.html", context)


def results_page(request):
    answers = request.session.get('lead_generation_answers', None)
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

    for i in range(len(RESULT_DATA)):
        answer = {'answer': answers[i]}
        data = {**RESULT_DATA[i], **answer}
        table_data.append(
            data
        )

    context = {
        'answers': answers,
        'RESULT_DATA': RESULT_DATA,
        'table_data': table_data,
        'QUESTIONS_TITLES': QUESTIONS_TITLES,
        'averages': averages,
        'json_averages': json.dumps(averages),
        'total': total,
    }

    return render(request, "lead_generation_assesments/results_page.html", context)
