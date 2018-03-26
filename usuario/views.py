from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, get_user_model, logout, update_session_auth_hash
from django.core import serializers
from django.http import Http404


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

@csrf_exempt
def login_rest(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        UserModel=get_user_model()
        try:
            usuario=UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            mensaje = 'Nombre de usuario o clave no valido'
            raise Http404(mensaje)
        else:
            if usuario.check_password(password):
                login(request, usuario)
                return HttpResponse(serializers.serialize("json", [usuario]))
            else:
                mensaje = 'Nombre de usuario o clave no valido'
                raise Http404(mensaje)


def login_view(request):
    return render(request, 'login.html')