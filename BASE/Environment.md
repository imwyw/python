<!-- TOC -->

- [环境及配置](#环境及配置)
  - [Anaconda](#anaconda)
    - [环境变量](#环境变量)
    - [Channels源设置](#channels源设置)
    - [pip安装](#pip安装)
    - [多个python路径的pip管理](#多个python路径的pip管理)
  - [pycharm](#pycharm)
  - [其他](#其他)
    - [PermissionError](#permissionerror)
    - [AnacondaNavigator打开无响应](#anacondanavigator打开无响应)

<!-- /TOC -->

<a id="markdown-环境及配置" name="环境及配置"></a>
# 环境及配置
<a id="markdown-anaconda" name="anaconda"></a>
## Anaconda

Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。

可以用于在同一个机器上安装不同版本的软件包及其依赖，并能够在不同的环境之间切换。

* Anaconda Navigator ：用于管理工具包和环境的图形用户界面，后续涉及的众多管理命令也可以在 Navigator 中手工实现。
* Jupyter notebook ：基于web的交互式计算环境，可以编辑易于人们阅读的文档，用于展示数据分析的过程。
* qtconsole ：一个可执行 IPython 的仿终端图形界面程序，相比 Python Shell 界面，qtconsole 可以直接显示代码生成的图形，实现多行代码输入执行，以及内置许多有用的功能和函数。
* spyder ：一个使用Python语言、跨平台的、科学运算集成开发环境。

安装完成即已经有了python环境，如下图命令提示符中可见：

![](../assets/Environment/anaconda-python.png)

官网地址：
> https://www.anaconda.com/

历史版本-清华镜像
> https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

<a id="markdown-环境变量" name="环境变量"></a>
### 环境变量

Windows下anaconda3的安装非常简单，但是如果 anaconda 没有写入环境变量路径，就会导致我们在命令行中输入诸如 conda list 之类的命令时会报错。

这就需要我们手动设置【系统环境变量 】，【此电脑】-【属性】-【高级系统设置】-【环境变量】-【系统变量】-【Path】编辑

![](../assets/Environment/系统环境变量.png)

<a id="markdown-channels源设置" name="channels源设置"></a>
### Channels源设置
Anaconda 默认从国外镜像源下载，而从国外下载速度极慢，容易导致报错。

清华大学经与 Anaconda, Inc. 沟通，获得了镜像的授权，因此我们又能使用清华大学的镜像了。

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --set show_channel_urls yes
```

参考引用：

> https://blog.csdn.net/wsjzzcbq/article/details/101052960

<a id="markdown-pip安装" name="pip安装"></a>
### pip安装
升级pip：

```cmd
python -m pip install --upgrade pip
```

手动指定源进行python库的安装：

下例为安装 xlwings 库，并修改默认超时时间100秒

```cmd
pip --default-timeout=100 install xlwings -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

<a id="markdown-多个python路径的pip管理" name="多个python路径的pip管理"></a>
### 多个python路径的pip管理

比如已有Anaconda环境，单独安装纯净的python环境，如何基于纯净的python环境进行pip包的管理？

假设当前系统已有Anaconda-python环境，并且环境变量设置为Anaconda，在cmd中直接使用

关键在于使用单独安装python路径下的【scripts/pip.exe】文件：

```cmd
C:\Users\Administrator>D:\Python36_pack\Scripts\pip install pyyaml

C:\Users\Administrator>D:\Python36_pack\Scripts\pip --default-timeout=100 install xlwings -i https://pypi.tuna.tsinghua.edu.cn/simple/
-------------------------------------------------------------------
Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple/
Collecting pyinstaller
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/82/96/21ba3619647bac2b34b4996b2dbbea8e74a703767ce24192899d9153c058/pyinstaller-4.0.tar.gz (3.5 MB)
     |████████████████████████████████| 3.5 MB 64 kB/s
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
    Preparing wheel metadata ... done
Collecting altgraph
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/ee/3d/bfca21174b162f6ce674953f1b7a640c1498357fa6184776029557c25399/altgraph-0.17-py2.py3-none-any.whl (21 kB)
Collecting pefile>=2017.8.1; sys_platform == "win32"
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/36/58/acf7f35859d541985f0a6ea3c34baaefbfaee23642cf11e85fe36453ae77/pefile-2019.4.18.tar.gz (62 kB)
     |████████████████████████████████| 62 kB 397 kB/s
Collecting pywin32-ctypes>=0.2.0; sys_platform == "win32"
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/9e/4b/3ab2720f1fa4b4bc924ef1932b842edf10007e4547ea8157b0b9fc78599a/pywin32_ctypes-0.2.0-py2.py3-none-any.whl (28 kB)
Requirement already satisfied: setuptools in d:\python36_pack\lib\site-packages (from pyinstaller) (39.0.1)
Collecting pyinstaller-hooks-contrib>=2020.6
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/d8/c8/78cbee6bb0337b723cd57c11924566026fb7762f9999abccca3ccd0b8651/pyinstaller_hooks_contrib-2020.8-py2.py3-none-any.whl (159 kB)
     |████████████████████████████████| 159 kB 2.2 MB/s
Collecting future
  Downloading https://pypi.tuna.tsinghua.edu.cn/packages/45/0b/38b06fd9b92dc2b68d58b75f900e97884c45bedd2ff83203d933cf5851c9/future-0.18.2.tar.gz (829 kB)
     |████████████████████████████████| 829 kB 111 kB/s
Using legacy 'setup.py install' for pefile, since package 'wheel' is not installed.
Using legacy 'setup.py install' for future, since package 'wheel' is not installed.
Building wheels for collected packages: pyinstaller
  Building wheel for pyinstaller (PEP 517) ... done
  Created wheel for pyinstaller: filename=pyinstaller-4.0-py3-none-any.whl size=2789243 sha256=f04925e500d089503aceeb1a4c63f390fbff29752a93a4b2748e66b7f4d59223
  Stored in directory: c:\users\administrator\appdata\local\pip\cache\wheels\d1\12\69\37daf1688a0c60785e1ec8dfa864aa56e16a94cd3c5e316ae0
Successfully built pyinstaller
Installing collected packages: altgraph, future, pefile, pywin32-ctypes, pyinstaller-hooks-contrib, pyinstaller
    Running setup.py install for future ... done
    Running setup.py install for pefile ... done
  WARNING: The scripts pyi-archive_viewer.exe, pyi-bindepend.exe, pyi-grab_version.exe, pyi-makespec.exe, pyi-set_version.exe and pyinstaller.exe are installed in 'd:\python36_pack\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed altgraph-0.17 future-0.18.2 pefile-2019.4.18 pyinstaller-4.0 pyinstaller-hooks-contrib-2020.8 pywin32-ctypes-0.2.0

```

使用指定的python环境进行执行python脚本：

```cmd
D:\Python36_pack\FinanceAnalysis>D:\Python36_pack\python ui.py
```

基于指定的python环境进行pyinstaller打包：

```cmd
D:\Python36_pack\FinanceAnalysis>D:\Python36_pack\Scripts\pyinstaller -w --clean ui.py
-----------------------------------
148 INFO: PyInstaller: 4.0
148 INFO: Python: 3.6.5
148 INFO: Platform: Windows-10-10.0.18362-SP0
152 INFO: wrote D:\Python36_pack\FinanceAnalysis\ui.spec
155 INFO: UPX is not available.
155 INFO: Removing temporary files and cleaning cache in C:\Users\Administrator\AppData\Roaming\pyinstaller
158 INFO: Extending PYTHONPATH with paths
['D:\\Python36_pack\\FinanceAnalysis', 'D:\\Python36_pack\\FinanceAnalysis']
173 INFO: checking Analysis
173 INFO: Building Analysis because Analysis-00.toc is non existent
174 INFO: Initializing module dependency graph...
178 INFO: Caching module graph hooks...
194 INFO: Analyzing base_library.zip ...
3771 INFO: Caching module dependency graph...
3844 INFO: running Analysis Analysis-00.toc
3848 INFO: Adding Microsoft.Windows.Common-Controls to dependent assemblies of final executable
  required by d:\python36_pack\python.exe
4440 INFO: Analyzing D:\Python36_pack\FinanceAnalysis\ui.py
4865 INFO: Processing pre-find module path hook distutils from 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks\\pre_find_module_path\\hook-distutils.py'.
4867 INFO: distutils: retargeting to non-venv dir 'd:\\python36_pack\\lib'
4967 INFO: Processing pre-safe import module hook win32com from 'd:\\python36_pack\\lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\pre_safe_import_module\\hook-win32com.py'.
6950 INFO: Processing module hooks...
6950 INFO: Loading module hook 'hook-pythoncom.py' from 'd:\\python36_pack\\lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
7478 INFO: Loading module hook 'hook-pywintypes.py' from 'd:\\python36_pack\\lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
7976 INFO: Loading module hook 'hook-win32com.py' from 'd:\\python36_pack\\lib\\site-packages\\_pyinstaller_hooks_contrib\\hooks\\stdhooks'...
7980 INFO: Loading module hook 'hook-distutils.py' from 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks'...
7982 INFO: Loading module hook 'hook-encodings.py' from 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks'...
8272 INFO: Loading module hook 'hook-xml.py' from 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks'...
8494 INFO: Loading module hook 'hook-_tkinter.py' from 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks'...
9045 INFO: checking Tree
9045 INFO: Building Tree because Tree-00.toc is non existent
9046 INFO: Building Tree Tree-00.toc
9085 INFO: checking Tree
9085 INFO: Building Tree because Tree-01.toc is non existent
9085 INFO: Building Tree Tree-01.toc
9109 INFO: Looking for ctypes DLLs
9189 WARNING: library coredll required via ctypes not found
9198 INFO: Analyzing run-time hooks ...
9201 INFO: Including run-time hook 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_multiprocessing.py'
9204 INFO: Including run-time hook 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth_win32comgenpy.py'
9208 INFO: Including run-time hook 'd:\\python36_pack\\lib\\site-packages\\PyInstaller\\hooks\\rthooks\\pyi_rth__tkinter.py'
9215 INFO: Looking for dynamic libraries
9656 INFO: Looking for eggs
9656 INFO: Using Python library d:\python36_pack\python36.dll
9657 INFO: Found binding redirects:
[]
9665 INFO: Warnings written to D:\Python36_pack\FinanceAnalysis\build\ui\warn-ui.txt
9710 INFO: Graph cross-reference written to D:\Python36_pack\FinanceAnalysis\build\ui\xref-ui.html
9774 INFO: checking PYZ
9774 INFO: Building PYZ because PYZ-00.toc is non existent
9775 INFO: Building PYZ (ZlibArchive) D:\Python36_pack\FinanceAnalysis\build\ui\PYZ-00.pyz
10459 INFO: Building PYZ (ZlibArchive) D:\Python36_pack\FinanceAnalysis\build\ui\PYZ-00.pyz completed successfully.
10476 INFO: checking PKG
10477 INFO: Building PKG because PKG-00.toc is non existent
10477 INFO: Building PKG (CArchive) PKG-00.pkg
10514 INFO: Building PKG (CArchive) PKG-00.pkg completed successfully.
10520 INFO: Bootloader d:\python36_pack\lib\site-packages\PyInstaller\bootloader\Windows-64bit\runw.exe
10520 INFO: checking EXE
10520 INFO: Building EXE because EXE-00.toc is non existent
10520 INFO: Building EXE from EXE-00.toc
10521 INFO: Appending archive to EXE D:\Python36_pack\FinanceAnalysis\build\ui\ui.exe
10543 INFO: Building EXE from EXE-00.toc completed successfully.
10553 INFO: checking COLLECT
10553 INFO: Building COLLECT because COLLECT-00.toc is non existent
10554 INFO: Building COLLECT COLLECT-00.toc
22122 INFO: Building COLLECT COLLECT-00.toc completed successfully.
```

这样打出来的程序包，仅仅是基于指定的python环境，会小很多。

<a id="markdown-pycharm" name="pycharm"></a>
## pycharm
PyCharm是一种Python IDE，带有一整套可以帮助用户在使用Python语言开发时提高其效率的工具，

比如调试、语法高亮、Project管理、代码跳转、智能提示、自动完成、单元测试、版本控制。

下载Community社区版本即可，因为Free Community

下载地址：

>https://www.jetbrains.com/pycharm/download/#section=windows

hello python

![](../assets/Environment/pycharm-hello.png)


<a id="markdown-其他" name="其他"></a>
## 其他

<a id="markdown-permissionerror" name="permissionerror"></a>
### PermissionError
pip或者interpreter安装包时发生错误：

`PermissionError: [Errno 13] Permission denied: 'C:\\ProgramData\\Anaconda3\\pkgs\\cache\\2116b818.json'`

<a id="markdown-anacondanavigator打开无响应" name="anacondanavigator打开无响应"></a>
### AnacondaNavigator打开无响应

```cmd
:: 先更新pip
python -m pip install --upgrade pip

pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple

:: pip安装超时问题-pip._vendor.urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out.
pip --default-timeout=100 install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
```


