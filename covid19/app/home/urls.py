from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'md$', views.boot, name='bootstrap'),
]