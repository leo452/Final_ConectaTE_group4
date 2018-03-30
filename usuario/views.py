from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, get_user_model, logout, update_session_auth_hash
from django.core import serializers
from django.http import Http404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from usuario.models import Usuario
from herramienta.models import HerramientaEdicion
from django.core.paginator import Paginator


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

@csrf_exempt
def crear_usuario_rest(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        username= request.POST.get("username")
        first_name= request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        perfiles=request.POST.getlist("perfiles")

        if Usuario.objects.filter(email=email).exists():
            mensaje = 'Email ya existe'
            raise Http404(mensaje)
        try:
            usuario = Usuario.objects.create(email=email, password=password, username=username, first_name=first_name,
                                             last_name=last_name)
            for perfil in perfiles:
                my_group = Group.objects.get(name=perfil)
                my_group.user_set.add(usuario)
            usuario.save()
            return HttpResponse(serializers.serialize("json", [usuario]))

        except Exception as e:
            raise Http404(e)






@csrf_exempt
def get_groups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
    return HttpResponse(serializers.serialize("json", groups))

def crear_usuario(request):
    return render(request, 'crearUsuario.html')

def in_admin_group(user):
    return user.is_authenticated() and 'Admin' in user.groups.iterator()


def paginator(request, query, paginas):
    result_list = Paginator(query, paginas)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1

    if page <= 0:
        page = 1

    if page > result_list.num_pages:
        page = result_list.num_pages

    if result_list.num_pages >= page:
        pagina = result_list.page(page)
        context= {
            'queryset': pagina.object_list,
            'page': page,
            'pages': result_list.num_pages,
            'has_next': pagina.has_next(),
            'has_prev': pagina.has_previous(),
            'next_page': page+1,
            'prev_page': page-1,
            'firstPage': 1,
        }
        return context


#@user_passes_test(in_admin_group, login_url='usuario/loginview')
def admin_edicion_perfiles(request):
    grupos = Group.objects.all()
    user_list = Usuario.objects.all()
    pag = paginator(request, user_list, 10)
    cxt = {
        'user_pag': pag['queryset'],
        'user_list': user_list,
        'paginator': pag,
        'grupos': grupos
    }
    return render(request, 'editarperfiles.html', cxt)

@csrf_exempt
def admin_cambia_grupo(request):
    if request.method == 'POST':
        id = int(request.POST.get("id"))
        uGrupo = int(request.POST.get("grupo"))
        user = get_object_or_404(Usuario, id=id)
        group = get_object_or_404(Group, id=uGrupo)

        user_group = Usuario.groups.through.objects.get(user=user)
        user_group.group = group
        user_group.save()

        return HttpResponse("actualizado",content_type="text/plain")


def usuarios(request):
    usuarios = Usuario.objects.all()
    return HttpResponse(serializers.serialize("json", usuarios))

def usuarioHeramientas(request, uId):
    usuherramienta = HerramientaEdicion.objects.all().filter(usuarioHerramienta = uId)
    return HttpResponse(serializers.serialize("json", usuherramienta))


def admin_ver_usuario_herramienta(request):
    user_list = Usuario.objects.all()
    pag = paginator(request, user_list, 10)
    cxt = {
        'user_pag': pag['queryset'],
        'user_list': user_list,
        'paginator': pag
    }
    return render(request, 'usuarioherramienta.html', cxt)


