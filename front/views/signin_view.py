from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth
from django.contrib import messages
import requests
import json 


def set_user(username, password, email):
    url = "http://127.0.0.1:8000/api/v1/users/"
    body = {
        "email": email,
        "username": username,
	    "password": password
    }
    res = requests.post(url, body)
    data = json.loads(res.content) 
    return data, res.status_code

def signin(request):
    context = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user, status = set_user(username, password, email)
        if status < 300:
            messages.add_message(request, messages.SUCCESS, "Usuário Criado")
            return redirect('Login')
        else:
            messages.add_message(request, messages.ERROR, user['message'])
    return render(request, "front/login.html", context)
