from django.conf.urls import url

from . import views

#app_name = "timeNow"
urlpatterns = [
    url(r'^$', views.get, name='get'),
]