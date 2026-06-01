from django.http import HttpResponse


def index(request):
    """这是我们的第一个视图函数：返回一行文本"""
    return HttpResponse("Hello from DevToProd! 🚀 这是通过 CI/CD 自动部署的版本！")
