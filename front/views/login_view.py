from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_auth
from django.contrib import messages
import requests
import json 

def get_token(username, passwork):
    url = "http://127.0.0.1:8000/auth/token/"
    body = {
        "username": username,
	    "password": passwork
    }
    res = requests.post(url, body)
    data = json.loads(res.content) 
    return data
    
    
def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if  user is not None:
            token = get_token(username, password)
            request.session["token"] = token
            login_auth(request, user)
            return redirect('Home')
        else:
            messages.add_message(request, messages.ERROR, "Usuário ou Senha inválidos")
    return render(request, "front/login.html", context)
