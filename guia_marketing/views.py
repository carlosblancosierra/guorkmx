from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Capitulo


def guia_marketing_digital(request):
    capitulos = Capitulo.objects.active()

    next_url = capitulos.first().get_absolute_url

    context = {
        'capitulos': capitulos,
        'next_url': next_url,
    }

    return render(request, "guia_marketing/guia_marketing_digital_page.html", context)


def detail_view(request, slug):
    obj = get_object_or_404(Capitulo, slug=slug)

    template_name = 'guia_marketing/detail.html'
    capitulos = Capitulo.objects.active()

    next_url = None
    next = capitulos.filter(slug=int(obj.slug) + 1)

    if len(next) == 1:
        next_url = next.first().get_absolute_url()

    context = {
        "object": obj,
        "capitulos": capitulos,
        "next_url": next_url,
    }

    return render(request, template_name, context)
