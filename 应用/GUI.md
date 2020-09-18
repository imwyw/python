<!-- TOC -->

- [GUI](#gui)
  - [tkinter](#tkinter)
  - [打包](#打包)
    - [pyinstaller](#pyinstaller)

<!-- /TOC -->

<a id="markdown-gui" name="gui"></a>
# GUI

<a id="markdown-tkinter" name="tkinter"></a>
## tkinter

<a id="markdown-打包" name="打包"></a>
## 打包

<a id="markdown-pyinstaller" name="pyinstaller"></a>
### pyinstaller

首先需要在【anaconda navigator】中安装 pyinstaller，常用的参数用法:

```
--distpath <path>: 打包到哪个目录下
-w: 指定生成 GUI 软件，也就是运行时不打开控制台
-c: 运行时打开控制台
-i <Icon File>: 指定打包后可执行文件的图标
--clean: 在构建之前清理PyInstaller缓存并删除临时文件
```

关于打包成什么样，有两种选择：

```
-D: 创建包含可执行文件的单文件夹包，同时会有一大堆依赖的 dll 文件，这是默认选项
-F: 只生成一个 .exe 文件，如果项目比较小的话可以用这个，但比较大的话就不推荐
```

比如：

```
pyinstaller --distpath Release/ -w -i x.ico --clean main.py
```


