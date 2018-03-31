from django.conf.urls import url
import  views

#las url que inician con api son las correspondientes a los servicios GET Y POST de herramientas utilizando REST
#las demas url son las pantallas html de los formularios
urlpatterns = [
    url(r'^api/categorias/$', views.ListCategorias.as_view(), name='categoria'),
    url(r'^api/categoria/form/$', views.addCategoria, name='categoria-form'),
    url(r'^api/categoria/form/(?P<id>\d+)/$', views.editCategoria, name='categoria-form-edit'),
    url(r'^api/revisiones/$', views.ListRevisiones.as_view(), name='revision'),
    url(r'^api/revisiones/form/$', views.addRevision, name='revision-form'),
    url(r'^api/revisiones/form/(?P<id>\d+)/$', views.editRevision, name='revision-form-edit'),
    url(r'^api/herramientas/$', views.ListHerramienta.as_view(), name='herramienta'),
    url(r'^api/herramientas/form/$', views.addHerramienta, name='herramienta-form'),
    url(r'^api/herramientas/form/(?P<id>\d+)/$', views.editHerramienta, name='herramienta-form-edit'),
    url(r'^api/edicion/$', views.ListHerramientaEdicion.as_view(), name='edicion'),
    url(r'^api/edicion/form/$', views.addHerramientaEdicion, name='edicion-form'),
    url(r'^api/edicion/form/(?P<id>\d+)/$', views.editHerramientaEdicion, name='edicion-form-edit'),
    url(r'^categoria/add/$', views.addCategoriaView, name='categoria-v'),
    url(r'^lista/$', views.listHerramienta, name='herramientas'),
    url(r'^herramienta/add/$', views.addHerramientaView, name='herramienta-v'),
    url(r'^herramienta/edit/(?P<id>\d+)/$', views.editHerramientaView, name='herramienta-edit'),
    url(r'^listaedicion/$', views.listRevisiones, name='ediciones'),
    url(r'^edicion/add/$', views.addRevisionView, name='ediciones-v'),
   # url(r'^edicion/edit/(?P<id>\d+)/$', views.editRevisionView, name='ediciones-edit'),
    url(r'^revision/add/$', views.addRevisionEstadoView, name='revision-v'),
]