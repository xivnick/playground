from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .forms import SignUpForm, LoginForm

from django.contrib.auth import views

views.auth_login

def login(req):
    if req.method == 'POST':
        login_form = LoginForm(req.POST)

        username = req.POST['username']
        password = req.POST['password']
        user = auth.authenticate(req, username=username, password=password)

        if user is not None:
            auth.login(req, user)

            print('[log]', username, 'login')

            return redirect('main_page')

        return render(req, 'account/login.html', {'form': login_form, 'failed': True})

    login_form = LoginForm()

    return render(req, 'account/login.html', {'form': login_form, 'failed': False})


def logout(req):
    user = req.user
    auth.logout(req)

    print('[log]', user, 'logout')

    return redirect('account_login')


def signup(req):

    if req.method == 'POST':
        signup_form = SignUpForm(req.POST)

        if signup_form.is_valid():

            user_instance = signup_form.save(commit=False)

            user_instance.set_password(signup_form.cleaned_data['password'])
            user_instance.last_name = signup_form.cleaned_data['first_name']

            user_instance.save()

            # 회원가입이 정상적으로 되었을때만
            return redirect('account_login')

    else:
        signup_form = SignUpForm()

    return render(req, 'account/signup.html', {'form': signup_form})
