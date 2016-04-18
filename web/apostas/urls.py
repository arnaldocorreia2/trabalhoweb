from django.conf.urls import url
from .views import user_login
from django.conf.urls import include
from .views import exibir_partida
from .views import aposta_new
urlpatterns = [
    #url(r'^login/$', user_login, name='login'),
    url(r'^$', user_login, name='login'),
    url(r'^v1/(?P<partida_id>(\d+))/(?P<user_id>(\d+))/$', exibir_partida, name='exibir'),
    url(r'^aposta/new/$', aposta_new, name='aposta_new'),
]
