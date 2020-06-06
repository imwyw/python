<!-- TOC -->

- [Selenium](#selenium)
    - [安装](#安装)
    - [基础](#基础)
        - [关键字搜索](#关键字搜索)
        - [猫扑首页](#猫扑首页)

<!-- /TOC -->


<a id="markdown-selenium" name="selenium"></a>
# Selenium

Selenium with Python中文翻译文档

> https://selenium-python-zh.readthedocs.io/en/latest/index.html

<a id="markdown-安装" name="安装"></a>
## 安装
命令：
```bash
pip install selenium
```

安装 Chrome 对应的 Chromedriver 工具：

> http://chromedriver.storage.googleapis.com/index.html
> http://npm.taobao.org/mirrors/chromedriver/


<a id="markdown-基础" name="基础"></a>
## 基础

模拟浏览器打开动作，并显示页面文档内容：

```python
from selenium import webdriver  # 从selenium导入webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')  # 获取百度页面
html = driver.page_source
print(html)

# 可以应用 find_element_xxx 定位元素，如id,name,xpath,link_text等等
```

<a id="markdown-关键字搜索" name="关键字搜索"></a>
### 关键字搜索

模拟打开页面，并输入关键字进行搜索，在上述案例的基础上添加代码：

```python
from selenium import webdriver  # 从selenium导入webdriver
import time

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')  # 获取百度页面

input_element = driver.find_element_by_id('kw')
input_element.send_keys('python')  # 输入python

search_btn = driver.find_element_by_id('su')  # 找到按钮

search_btn.click()
time.sleep(5) # 等待5s

#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 滚动至底部
html = driver.page_source # 页面文档
print(html)
```

<a id="markdown-猫扑首页" name="猫扑首页"></a>
### 猫扑首页

```python
import time
from bs4 import BeautifulSoup
import pymysql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 异常模块
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 使用selenium打开浏览器并访问地址
driver = webdriver.Chrome()
# 猫扑网
driver.get('https://www.mop.com/')

try:
    # 等待直到内容加载出来
    wait = WebDriverWait(driver, 10)
    # 等待加载
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "content-flow")))

    # 下翻5次
    # for i in range(5):
    #     time.sleep(5)  # 等待5秒
    #     # 翻到底部加载更多内容
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    list = soup.select('div.bottom-rel-item')
    print(list)

except Exception as e:
    print(e)
finally:
    driver.quit()

```

















