from django.urls import path, include

urlpatterns = [
    # 所有以 "" 开头的请求，都交给 myapp 去处理
    path('', include('myapp.urls')),
]
