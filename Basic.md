<!-- TOC -->

- [Basic](#basic)
    - [输入输出](#输入输出)
    - [标准数据类型](#标准数据类型)
        - [Number（数字）](#number数字)
        - [String（字符串）](#string字符串)
        - [列表和元组](#列表和元组)
            - [通用序列操作](#通用序列操作)
            - [列表list](#列表list)
            - [元组tuple](#元组tuple)
        - [Sets（集合）](#sets集合)
        - [Dictionary（字典）](#dictionary字典)
    - [其他TODO](#其他todo)

<!-- /TOC -->

<a id="markdown-basic" name="basic"></a>
# Basic

<a id="markdown-输入输出" name="输入输出"></a>
## 输入输出
```python
name = input("input ur name:")
print("ur name is :" + name)
```

还有raw_input，todo

<a id="markdown-标准数据类型" name="标准数据类型"></a>
## 标准数据类型

<a id="markdown-number数字" name="number数字"></a>
### Number（数字）
Python3 支持 int、float、bool、complex（复数）。

```python
# 奇葩的赋值方式，对象依次赋值给变量，并且没有类型声明
a, b, c, d = 20, 5.5, True, 4+3j

# output：<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
print(type(a), type(b), type(c), type(d))

```

<a id="markdown-string字符串" name="string字符串"></a>
### String（字符串）
单引号或双引号表示字符串，`'`或`"`本身只是一种表示方式，不是字符串的一部分。
```python
'hello world'
"hello world"
```

转义字符`\`可以转义很多字符，比如`\n`表示换行，`\t`表示制表符，字符`\`本身也要转义，所以`\\`表示的字符就是`\`。

如果字符串里面有很多字符都需要转义，就需要加很多`\`，为了简化，Python还允许用`r''`表示`''`内部的字符串默认不转义。

```python
# 输出转义后的制表符
print('\t')

# 直接输出字符，不进行转义
print(r'\t')
```

多行字符串：Python允许用`'''...'''`的格式表示多行内容，或者表示区块代码的注释

```python
# 多行字符串
print('''
无题
锦瑟无端五十弦
''')
```


<a id="markdown-列表和元组" name="列表和元组"></a>
### 列表和元组
列表和元组都是序列的一种

列表`[]`很像JS里的数组，不限定元素的类型，并且是支持修改的。

元组`()`和列表不同之处在于，元组是不允许修改的。并且在支持的方法上也有一定的区分。

<a id="markdown-通用序列操作" name="通用序列操作"></a>
#### 通用序列操作
```python
# 列表list或元组tuple均支持以下操作
tags = [1, 2, 3, "hello", "world", True]

# 1.索引访问，同其他语言
print(tags[1])  # [2]

# 2.分片 [start:end] 不包含end索引

#   a)截取第2位，即索引为1
print(tags[1:2])  # [2]

#   b)截取最后一个元素
print(tags[-1:])  # [True]

#   c)利用分片进行复制list，因为list也是引用，直接赋值只是引用copy，可以通过分片[:]达到深度复制
tagsCopy = tags[:]
tagsCopy += [False]
print(tags)
print(tagsCopy)

# 3.序列相加，有些类似于拼接
print([1, 2, 3] + ["abc" + "xyz"])  # [1, 2, 3, 'abcxyz']

# 4.序列乘法，即原来的序列被重复N次
print(["repeat"] * 3)  # ['repeat', 'repeat', 'repeat']

# 5.检查元素是否在序列中，这里和js中的表示不一样
print("xyz" in ["abc", "xyz", "opq"])  # True
print("ll" in "hello")  # True

# 6.长度、最大、最小
nums = [9, 5, 2, 7]
print(len(nums))
print(max(nums))
print(min(nums))
```

<a id="markdown-列表list" name="列表list"></a>
#### 列表list
- 列表赋值，同js
- 删除元素，`del lst[index]`
- 

<a id="markdown-元组tuple" name="元组tuple"></a>
#### 元组tuple

<a id="markdown-sets集合" name="sets集合"></a>
### Sets（集合）

<a id="markdown-dictionary字典" name="dictionary字典"></a>
### Dictionary（字典）




<a id="markdown-其他todo" name="其他todo"></a>
## 其他TODO

Anaconda?