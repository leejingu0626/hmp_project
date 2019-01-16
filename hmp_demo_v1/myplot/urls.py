from django.conf.urls import url
from . import views
from .views import data_json

urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.upload_file),
    url(r'^upload/$', views.upload_file_to_html),
    url(r'data_json/$', views.data_json, name='data_json'),
]