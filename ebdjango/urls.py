"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from accounts.views import login_page, register_page, register_page_local
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('inbound', views.inbound_page, name='inbound'),
    path('contacto', views.contact_page, name='contact'),
    path('nosotros', views.nosotros_page, name='nosotros'),

    path('auditoria_landing/', views.audit_landing_page, name='audit_lp'),
    path('auditoria_pre/', views.audit_pre_page, name='audit_pre'),
    path('auditoria/', views.audit_page, name='audit'),
    path('auditoria/resultado/', views.audit_result_page, name='audit_result'),

    path('guia_marketing_digital', views.guia_marketing_digital, name='guia_marketing_digital'),

    path('eventos', views.events_list_page, name='events'),
    path('reserva_un_experto', views.experts_list_page, name='experts'),
    path('audio_visual', views.audio_visual_page, name='audio_visual'),

    path('soluciones', views.soluciones_page, name='soluciones'),
    path('soluciones/programas_estrategicos', views.programas_estrategicos_page, name='programas_estrategicos'),
    path('soluciones/soporte_tactico', views.soporte_tactico_page, name='soporte_tactico'),
    path('soluciones/proyectos', views.proyectos_page, name='proyectos'),

    path('recursos', views.recursos_page, name='recursos'),

    path('admin/', admin.site.urls),

    path('blog/', include('blog.urls')),
    path('workshops/', include('courses.urls')),
    path('checkout/', include('stripe_checkout.urls')),

    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page_local, name='register'),
    path('cuenta/', include('accounts.urls')),
    path('cuenta/', include('accounts.passwords.urls')),

    path('aviso-de-privacidad', views.aviso_de_privacidad_page, name='aviso_de_privacidad'),

    # third party
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
