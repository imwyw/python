<!-- TOC -->

- [Django](#django)
    - [概要和环境](#概要和环境)
        - [第一个页面](#第一个页面)
    - [应用模块](#应用模块)
        - [应用目录结构](#应用目录结构)
        - [应用页面和url](#应用页面和url)
    - [模板Templates](#模板templates)
        - [render](#render)
        - [应用下的render](#应用下的render)
    - [Models模块](#models模块)
        - [数据的呈现](#数据的呈现)
    - [Admin](#admin)
        - [创建用户](#创建用户)
        - [配置models](#配置models)
    - [Django调试](#django调试)
    - [博客设计](#博客设计)
        - [博客主页](#博客主页)
        - [博客详情](#博客详情)
        - [链接跳转](#链接跳转)
        - [发表博客](#发表博客)
        - [修改博客](#修改博客)
        - [Templates过滤器](#templates过滤器)
        - [Admin增强](#admin增强)

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

【`__init__.py`】声明模块的文件

<a id="markdown-第一个页面" name="第一个页面"></a>
### 第一个页面

在【项目名称】文件夹中添加 【views.py】 处理文件，用于处理请求并响应

```py
from django.http import HttpResponse

def index(request):
    return HttpResponse('hello django!')
```

在同目录文件 【urls.py】 中添加路由信息：

```py
from django.contrib import admin
from django.urls import path

# 引入当前目录文件
from . import views

# 第一个参数是正则匹配，第二个参数是对应的处理函数，第三个参数是名称
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
```

在 `PyCharm Terminal` 终端中输入运行命令： `python manage.py runserver 端口号`

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py runserver 5000
```

在浏览器中访问url即可： http://127.0.0.1:5000/index/  或者 http://localhost:5000/index/


<a id="markdown-应用模块" name="应用模块"></a>
## 应用模块

打开 `cmd` 命令行，进入项目中 【manage.py】 同级目录

或者直接在 `pycharm terminal` 终端窗口中操作：

输入： `python manage.py startapp 应用名称` ，应用名称不能重复

然后，添加应用名到 【settings.py】 中 `INSTALLED_APPS` 里

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blogs'#添加应用的名称
]
```

这样，新添加的应用才会起作用。

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

创建应用后，在应用文件夹下会自动生成对应的 【blog/views.py】 文件

新增处理方法 `main(request)` 

```py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def main(request):
    return HttpResponse('this is blog view!')
```

添加应用中的 `urls` 配置，新增文件【blog/urls.py】，路由规则如下：

```py
from django.urls import path
from django.contrib import admin

# 引入当前目录文件
from . import views

# 用法有点类似于 Vue 的嵌套路由 访问url需要结合根url配置，localhost:5000/blog/index 
urlpatterns = [
    path('index/', views.main)
]
```

在根 `urls` 中添加配置，修改【项目名称/urls.py】文件，导入 `include` 方法

```py
from django.conf.urls import url, include
from django.contrib import admin

# 引入当前目录文件
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
```

<a id="markdown-模板templates" name="模板templates"></a>
## 模板Templates
- HTML文件，DTL（Django Template Language）模板语言

<a id="markdown-render" name="render"></a>
### render
在根路径下创建【templates】目录，用于存放前端页面文件

在【views.py】处理请求方法中通过 `render()` 返回对应的前端页面

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

如果显示 `TemplateDoesNotExist at /index/` 问题，因为 Django 3.0 创建模板没有配置默认的 `Template DIR`

修改配置【settings.py】中的 TEMPLATES 配置项：

```py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

<a id="markdown-应用下的render" name="应用下的render"></a>
### 应用下的render

前面创建 `blog` 应用，也可以渲染静态页面，创建应用 `blog` 对应【templates/blog】文件夹，在该文件夹中新建HTML

【templates/blog/main.html】

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello blog main</title>
</head>
<body>
<h1>博客主页-- {{ site_name }}</h1>

</body>
</html>
```

修改 【blog/views.py】 中请求处理方法如下：

```py
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def main(request):
    return render(request, 'blog/main.html', {'site_name': '博客园'})
```


<a id="markdown-models模块" name="models模块"></a>
## Models模块
通常，一个 Model 对应数据库的一张数据表

Django 中 Models 以`类`的形式出现，包含了基本字段和数据的行为。

ORM，对象关系映射 Object Relation Mapping，实现了对象和数据库的映射。

在应用 blog 文件夹内 【models.py】用于描述实体信息，继承 `models.Model` ，代码如下：

```py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='标题')
    content = models.TextField()
```

如上，定义了一个文章类，通过命令 `python manage.py makemigrations app名（可选）`

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0001_initial.py
    - Create model Article

```

再执行命令 `python manage.py migrate`

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0001_initial... OK

```

Django 会在 【blog/migrations】 目录下生成移植文件，如 【0001_initial.py】

执行 `python manage.py sqlmigrate 应用名称 文件id` 查看对应SQL语句

```py
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py sqlmigrate blog 0001
BEGIN;
--
-- Create model Article
--
CREATE TABLE "blog_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(32) NOT NULL, "content" text NOT NULL);
COMMIT;

```

默认 sqlite3 的数据库在项目根目录下 【db.sqlite3】

可以使用 Navicat 或者 SqliteExpertPersonal 工具打开管理数据库文件。


<a id="markdown-数据的呈现" name="数据的呈现"></a>
### 数据的呈现

【blog/views.py】中 `import models`

```py
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def main(request):
    # 根据主键信息查询对象，也可以根据字段 title或者content获取 
    # models.Article.objects.get(title='xxx')
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/main.html', {'article': article})
```

前端HTML页面的调整，【blog/main.html】

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello blog main</title>
</head>
<body>
<h1>博客主页-- 知乎</h1>
<hr>

<h3>{{ article.title }}</h3>
<h3>{{ article.content }}</h3>

</body>
</html>
```


<a id="markdown-admin" name="admin"></a>
## Admin
Admin 是 Django 自带的一个功能强大的自动化数据管理界面

被授权的用户可以直接在 Admin 中管理数据库

Django 提供了许多针对Admin的定制功能

<a id="markdown-创建用户" name="创建用户"></a>
### 创建用户
创建用户 `python manage.py createsuperuser` 创建超级用户

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py createsuperuser
Username (leave blank to use 'now_w'): admin
Email address: abc@python.com
Password:
Password (again):
Superuser created successfully.

```

密码不能太简单，不少于8个字符，推荐使用简单好记密码 `Admin@123`

管理页面入口 `localhost:端口号/admin` ，就像配置路由器一样

切换中文版显示，修改 【settings.py】文件中 `LANGUAGE_CODE='zh_Hans'`

注意，Django-2.0+版本的配置有调整： `LANGUATE_CODE='zh-hans'`

<a id="markdown-配置models" name="配置models"></a>
### 配置models

在应用下【admin.py】中引入自身的models模块，使用 `admin.site.register()` 注册模块即可

修改【blog/admin.py】文件

```py
from django.contrib import admin
from . import models

# Register your models here.
# 注册Article，使用Admin管理Article数据
admin.site.register(models.Article)
```

以上，便可以通过 Admin 模块对应用下创建的数据进行简单的增删改查。

如要切换 Admin 界面显示标题，可以修改 【blog/models.py】，增加 `def __str__(self)`

```py
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32, default='标题')
    content = models.TextField()

    def __str__(self):
        return self.title
```

<a id="markdown-django调试" name="django调试"></a>
## Django调试

用 `PyCharm` 开发 `django` 程序的时候，对于打印日志调试程序的方式感觉还是有点麻烦和不直观，在IDE中调试方法如下：

* 打开你的工程，在菜单栏里找到Run-->Edit Configurations

![](../assets/Django/DebugEditConfig.png)

* 脚本选择你网站的manage.py，脚本参数用runserver，跟平常用命令行是一样的

![](../assets/Django/DebugParameter.png)

之后在菜单栏里找到 `Run-->Debug'debug'` ，运行后，你能在Console中看到服务器已经运行起来了，有日志打印

然后就可以通过断点开始调试了。

<a id="markdown-博客设计" name="博客设计"></a>
## 博客设计

* 博客主页页面，标题（超链接）列表，发表博客按钮
* 博客内容页面
* 编辑博客页面

<a id="markdown-博客主页" name="博客主页"></a>
### 博客主页
设计思路：

1. 取出数据库中所有文章对象
2. 将文章对象打包成列表，传递到前端
3. 前端页面显示所有文章（超链接显示标题）

修改应用 blog 处理请求代码【blog/views.py】：

```py
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

# 博客主页
def main(request):
    # 获取所有数据信息，返回列表
    articles = models.Article.objects.all()
    return render(request, 'blog/main.html', {'articles': articles})
```

修改对应的HTML模板页面【templates/blog/main.html】

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello blog main</title>
</head>
<body>
<h1>
    <a href="">发表新文章</a>
</h1>

{% for article in articles %}
    <h3><a href="">{{ article.title }}</a></h3>
{% endfor %}

</body>
</html>
```

<a id="markdown-博客详情" name="博客详情"></a>
### 博客详情

新增一个请求处理方法，修改【blog/views.py】代码：

```py
from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

# 博客主页
def main(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/main.html', {'articles': articles})


# 博客详情界面
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})
```

创建对应的前端 HTML 页面，新增【templates/blog/article_page.html】：

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>博客内容</title>
</head>
<body>
<h1>{{ article.title }}</h1>
<hr>
<h3>{{ article.content }}</h3>
<br><br>

<a href="">修改</a>
</body>
</html>
```

增加 url 配置，修改【blog/urls.py】文件：

```py
from django.conf.urls import url
from django.contrib import admin

# 引入当前目录文件
from . import views

# 用法有点类似于 Vue 的嵌套路由
urlpatterns = [
    url(r'^index/$', views.main),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page),# P<article_id>[0-9]+ 正则匹配数字
]
```

通过正则匹配参数（此处方式比较老旧，基于 `Django-1.11` 版本，新版本使用 `Path` 方法要方便很多）

测试访问，最后 1 为传参，在请求方法 `def article_page(request, article_id):` 方法中根据 `article_id` 获取对应对象信息：

> localhost:5000/blog/article/1

<a id="markdown-链接跳转" name="链接跳转"></a>
### 链接跳转

template 中DTL可以使用 `{% url 'app_name:url_name' param %}`

`app_name` 和 `url_name` 都是在 【urls.py】中配置

`app_name` 是应用名称，在根urls中通过 `include` 配置的命名空间 `namespace`

`url_name` 是应用中urls配置的名称

配置根urls 【项目名称/urls.py】：

```py
from django.conf.urls import url, include
from django.contrib import admin

# 引入当前目录文件
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^blog/', include(('blog.urls', 'blog'), namespace='blog'))
]
```

增加了 `namespace` `的配置，include` 第一个参数为元组，配置应用 `urls` 和 `app_name` 

配置应用下的urls，【blog/urls.py】：

```py
from django.conf.urls import url
from django.contrib import admin

# 引入当前目录文件
from . import views

# 用法有点类似于 Vue 的嵌套路由
urlpatterns = [
    url(r'^index/$', views.main),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),  # P<article_id>[0-9]+ 正则匹配数字
]
```

设置前端HTML页面，【templates/blog/main.html】

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>hello blog main</title>
</head>
<body>
<h1>
    <a href="">发表新文章</a>
</h1>

<hr>
{% for article in articles %}
    <h3>
        <a href="{% url 'blog:article_page' article.id %}">{{ article.title }}</a>
    </h3>
{% endfor %}

</body>
</html>
```

<a id="markdown-发表博客" name="发表博客"></a>
### 发表博客

* 标题和内容输入
* 提交按钮
* 后端获取数据并保存数据库

新增编辑的页面，需要包含标题和内容等博客信息，创建HTML文件【templates/blog/edit_article.html】:

```py
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>发表帖子</title>
</head>
<body>
<form action="{% url 'blog:save_article' %}" method="post">
    {% csrf_token %}
    <fieldset>
        <label for="">文章标题</label>
        <input type="text" name="title"/>
    </fieldset>
    <fieldset>
        <label for="">文章内容</label>
        <input type="text" name="content">
    </fieldset>
    <fieldset>
        <input type="submit" value="提交">
    </fieldset>
</form>
</body>
</html>
```

`form` 表单的 `action` 属性设置了对应的处理方法，对应到应用中【views.py】处理逻辑

新增应用下处理请求的方法 `def edit_article(request)` 和 `def save_article(request)`，修改【blog/views.py】：

```py
# 编辑页面
def edit_article(request):
    return render(request, 'blog/edit_article.html')


# 保存操作
def save_article(request):
    # request.POST.get('key','defaultvalue') 获取前端表单post的值，如果没有则使用默认值
    title = request.POST.get('title', '默认标题')
    content = request.POST.get('content', '默认内容')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'blog/main.html', {'articles': articles})
```

在应用 urls 下增加配置，修改【blog/urls.py】：

```py
urlpatterns = [
    url(r'^index/$', views.main),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),  # P<article_id>[0-9]+ 正则匹配数字
    url(r'^edit$', views.edit_article, name='edit_article'),
    url(r'^save$', views.save_article, name='save_article')
]
```

TODO，以上还有个bug，添加博客文章保存后刷新会重复添加数据

<a id="markdown-修改博客" name="修改博客"></a>
### 修改博客

考虑到修改页面和新增页面大部分都是重复的内容，我们需要复用页面。

修改【templates/blog/edit_article.html】：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>发表帖子</title>
</head>
<body>
<form action="{% url 'blog:save_article' %}" method="post">
    {% csrf_token %}
    {% if article.id %}
        <h1>更新博客</h1>
    {% else %}
        <h1>新增博客</h1>
    {% endif %}

    <input type="hidden" name="article_id" value="{{ article.id }}">
    <fieldset>
        <label for="">文章标题</label>
        <input type="text" name="title" value="{{ article.title }}"/>
    </fieldset>
    <fieldset>
        <label for="">文章内容</label>
        <input type="text" name="content" value="{{ article.content }}">
    </fieldset>
    <fieldset>
        <input type="submit" value="提交">
    </fieldset>
</form>
</body>
</html>
```

修改【blog/views.py】编辑页面方法 `def edit_article(request):`

```py
# 编辑页面
def edit_article(request, article_id):
    article = None
    # 通过列表编辑进入
    if str(article_id) != '0':
        article = models.Article.objects.get(pk=article_id)
    else:
        article = {'id': 0}
    
    return render(request, 'blog/edit_article.html', {'article': article})
```

`edit_article` 方法区分新增还是修改的业务，通过判断请求的传参进行区分

修改【blog/views.py】编辑页面方法 `def save_article(request):`

```py
# 保存操作
def save_article(request):
    # request.POST.get('key','defaultvalue') 获取前端表单post的值，如果没有则使用默认值
    title = request.POST.get('title', '默认标题')
    content = request.POST.get('content', '默认内容')
    # 新增时，默认 article_id 是没有值的
    article_id = request.POST.get('article_id', '0')

    if article_id == '':  # 新增业务
        models.Article.objects.create(title=title, content=content)
    else:  # 更新业务
        entity = models.Article.objects.get(pk=article_id)
        entity.title = title
        entity.content = content
        entity.save()

    articles = models.Article.objects.all()
    return render(request, 'blog/main.html', {'articles': articles})
```

保存方法也需要针对新增和修改进行区分

最后修改urls配置，edit入口复用新增和修改的业务，修改路由配置【blog/urls.py】：

```py
urlpatterns = [
    url(r'^index/$', views.main),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),  # P<article_id>[0-9]+ 正则匹配数字
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_article, name='edit_article'),
    url(r'^save/$', views.save_article, name='save_article')
]
```

<a id="markdown-templates过滤器" name="templates过滤器"></a>
### Templates过滤器

`{{ value | filter }}`

为模版过滤器提供参数的方式是：过滤器后加个冒号，再紧跟参数，中间不能有空格！


例如为变量提供一个默认值，当 `article.id` 为空的时候 取默认值 `value`

`{{ article.id | default:'value' }}`

博客案例新增业务，当判断为新增业务时，回传前端的对象id设置可以完全在前端处理

注释掉【blog/views.py】 `edit_article` 方法中设置默认id部分

```py
# 编辑页面
def edit_article(request, article_id):
    article = None
    # 通过列表编辑进入
    if str(article_id) != '0':
        article = models.Article.objects.get(pk=article_id)
    # else:  # 新增业务时，需要标记对象id为0
    #     article = {'id': 0}
    return render(request, 'blog/edit_article.html', {'article': article})
```

并在前端页面通过 `default` 过滤器设置新增业务的默认值，修改【templates/blog/edit_article.html】

表单中隐藏域的 `value` 增加默认过滤器，当新增业务时，提交的 `article.id` 为0

```html
<input type="hidden" name="article_id" value="{{ article.id | default:0 }}">
```


更多的过滤器请参考：

> https://www.liujiangblog.com/course/django/147

<a id="markdown-admin增强" name="admin增强"></a>
### Admin增强
创建 admin配置类

class ArticleAdmin(admin.ModelAdmin)

显示其他字段， `list_display = ('title', 'content')`

`list_display` 同时支持 元组tuple和列表list，但是元素内容必须是字符串

修改应用下【blog/admin.py】

```py
from django.contrib import admin
from . import models


class ArticleAdmin(admin.ModelAdmin):
    # 设置管理界面显示字段
    list_display = ('title', 'content', 'pub_time')


# Register your models here.

# 注册Article，使用Admin管理Article数据
admin.site.register(models.Article, ArticleAdmin)
```

使用 `makemigrations` 和 `migrate` 执行数据迁移更新：

```bash
(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py makemigrations
Migrations for 'blog':
  blog\migrations\0002_article_pub_time.py
    - Add field pub_time to article

(C:\ProgramData\Anaconda3) D:\Codes\Py\hello_dj>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying blog.0002_article_pub_time... OK

```

重新 runserver ，观察 admin 管理页面










----


https://blog.csdn.net/weixin_42134789/article/details/80276855

