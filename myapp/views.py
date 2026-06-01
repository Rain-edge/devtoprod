from django.http import HttpResponse


def index(request):
    """这是我们的第一个视图函数：返回一行文本"""
    return HttpResponse("Hello from DevToProd! 🚀 我的第一个 Django 应用成功运行了！")
