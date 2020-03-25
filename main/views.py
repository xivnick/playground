from django.shortcuts import render


def main(req):
    return render(req, 'main/main.html', {})


def login(req):
    return render(req, 'main/login.html', {})