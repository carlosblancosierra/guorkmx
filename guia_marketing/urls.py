from django.urls import path

from . import views

app_name = 'guia_marketing_digital'

urlpatterns = [
    path('', views.guia_marketing_digital, name="home"),
    path('<str:slug>', views.detail_view),
]
