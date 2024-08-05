import requests
import json
from django.shortcuts import render


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


def get_users(req, token):
    url = "http://127.0.0.1:8000/api/v1/users/"
    header = {
        "Authorization": f"Bearer {token}"
    }
    data, status = call_api(url, header=header)
    return data


def users(request):
    token = request.session.get("token", None)
    users = get_users(request, token["access"])
    
    context = {
        "users": users
    }
    return render(request, "front/users.html", context)