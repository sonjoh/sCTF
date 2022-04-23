from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static


from . import views



# URLConf
urlpatterns = [
    path('make-chall/', views.make_chall),
    path('edit-chall/', views.edit_chall),
    path('upload', views.upload),
    path('', views.admin_panel),
    path('settings', views.admin_settings),
    path('setup', views.admin_setup),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)