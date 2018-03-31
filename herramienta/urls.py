from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^detail/(?P<index>\d+)/$', views.details, name="tool_detail"),
    url(r'^$', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
