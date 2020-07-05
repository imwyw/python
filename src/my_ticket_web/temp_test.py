print('非必须文件，仅仅进行一些临时脚本测试。。。。')

stus = [
    {'name': 'jack', 'age': 12},
    {'name': 'lucy', 'age': 1},
    {'name': 'smith', 'age': 2},
    {'name': 'tony', 'age': 19},
    {'name': 'tom', 'age': 21},
]

ff = filter(lambda x: x['age'] > 18, stus)
ll = list(ff)
print(len(ll))
