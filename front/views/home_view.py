import requests
import json
from django.shortcuts import render


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
    token = request.session.get("token")
    if request.user.is_authenticated:
        posts = get_posts(token['access'])
        seguindo = get_seguidores(token['access'])
        context["posts"] = posts
        context["seguindo"] = seguindo
    return render(request, "front/home.html", context)
