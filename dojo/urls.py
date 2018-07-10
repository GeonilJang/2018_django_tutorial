#blog/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    #^시작 $끝
    url(r'^$', views.myfun),
    url(r'^(?P<a>\d+)/(?P<b>\d+)/$', views.myfun, name="myfun"),


]
