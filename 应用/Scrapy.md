<!-- TOC -->

- [Scrapy](#scrapy)
    - [安装和环境](#安装和环境)
    - [开始项目](#开始项目)
    - [疑难杂症](#疑难杂症)
        - [Permission denied](#permission-denied)

<!-- /TOC -->


<a id="markdown-scrapy" name="scrapy"></a>
# Scrapy
Scrapy是一个纯Python语言实现的爬虫框架，简单、易用、拓展性高使得其成为Python爬虫中的主流利器。

> https://www.osgeo.cn/scrapy/

<a id="markdown-安装和环境" name="安装和环境"></a>
## 安装和环境
以 Anaconda 环境和 Pycharm 为例，由于 Scrapy 库依赖于其他的第三方库，


<a id="markdown-开始项目" name="开始项目"></a>
## 开始项目

```bash
scrapy startproject 项目名称
```

<a id="markdown-疑难杂症" name="疑难杂症"></a>
## 疑难杂症

<a id="markdown-permission-denied" name="permission-denied"></a>
### Permission denied

Anaconda Navigator 在 Environments 中进行安装 `Scrapy` ：

```
ERROR conda.core.link:_execute(481): An error occurred while uninstalling package 'defaults::conda-4.4.10-py36_0'.

PermissionError(13, 'Permission denied')
```

安装 `Scrapy` 框架时权限问题，用管理员权限打开 `Anaconda` 进行安装即可。


