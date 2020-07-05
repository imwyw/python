from collections import namedtuple

from django.db import connection


def get_last_ticket_list(from_name, dest_name):
    '''
    查询最近一次爬取到的 A-B 余票信息
    TODO 此处暂未考虑车票哪一天的。。。。
    :param from_name: 模糊匹配出发地名称
    :param dest_name: 模糊匹配到达地名称
    :return: 返回list
    '''
    sql = '''
    SELECT
	a.id,
	a.query_time,
	a.train_no,
	a.train_code,
	start_st.station_code start_code,
	start_st.full_name start_name,
	end_st.station_code end_code,
	end_st.full_name end_name,
	from_st.station_code from_code,
	from_st.full_name from_name,
	dest_st.station_code to_code,
	dest_st.full_name to_name,
	a.start_time,
	a.arrive_time,
	a.run_time,
	a.gr_num,
	a.rw_num,
	a.rz_num,
	a.tz_num,
	a.wz_num,
	a.yw_num,
	a.yz_num,
	a.edz_num,
	a.ydz_num,
	a.swz_num,
	a.dw_num
FROM
	t_left_ticket a
LEFT JOIN t_station start_st ON a.start_station_code = start_st.station_code
LEFT JOIN t_station end_st ON a.end_station_code = end_st.station_code
LEFT JOIN t_station from_st ON a.from_station_code = from_st.station_code
LEFT JOIN t_station dest_st ON a.dest_station_code = dest_st.station_code
WHERE
	can_buy != 'IS_TIME_NOT_BUY'
AND from_st.full_name LIKE %s
AND dest_st.full_name LIKE %s
AND query_time =(
	SELECT
		query_time
	FROM
		t_left_ticket
	WHERE
		1 = 1
	AND from_st.full_name LIKE %s
	AND dest_st.full_name LIKE %s
	GROUP BY
		query_time
	ORDER BY
		query_time DESC
	LIMIT 1
)
    '''
    param_from_name = '%' + from_name + '%'
    param_dest_name = '%' + dest_name + '%'
    with connection.cursor() as cursor:
        cursor.execute(sql, (param_from_name, param_dest_name, param_from_name, param_dest_name))
        # result = namedtuplefetchall(cursor)
        result = dictfetchall(cursor)
    return result


def namedtuplefetchall(cursor):
    '''
    转换 tuple 值 为 dict 字典值，方便渲染至前端处理
    参考官网：https://docs.djangoproject.com/el/3.0/topics/db/sql/
    '''
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
