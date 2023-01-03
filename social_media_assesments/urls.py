from django.urls import path

from . import views

app_name = 'social_media_assesments'

urlpatterns = [
    path('', views.assesment_page, name='home'),
    # path('landing', views.landing_page, name='landing'),
    path('results/', views.results_page, name='results'),

]
