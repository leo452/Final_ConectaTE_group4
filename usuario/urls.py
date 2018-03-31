from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_rest, name='login'),
    url(r'^loginview$', views.login_view, name='loginview'),
    url(r'^crearusuario$', views.crear_usuario_rest , name='crearusuario'),
    url(r'^crearusuarioview$', views.crear_usuario ,name='crearusuarioview'),
    url(r'^getgroups', views.get_groups,name='getgroups'),
    url(r'^editarperfiles/', views.admin_edicion_perfiles, name="editarPerfiles"),
    url(r'^cambiagrupo/', views.admin_cambia_grupo)
    #url(r'^cambiaGrupo/(\d+)/(\d+)', views.admin_cambia_grupo)
]