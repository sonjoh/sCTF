from django.urls import path
from . import views


# URLConf
urlpatterns = [
    path('', views.challs),
    path('dbtest/', views.dbtest),
    path('<int:id_value>/', views.challs_id)
]