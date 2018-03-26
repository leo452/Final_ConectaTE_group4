from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core import serializers
from django.http import Http404


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

@csrf_exempt
def login_rest(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        print(user)
    if user is not None:
        login(request,user)
        return HttpResponse(serializers.serialize("json", [user]))
    else:
        mensaje= 'Nombre de usuario o clave no valido'
        raise Http404(mensaje)


def login_view(request):
    return render(request, 'login.html')