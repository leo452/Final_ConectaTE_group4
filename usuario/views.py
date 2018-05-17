from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import  login, get_user_model, logout
from django.core import serializers
from django.http import Http404
from django.contrib.auth.decorators import  user_passes_test
from django.contrib.auth.models import Group, User
from usuario.models import Usuario
from django.urls import reverse
from herramienta.models import Herramienta, HerramientaEdicion
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#servicio rest para autenticar un usuario
@csrf_exempt
def login_rest(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        UserModel=get_user_model()
        try:
            usuario=UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            mensaje = 'Nombre de usuario no valido'
            raise Http404(mensaje)
        else:
            if usuario.check_password(password):
                print("aqui no entra")
                login(request, usuario)
                return HttpResponse(serializers.serialize("json", [usuario]))
            else:
                mensaje = 'clave no valida'
                print(mensaje)
                raise Http404(mensaje)

#metodo encargado de renderizar la pantalla de login
def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

#servicio rest encargado de la creacion de un usuario
@csrf_exempt
def crear_usuario_rest(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        username= request.POST.get("username")
        first_name= request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        perfiles=request.POST.getlist("perfiles")
        proyectos = request.POST.get("proyectos")
        print(password)
        if Usuario.objects.filter(email=email).exists():
            mensaje = 'Email ya existe'
            raise Http404(mensaje)
        try:
            usuario = Usuario.objects.create(email=email, username=username, first_name=first_name,
                                             last_name=last_name, proyectos=proyectos)
            usuario.set_password(password)
            for perfil in perfiles:
                my_group = Group.objects.get(name=perfil)
                my_group.user_set.add(usuario)
            usuario.save()
            return HttpResponse(serializers.serialize("json", [usuario]))

        except Exception as e:
            raise Http404(e)

#servicio rest para acceder e los grupos/perfiles que estan creados en la base de datos
def get_groups(request):
    if request.method == 'GET':
        groups = Group.objects.all()
    return HttpResponse(serializers.serialize("json", groups))


# este metodo se usa para validar si un usuario esta autenticado y si es administrador
# esto para asegurar que pueda acceder paginas de administracion
# este metodo se unsa en la precondiocion @user_passes_test
def in_admin_group(user):
    group = Group.objects.get(name="Administrador")
    return True if group in user.groups.all() else False

#metodo renderizar la pantalla de creacion de usuario
#esta pantalla solo si un usuario con perfil de administrador esta autenticado
@user_passes_test(in_admin_group)
def crear_usuario(request):
    return render(request, 'crearUsuario.html')



# metodo para realizar paginacion para una vista. se esperan dos parametros query y paginas
# query recive el listado de objetos a paginas
# paginas recive el numero de objetos por pagina
# se retorna un areglo con todos los datos de paginacion para ser procedos en una vista
# este metodo esta ideado para ser usado en una vista que envie informacion como contexto a un html
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


# esta vista se accede al llamar /editarperfiles esta vista se encarga de prosesar la paginacion de los usuarios
# que se muestran en la pagina /editarperfiles.html
# esta vista se llama solamente desde /editarperfiles.html
def edicion_perfiles_list(request):
    if request.method == "GET":
        page = request.GET.get('page')
        user_li = User.objects.all().filter(is_staff=False)
        user_list = user_li.filter(groups__isnull=False)
        pag = Paginator(user_list, 10)

        try:
            user_pag = pag.page(page)
            page = int(str(page))
        except PageNotAnInteger:
            user_pag = pag.page(1)
            page = 1
        except EmptyPage:
            user_pag = pag.page(pag.num_pages)
            page = pag.num_pages

        #data = serializers.serialize('json', user_pag.object_list)
        data = serializers.serialize('json', user_pag)
        response = HttpResponse(data)

        if page < pag.num_pages:
            pagenext = str((int(page + 1)))
            response['next'] = "/usuario/editarperfilesview?" + \
                               "page=" + pagenext
        if page > 1:
            pageprevious = str((int(page - 1)))
            response['previous'] = "/usuario/editarperfilesview?" + \
                                   "page=" + pageprevious
        response['numpages'] = pag.num_pages
        return response

    #grupos = Group.objects.all()
    #user_list = Usuario.objects.all()
    #pag = paginator(request, user_list, 10)
    #cxt = {
    #    'user_pag': pag['queryset'],
    #    'user_list': user_list,
    #    'paginator': pag,
    #    'grupos': grupos
    #}
    #return render(request, 'editarperfiles.html', cxt)


# esta vista se encaraga de mostraa la el html editarperfiles.html
# se adiciona una pre validacion antes de llamar esta vista para que esta solo pueda ser accedida por usuarios con
# perfil administrador
# @user_passes_test(in_admin_group, login_url='https://final-conectate-group4.herokuapp.com/usuario/loginview')
#@user_passes_test(in_admin_group, login_url='http://localhost:8000/usuario/loginview')
@user_passes_test(in_admin_group)
def edicion_perfiles_view(request):
    return render(request, 'editarperfiles.html')


# esta vista recive las peticiones del servicio /cambiagrupo y se encarga de recibir y actualizar el perfil de un
# usuario
# la vista espera dos parametros id y grupo
# id representa el id del usuario que se quiere actualizar
# grupo representa el id del nuevo grupo que al que se va a asociar al usuario
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


# esta vista se llama al aceder a /usuarios y retorna un JSON con el listado de Usuarios que se han Registrado en la
# aplicacion
def usuarios(request):
    if request.method == "GET":
        usuarios = Usuario.objects.all()
        return HttpResponse(serializers.serialize("json", usuarios))


# esta vista se llama al aceder a /grupos y retorna un JSON con el listado de grupos que se han creado en el modelo
# de autenticacion de DJango
def grupo(request, id):
    if request.method == "GET":
        user = get_object_or_404(Usuario, id=id)
        grupos = user.groups.all()
        return HttpResponse(serializers.serialize("json", grupos))


# esta vista se llama al aceder a /grupos y retorna un JSON con el listado de grupos que se han creado en el modelo
# de autenticacion de DJango
def grupos(request):
    if request.method == "GET":
        grupos = Group.objects.all()
        return HttpResponse(serializers.serialize("json", grupos))


# esta vista se llama al aceder a /edicionherramientas/uId
# donde uId es el ide del Usuario
# este metodo reorna un listado en formato JSON con todas las ediciones de herramientas
# en las que el usuario indicado ha trabajdo
def edicionherramientas(request, id):
    if request.method == "GET":
        user = get_object_or_404(Usuario, id=id)
        tools = HerramientaEdicion.objects.all().filter(usuarioHerramienta=user)
        return HttpResponse(serializers.serialize("json", tools))


# esta vista se llama al aceder a /usuarioherramientas/uId
# donde id es el id de un Usuario
# este metodo reorna un listado en formato JSON con todas las herramientas en las que el usuario indicado ha trabajdo
def usuarioHeramientas(request, id):
    user = get_object_or_404(Usuario, id=id)
    usuherramienta = Herramienta.objects.all().filter(owner=user)
    return HttpResponse(serializers.serialize("json", usuherramienta))


# esta vista se llama al aceder a /usuarioproyectos/uId
# donde id es el id de un Usuario
# este metodo reorna un listado en formato JSON con los proyectos que ha trabajado el usuario
def usuarioProyecto(request, id):
    user = get_object_or_404(Usuario, id=id)
    return HttpResponse(user.proyectos)


# esta vista se accede al llamar /usuarioherramienta esta vista se encarga de prosesar la paginacion de los usuarios
# que se muestran en la pagina /usuarioherramienta.html
# esta vista se llama solamente desde /usuarioherramienta.html
def usuario_herramienta_list(request):
    if request.method == "GET":
        page = request.GET.get('page')
        group = Group.objects.filter(name="MiembroGTI")#(name__in=["MiembroGTI", "Administrador"])
        user_list = User.objects.all().filter(groups__in=group)#.filter(is_staff=False)
        pag = Paginator(user_list, 10)

        try:
            user_pag = pag.page(page)
            page = int(str(page))
        except PageNotAnInteger:
            user_pag = pag.page(1)
            page = 1
        except EmptyPage:
            user_pag = pag.page(pag.num_pages)
            page = pag.num_pages

        #data = serializers.serialize('json', user_pag.object_list)
        data = serializers.serialize('json', user_pag)
        response = HttpResponse(data)

        if page < pag.num_pages:
            pagenext = str((int(page + 1)))
            response['next'] = "/usuario/usuarioherramientaview?" + \
                               "page=" + pagenext
        if page > 1:
            pageprevious = str((int(page - 1)))
            response['previous'] = "/usuario/usuarioherramientaview?" + \
                                   "page=" + pageprevious
        response['numpages'] = pag.num_pages
        return response

    #user_list = Usuario.objects.all()
    #pag = paginator(request, user_list, 10)
    #cxt = {
    #    'user_pag': pag['queryset'],
    #    'user_list': user_list,
    #    'paginator': pag
    #}
    #return render(request, 'usuarioherramienta.html', cxt)


# esta vista se encaraga de mostraa la el html usuarioherramienta.html
@user_passes_test(in_admin_group)
def usuario_herramienta_view(request):
    return render(request, 'usuarioherramienta.html')
