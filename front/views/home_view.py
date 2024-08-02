import requests
import json
from django.shortcuts import render
from django.contrib import messages


def set_post(req, token, user, titulo, conteudo):
    url = "http://127.0.0.1:8000/api/v1/posts/"
    header = {
        "Authorization": f"Bearer {token}"
    }
    body = {
        "usuario": user.id,
        "titulo": titulo,
        "conteudo": conteudo
    }
    res = requests.post(url, headers=header, data=body)
    data = json.loads(res.content)
    if res.status_code > 299:
        messages.add_message(req, messages.WARNING, data['message'])
    else:
        messages.add_message(req, messages.SUCCESS, "Post Criado")
    
def get_posts(token):
    url = "http://127.0.0.1:8000/api/v1/posts/"
    header = {
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(url, headers=header)
    return json.loads(res.content)

def get_seguidores(token):
    url = "http://127.0.0.1:8000/api/v1/seguidor/"
    header = {
        "Authorization": f"Bearer {token}"
    }
    res = requests.get(url, headers=header)
    return json.loads(res.content)  
    
def home(request):
    context = {}
    if request.method == "POST":
        token = request.session.get("token", None)
        titulo = request.POST.get("titulo")
        conteudo = request.POST.get("conteudo")
        set_post(request, token['access'], request.user, titulo, conteudo)
        print(request.user, titulo, conteudo)
        #print(titulo, conteudo)
        
    if request.user.is_authenticated:
        token = request.session.get("token", None)
        if token is not None:
            posts = get_posts(token['access'])
            seguindo = get_seguidores(token['access'])
            context["posts"] = posts
            context["seguindo"] = seguindo
    return render(request, "front/home.html", context)
