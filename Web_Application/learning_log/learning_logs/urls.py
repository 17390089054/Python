#定义learning_logs的url模式
from django.conf.urls import url

from . import views

urlpatterns=[
        #主页
        url(r'^$',views.index,name='index'),
    ]
