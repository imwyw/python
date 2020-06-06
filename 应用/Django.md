<!-- TOC -->

- [Django](#django)
    - [概要和环境](#概要和环境)
        - [第一个页面](#第一个页面)
    - [模板Templates](#模板templates)
        - [render](#render)
    - [Models模块](#models模块)
    - [应用模块](#应用模块)
        - [应用目录结构](#应用目录结构)
        - [应用页面和url](#应用页面和url)

<!-- /TOC -->

<a id="markdown-django" name="django"></a>
# Django
Django作为一个Python的高级Web框架，功能非常强大，其自身封装了大量底层逻辑，并实现了ORM，

同时， MVT 结构保证了代码结构的完整性，这一切给了开发人员巨大的便利，让Web开发变得高效且简洁。

> https://docs.djangoproject.com/zh-hans/3.0/

<a id="markdown-概要和环境" name="概要和环境"></a>
## 概要和环境

```bash
django-admin startproject 项目名称
```

【manage.py】 与项目交互的命令行工具集入口，项目管理器

执行 python manage.py 查看所有命令

```bash
python manage.py runserver
```

【wsgi.py】 python web server gateway interface ，python服务器网关接口，很少修改

【urls.py】 URL配置，访问url需要进行配置

【settings.py】包含数据库、web应用、时间等配置

【__init__.py】声明模块的文件

<a id="markdown-第一个页面" name="第一个页面"></a>
### 第一个页面

在【项目名称】文件夹中添加 【views.py】 处理文件，用于处理请求并响应

```py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello django!')
```

在同目录文件 【urls.py】 中添加路由信息：

```py
from django.conf.urls import url
from django.contrib import admin

# 引入当前目录文件
from . import views

# 第一个参数是正则匹配，第二个参数是对应的处理函数，第三个参数是名称
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
]
```

在 PyCharm Terminal 终端中输入运行命令： `python manage.py runserver 端口号`

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py runserver 5000
```

在浏览器中访问url即可： http://127.0.0.1:5000/index/  或者 http://localhost:5000/index/

<a id="markdown-模板templates" name="模板templates"></a>
## 模板Templates
- HTML文件，DTL（Django Template Language）模板语言
- 

<a id="markdown-render" name="render"></a>
### render
在【Templates】目录中创建HTML文件，在【views.py】处理请求方法中返回 `render()` 

【templates/index.html】

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello index page</title>
</head>
<body>
<h1>hello django main page  {{ site_name }}</h1>

</body>
</html>
```

修改【项目名称/views.py】中请求处理：

```py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # 第一个参数是 请求上下文对象，第二个是静态文件，第三个是字典值 传参
    return render(request, 'index.html', {'site_name': '知乎'})
```

<a id="markdown-models模块" name="models模块"></a>
## Models模块
通常，一个 Model 对应数据库的一张数据表

Django 中 Models 以`类`的形式出现，包含了基本字段和数据的行为。

ORM，对象关系映射 Object Relation Mapping，实现了对象和数据库的映射。

项目文件夹内创建 【models.py】，继承 `models.Model`

<a id="markdown-应用模块" name="应用模块"></a>
## 应用模块

打开 `cmd` 命令行，进入项目中 【manage.py】 统计目录

输入： `python manage.py startapp 应用名称` ，应用名称不能重复

添加应用名到 【settings.py】 中 `INSTALLED_APPS` 里

<a id="markdown-应用目录结构" name="应用目录结构"></a>
### 应用目录结构

```
migrations
    __init__.py
__init__.py
admin.py
apps.py
models.py
tests.py
views.py
```

- migrations 数据迁移模块
- admin.py 应用后台管理系统配置，Django自带后台管理系统
- apps.py 应用配置，Django-1.9后版本才有
- models.py 数据模型，使用ORM框架
- tests.py 自动化测试模块，Django提供了自动化测试
- views.py 执行响应的逻辑代码

<a id="markdown-应用页面和url" name="应用页面和url"></a>
### 应用页面和url

在 PyCharm Terminal 终端中输入运行命令： `python manage.py startapp blog`

创建应用【blog】，同样的在 【blog/views.py】 中添加请求处理方法如下：

```py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def main(request):
    return HttpResponse('this is blog view!')
```

添加应用中的urls配置，新增文件【blog/urls.py】，路由规则如下：

```py
from django.conf.urls import url
from django.contrib import admin

# 引入当前目录文件
from . import views

# 用法有点类似于 Vue 的嵌套路由 访问url需要结合根url，localhost:5000/blog/index 
urlpatterns = [
    url(r'^index/$', views.main)
]
```

在根urls中添加配置，修改【项目名称/urls.py】文件，新增引入 include 支持

```py
from django.conf.urls import url, include
from django.contrib import admin

# 引入当前目录文件
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls'))
]
```
















