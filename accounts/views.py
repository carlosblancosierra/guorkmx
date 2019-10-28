# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from ebdjango.decorators import check_recaptcha
from django.contrib import messages
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AccountHomeView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/home.html'

    def get_object(self):
        return self.request.user


def login_page(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form,
        "title": "Iniciar Sesión",
    }

    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None

    if form.is_valid():
        print('form is valid')

        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if is_safe_url(redirect_path, request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")

        else:
            # Return an 'invalid login' error message
            print("error")
            messages.error(request, 'Error')
    else:
        print("form is not valid")

    return render(request, "accounts/login.html", context)


User = get_user_model()


@check_recaptcha
def register_page(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form,
        "title": "Registro",

    }

    if form.is_valid():

        if request.recaptcha_is_valid:
            print(form.cleaned_data)
            name = form.cleaned_data.get('name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            new_user = User.objects.create_user(username, email, password, first_name=name, last_name=last_name)
            messages.success(request, 'Se a creado exitosamente el usuario')
            login(request, new_user)
            return redirect("carts:home")
        else:
            messages.error(request, 'La verificación de Google ha fallado, por favor envié sus datos otra vez')
            return redirect("/")

    return render(request, "accounts/register.html", context)


def register_page_local(request):
    form = RegisterForm(request.POST or None)

    context = {
        "form": form,
        "title": "Registro Local",
    }

    if form.is_valid():
        print(form.cleaned_data)
        email = form.cleaned_data.get('email')
        password = form.clean_password2()
        new_user = User.objects.create_user(email, password=password)
        messages.success(request, 'Se a creado exitosamente el usuario')
        login(request, new_user)
        return redirect("home")
    else:
        messages.error(request, 'Error')

    return render(request, "accounts/register-local.html", context)
