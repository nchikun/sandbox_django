from django.conf.urls import url
from . import views

app_name = 'basic_practice_1'

urlpatterns = [
    # indexというビュー関数を作成する
    url(r'^$', views.index, name='index'),
]
