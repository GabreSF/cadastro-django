from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, RegisterForm


def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'register.html', {'form': form})


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save()

        del(request.session['register_form_data'])
        return redirect(reverse('AppCadastro:login'))

    return redirect('AppCadastro:register')


def login_view(request):
    form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'form_action': reverse('AppCadastro:create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)
    login_url = reverse('AppCadastro:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você esta logado!')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Credenciais invalidas')
    else:
        messages.error(request, 'ERRO, valide o formulário novamente')
    return redirect(login_url)


@login_required(login_url='AppCadastro:login', redirect_field_name='next')
def logout_View(request):
    logout(request)
    return redirect(reverse('AppCadastro:login'))
