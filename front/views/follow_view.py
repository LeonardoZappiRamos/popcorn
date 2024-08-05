from django.urls import reverse
from django.http import HttpResponseRedirect    
def follow(request):
    next = request.GET.get('next')
    return HttpResponseRedirect(reverse(f"Home"))

def unfollow(request):
    next = request.GET.get('next')
    print(next)
    return reverse(f"front:home")