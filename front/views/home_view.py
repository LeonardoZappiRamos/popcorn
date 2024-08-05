import requests
import json
from django.shortcuts import render
from django.contrib import messages

def call_api(url, method="GET", header=None, body=None):
    match method:
        case "GET":
            response = requests.get(url, headers=header, data=body)
            content = json.loads(response.content)
        case "POST":
            response = requests.post(url, headers=header, data=body)
            content = json.loads(response.content)
        case _:
            response = None
    return content, response


def set_post(req, token, user, titulo, conteudo):
    url = "http://127.0.0.1:8000/api/v1/posts/"
    header = {"Authorization": f"Bearer {token['access']}"}
    body = {
        "usuario": user.id,
        "titulo": titulo,
        "conteudo": conteudo
    }
    
    data, res = call_api(url, method="POST", header=header, body=body)
    
    if res.status_code == 201:
        messages.add_message(req, messages.SUCCESS, "Operação realizada com sucesso")
    else:
        messages.add_message(req, messages.WARNING, data['message'])
    
    
def get_posts(req, token):
    url = "http://127.0.0.1:8000/api/v1/posts/"
    print(token)
    header = {
        "Authorization": f"Bearer {token['access']}"
    }
    data, res = call_api(url, header=header)
    
    if res == 400:
        refresh_data, refresh_res = call_api("http://127.0.0.1:8000/auth/token/refresh/", method="POST", body={"refresh": token['refresh']})
        print(refresh_data, refresh_res)
        if refresh_res.status_code == 200:
            req.session["token"] = {"access": refresh_data['access']}
        new_token = {"access": refresh_data['access']}
        content, status = call_api(url, header={"Authorization": f"Bearer {new_token}"})
        return content, refresh_data
    return data

def get_seguidores(req, token):
    url = "http://127.0.0.1:8000/api/v1/seguidor/"
    header = {
        "Authorization": f"Bearer {token['access']}"
    }
    data, res = call_api(url, header=header)

    if res == 400:
        refresh_data, refresh_res = call_api("http://127.0.0.1:8000/auth/token/refresh/", method="POST", body={"refresh": token['refresh']})
        print(refresh_data, refresh_res)
        if refresh_res.status_code == 200:
            req.session["token"] = refresh_data['access']
        new_token = refresh_data['access']
        content, status = call_api(url, header={"Authorization": f"Bearer {new_token}"})
        return content, refresh_data
    return data  
    
def home(request):
    context = {}
    token = request.session.get("token", None)
    
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")
        set_post(request, token['access'], request.user, titulo, conteudo)
        
    if request.user.is_authenticated:
        if token is not None:
            posts = get_posts(request, token)
            seguindo = get_seguidores(request, token)
            context["posts"] = posts
            context["seguindo"] = seguindo
            
    return render(request, "front/home.html", context)
