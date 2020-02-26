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

from .views import (
    home_page,
    inbound_page,
    contact_page,
    audit_landing_page,
    audit_pre_page,
    audit_page,
    audit_result_page,
    events_list_page,
    experts_list_page,
    audio_visual_page,
    soluciones_page,
    programas_estrategicos_page,
    nosotros_page,
)

urlpatterns = [
    path('', home_page, name='home'),
    path('inbound', inbound_page, name='inbound'),
    path('contacto', contact_page, name='contact'),
    path('blog/', include('blog.urls')),
    path('nosotros', nosotros_page, name='nosotros'),

    path('auditoria_landing/', audit_landing_page, name='audit_lp'),
    path('auditoria_pre/', audit_pre_page, name='audit_pre'),
    path('auditoria/', audit_page, name='audit'),
    path('auditoria/resultado/', audit_result_page, name='audit_result'),

    path('eventos', events_list_page, name='events'),
    path('reserva_un_experto', experts_list_page, name='experts'),
    path('audio_visual', audio_visual_page, name='audio_visual'),

    path('soluciones', soluciones_page, name='soluciones'),
    path('soluciones/programas_estrategicos', programas_estrategicos_page, name='programas_estrategicos'),

    path('admin/', admin.site.urls),

    path('workshops/', include('courses.urls')),
    path('checkout/', include('stripe_checkout.urls')),

    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page_local, name='register'),
    path('cuenta/', include('accounts.urls')),
    path('cuenta/', include('accounts.passwords.urls')),

    # third party
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
