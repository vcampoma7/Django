from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^flights$', views.flights2, name='flights'),
    url(r'^flights/(?P<departure>.*)/$', views.flights2, name='flights'),
    #url(r'^flights/(?P<d>\w+)(?P<departure>)$', views.flights2, name='flights'),
    url(r'^shoppingcart/$', views.shoppingcart, name='shoppingcart'),
    url(r'^buy/$', views.buy, name='buy'),
]