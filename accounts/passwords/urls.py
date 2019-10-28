# accounts.passwords.urls.py
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('contrasena/cambiar/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),

    path('contrasena/cambiar/completado/',
         auth_views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('contrasena/reiniciar/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('contrasena/reiniciar/solicitado/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    url(r'^contrasena/reiniciar/\
        (?P<uidb64>[0-9A-Za-z_\-]+)/\
        (?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    path('contrasena/reiniciar/completado/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
