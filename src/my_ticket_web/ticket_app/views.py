import json

from django.http import JsonResponse
from django.shortcuts import render
from . import models

# Create your views here.
from .biz import ticket_biz


def left_ticket_list(request):
    '''
    查询余票页面
    :param request:
    :return:
    '''
    # 所有车站信息，查询需要用到车站编码
    stations = models.TStation.objects.all().values()
    # 所有车票信息，暂时全部显示过去
    ticket_list = models.TLeftTicket.objects.all().values()

    resp = {'stations': stations, 'ticket_list': ticket_list}
    return render(request, 'ticket_app/left_ticket_list.html', resp)


def train_cout_hour(request):
    '''
    以小时为单位统计 每小时内车次数量
    :param request:
    :return:
    '''
    # 拿到全量数据，然后进行筛选，得到小时段的统计，先写死地点
    left_tickets = ticket_biz.get_last_ticket_list('合肥', '芜湖')
    # 最终统计数据 列表元素为 {hour:xx,count:xx}
    result = []

    # 0-23 统计每个小时区间的车次数量
    for hour in range(24):
        current_hour = {'hour': hour, 'count': 0}
        # 筛选 出发时间的小时段
        has_train_filter = filter(lambda x: int(x['start_time'].split(':')[0]) == hour, left_tickets)
        current_hour['count'] = len(list(has_train_filter))
        result.append(current_hour)

    resp = {'data': result}
    return JsonResponse(resp)
