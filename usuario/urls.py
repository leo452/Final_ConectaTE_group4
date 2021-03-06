from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_rest, name='login'),
    url(r'^loginview$', views.login_view, name='loginview'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^crearusuario$', views.crear_usuario_rest , name='crearusuario'),
    url(r'^crearusuarioview$', views.crear_usuario ,name='crearusuarioview'),
    url(r'^getgroups', views.get_groups,name='getgroups'),
    url(r'^editarperfiles$', views.edicion_perfiles_list),
    url(r'^editarperfilesview/', views.edicion_perfiles_view, name="editarPerfilesview"),
    url(r'^cambiagrupo/', views.admin_cambia_grupo, name="cambiarGrupo"),
    url(r'^usuarios/', views.usuarios),
    url(r'^grupos/', views.grupos),
    url(r'^grupo/(?P<id>\d+)', views.grupo),
    url(r'^usuarioproyectos/(?P<id>\d+)', views.usuarioProyecto),
    url(r'^usuarioherramientas/(?P<id>\d+)', views.usuarioHeramientas),
    url(r'^usuarioherramientaview/', views.usuario_herramienta_view, name="usuarioherramientaview"),
    url(r'^usuarioherramienta$', views.usuario_herramienta_list),
    url(r'^edicionherramientas/(?P<id>\d+)', views.edicionherramientas)
]