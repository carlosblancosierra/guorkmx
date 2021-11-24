from django.urls import path

from . import views

app_name = 'recursos'

urlpatterns = [

    path('', views.home_page, name="home"),
    path('<str:slug>', views.recurso_detail_view),
]
