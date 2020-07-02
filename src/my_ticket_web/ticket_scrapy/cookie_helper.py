def get_cookie_dict():
    # 从文本中读取cookie信息
    with open('./ticket_scrapy/cookie.txt') as f:
        cookie_string = f.readline()

    # 定义 cookie 字典
    cookie_dict = {}
    # cookie 字符串中每对 key-value 以分号分隔
    cookie_array = cookie_string.split(';')
    for cookie_item in cookie_array:
        # 以等号拆分，取出 key 和 value 对应的值
        item_key = cookie_item.split('=')[0].replace(' ', '')
        item_value = cookie_item.split('=')[1]
        cookie_dict[item_key] = item_value

    return cookie_dict
