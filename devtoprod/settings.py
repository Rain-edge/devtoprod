import os

# 安全密钥，生产环境需要换成真正的随机值
SECRET_KEY = 'django-insecure-devtoprod-learn-2026'

# 关闭调试模式（部署时用）
DEBUG = True

# 允许所有主机访问（开发环境用，生产环境要改成具体域名）
ALLOWED_HOSTS = ['*']

# 已安装的应用
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'myapp',  # ← 我们自己的应用
]

# 中间件（Django 处理请求的管道）
MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'devtoprod.urls'

# 最简模板配置（这个项目不用模板，保留即可）
TEMPLATES = []

# WSGI 入口
WSGI_APPLICATION = 'devtoprod.wsgi.application'

# 数据库配置（用 SQLite，最简单）
DATABASES = {}

# 静态文件配置
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
