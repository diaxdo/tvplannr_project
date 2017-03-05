from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^plannr$', views.plannr),
    url(r'^create_account$', views.create_account),
    url(r'^log_in$', views.log_in),
]
