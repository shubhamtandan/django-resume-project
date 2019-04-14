from django.conf.urls import url
from test_app import views


app_name = "test_app"

urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]
