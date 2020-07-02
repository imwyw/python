from django.shortcuts import render
from . import models


# Create your views here.
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
