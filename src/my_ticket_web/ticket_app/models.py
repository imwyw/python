# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TLeftTicket(models.Model):
    query_time = models.DateTimeField(blank=True, null=True)
    train_no = models.CharField(max_length=50, blank=True, null=True)
    train_code = models.CharField(max_length=50, blank=True, null=True)
    start_station_code = models.CharField(max_length=50, blank=True, null=True)
    end_station_code = models.CharField(max_length=50, blank=True, null=True)
    from_station_code = models.CharField(max_length=50, blank=True, null=True)
    dest_station_code = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    arrive_time = models.TimeField(blank=True, null=True)
    run_time = models.CharField(max_length=50, blank=True, null=True)
    can_buy = models.CharField(max_length=50, blank=True, null=True)
    start_station_date = models.DateTimeField(blank=True, null=True)
    gr_num = models.CharField(max_length=50, blank=True, null=True)
    qt_num = models.CharField(max_length=50, blank=True, null=True)
    rw_num = models.CharField(max_length=50, blank=True, null=True)
    rz_num = models.CharField(max_length=50, blank=True, null=True)
    tz_num = models.CharField(max_length=50, blank=True, null=True)
    wz_num = models.CharField(max_length=50, blank=True, null=True)
    yw_num = models.CharField(max_length=50, blank=True, null=True)
    yz_num = models.CharField(max_length=50, blank=True, null=True)
    edz_num = models.CharField(max_length=50, blank=True, null=True)
    ydz_num = models.CharField(max_length=50, blank=True, null=True)
    swz_num = models.CharField(max_length=50, blank=True, null=True)
    dw_num = models.CharField(max_length=50, blank=True, null=True)
    remark = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_left_ticket'


class TStation(models.Model):
    short_name = models.CharField(max_length=20, blank=True, null=True)
    full_name = models.CharField(max_length=20, blank=True, null=True)
    station_code = models.CharField(max_length=10, blank=True, null=True)
    station_pin = models.CharField(max_length=50, blank=True, null=True)
    short_name2 = models.CharField(max_length=20, blank=True, null=True)
    num_code = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_station'
