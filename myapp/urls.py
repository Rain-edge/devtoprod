from django.urls import path
from . import views

urlpatterns = [
    # 当用户访问首页（""）时，调用 views.index 函数
    path('', views.index, name='index'),
]
