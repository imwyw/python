import operator
from functools import reduce

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from . import models


# Create your views here.
# 显示新闻列表
def show_news_list(request):
    # TODO 对新闻列表进行筛选，根据用户输入的信息实现filter，比如查询 教务处 发布的所有新闻
    # models.AiitNews.objects.filter(author__contains='教务处')
    condition_title = request.POST.get('condition_title', '')
    condition_author = request.POST.get('condition_author', '')
    condition_start_date = request.POST.get('start_date', '')
    condition_end_date = request.POST.get('end_date', '')

    # 构建查询参数列表，用于动态条件的查询
    query_condition = []

    '''
    这个查询，and 关系，对应的sql：
    SELECT * from aiit_news where
    title like '%学校%' and author like '%教务处%'
    '''
    # result = models.AiitNews.objects.filter(
    #     title__contains=condition_title,
    #     author__contains=condition_author
    # )

    # 使用 Q 对象的方式实现查询
    # result = models.AiitNews.objects.filter(
    #     Q(title__contains=condition_title),
    #     Q(author__contains=condition_author)
    # )

    if condition_title != '':
        q_dict = {'title__contains': condition_title}
        query_condition.append(Q(**q_dict))
    if condition_author != '':
        q_dict = {'author__contains': condition_author}
        query_condition.append(Q(**q_dict))
    if condition_start_date != '':
        q_dict = {'pub_date__gte': condition_start_date}
        query_condition.append(Q(**q_dict))
    if condition_end_date != '':
        q_dict = {'pub_date__lte': condition_end_date}
        query_condition.append(Q(**q_dict))

    # 动态查询，实现多条件的组合筛选
    result = models.AiitNews.objects.filter(reduce(operator.and_, query_condition))

    return render(request, 'news/show_news_list.html', {'data': result})


# 处理客户端传过来的数据，并添加至数据表
def save_action(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    summary = request.POST.get('summary')
    author = request.POST.get('author')
    pub_date = request.POST.get('pub_date')

    # 新增业务时，表单传递的id为空字符串
    if id == '':
        models.AiitNews.objects.create(
            title=title,
            summary=summary,
            author=author,
            pub_date=pub_date
        )
    else:
        entity = models.AiitNews.objects.get(id=id)
        entity.title = title
        entity.summary = summary
        entity.author = author
        entity.pub_date = pub_date
        entity.save()

    return redirect(show_news_list)


# 新增和更新业务复用页面
# def edit_view(request): 利用 url 拼接param参数方式进行传递，request.GET.get('xxx') 进行获取
def edit_view(request, id, title):
    # id = request.GET.get('id')
    print('==' * 50)
    print(id, title)
    entity = None
    if id:
        entity = models.AiitNews.objects.get(pk=id)

    return render(request, 'news/edit_view.html', {'data': entity})


def ajax_view(request):
    return render(request, 'news/ajax_view.html')


# 以数据为核心的操作，返回的是 字典值对应的 json 字符串
def ajax_data(request):
    condition_title = request.POST.get('condition_title', '')
    condition_author = request.POST.get('condition_author', '')
    condition_start_date = request.POST.get('start_date', '')
    condition_end_date = request.POST.get('end_date', '')

    # 构建查询参数列表，用于动态条件的查询
    query_condition = []

    if condition_title != '':
        q_dict = {'title__contains': condition_title}
        query_condition.append(Q(**q_dict))
    if condition_author != '':
        q_dict = {'author__contains': condition_author}
        query_condition.append(Q(**q_dict))
    if condition_start_date != '':
        q_dict = {'pub_date__gte': condition_start_date}
        query_condition.append(Q(**q_dict))
    if condition_end_date != '':
        q_dict = {'pub_date__lte': condition_end_date}
        query_condition.append(Q(**q_dict))

    # 动态查询，实现多条件的组合筛选
    if len(query_condition) == 0:
        result = models.AiitNews.objects.all().values()
    else:
        result = models.AiitNews.objects.filter(reduce(operator.and_, query_condition)).values()
    # 构造一个字典，将queryset查询结果转换为列表
    resp = {'data': list(result)}
    # 通过 JsonResponse 转字典值为 json 字符串，在前面进行反序列化为对象
    return JsonResponse(resp)
