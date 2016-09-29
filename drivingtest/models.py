# -*- coding: utf-8 -*-
from django.utils import timezone
from datetime import datetime
print 'in model 2'
from django.db import models
from django.template.defaultfilters import default
from django.contrib.auth.models import User
from django import forms

#from drivingtest.forms import D4_DATETIME_FORMAT
D4_DATETIME_FORMAT = '%H:%M %d/%m/%Y'
postdict ={}
autoimportdict ={}
Notification_global_from_model_module = 'this is Notification_global_from_model_module'
Da_import_xong_global_from_model_module = False
class TbImport(object):
    thongbao = 'chua co thong bao j'
    Da_import_xong_global_from_model_module = False
    GLOBAL_BRIEF_ID_LINK_LIST = []
    GLOBAL_BRIEF_ACTIVE_LIST = []
    GLOBAL_EXACTLY_ACTIVE_LIST = []
    GLOBAL_DUBAO_ACTIVE_LIST = {'du bao tai':[],'du bao xiu': []}
    how_many_current_is_repeat_tai_or_xiu = ('','')#'key of current_group_cau_sign, input of create table 2 la taixiu.objects.all()'
    for_make_fighter_dubao_link = {'du bao tai':('',''),'du bao xiu':('','')}
class thongbao(object):
    thongbao = 'chua co thong bao j'
    log = 'chua co log gi'
    

        
        
        ##OMCKV2
      



### POST FORUM

   
class Ulnew(models.Model):
    title= models.CharField(max_length=200,unique=True,verbose_name='model verbose name')#3
    category= models.CharField(max_length=200)#3
    description= models.CharField(max_length=50000,null=True,blank=True)#3
    date = models.DateTimeField(auto_now_add=True, blank=True)
    
    rg= models.CharField(max_length=2000,null=True,blank=True)#3
    ul= models.CharField(max_length=2000,null=True,blank=True)#3
    up= models.CharField(max_length=2000,null=True,blank=True)#3
    
    myrg= models.CharField(max_length=2000,null=True,blank=True)#3
    myul= models.CharField(max_length=2000,null=True,blank=True)#3
    myup= models.CharField(max_length=2000,null=True,blank=True)#3
    def __unicode__(self):
        return self.title

class ForumTable(models.Model):
    name = models.CharField(max_length=100)#3
    sleep_time = models.IntegerField(default=60)
    url= models.CharField(max_length=100,null=True,blank=True)#3
    postedLog_dat_tenJ_cungduoc_link = models.ManyToManyField('Ulnew', through='PostLog',related_name='forumback')
    uname= models.CharField(max_length=100,null=True,blank=True)#3
    passwd= models.CharField(max_length=100,null=True,blank=True)#3
    newthread_url= models.CharField(max_length=100,null=True,blank=True)#3
    music= models.CharField(max_length=100,null=True,blank=True)#3
    tv_show = models.CharField(max_length=100,null=True,blank=True)#3
    movie= models.CharField(max_length=100,null=True,blank=True)#3
    HDmovie= models.CharField(max_length=100,null=True,blank=True)#3
    software= models.CharField(max_length=100,null=True,blank=True)#3
    game= models.CharField(max_length=100,null=True,blank=True)#3
    anime= models.CharField(max_length=100,null=True,blank=True)#3
    mobile= models.CharField(max_length=100,null=True,blank=True)#3
    ebook= models.CharField(max_length=100,null=True,blank=True)#3
    def __unicode__(self):
        return self.url
class AdminUl (models.Model):
    ul_order = models.IntegerField(default=1)
    rg_order = models.IntegerField(default=2)
    up_order = models.IntegerField(default=3)
    show_not_my_link = models.BooleanField (default=True)
class PostLog(models.Model):
    forum =models.ForeignKey(ForumTable,related_name='postLog')
    posted_topic=models.ForeignKey(Ulnew,related_name='postLog')
    posted_link = models.CharField(max_length=100,null=True,blank=True)
    posted_datetime =  models.DateTimeField(auto_now_add=True, blank=True)

class LeechSite (models.Model):
    url= models.CharField(max_length=100,null=True,blank=True)#3
    music= models.CharField(max_length=100,null=True,blank=True)#3
    tv_show = models.CharField(max_length=100,null=True,blank=True)#3
    movie= models.CharField(max_length=100,null=True,blank=True)#3
    HDmovie= models.CharField(max_length=100,null=True,blank=True)#3
    software= models.CharField(max_length=100,null=True,blank=True)#3
    game= models.CharField(max_length=100,null=True,blank=True)#3
    anime= models.CharField(max_length=100,null=True,blank=True)#3
    mobile= models.CharField(max_length=100,null=True,blank=True)#3
    ebook= models.CharField(max_length=100,null=True,blank=True)#3
class TenTable(models.Model):
    name= models.CharField(max_length=100,unique=True)
    def __unicode__(self):
        return self.name
class DatCua(models.Model):
    cua_tai_hay_xiu= models.IntegerField()
    phien_cua = models.IntegerField(unique=True)
    so_tien = models.IntegerField()
    tenTable = models.ForeignKey(TenTable,blank=True)
class TaiXiu (models.Model):
    phien_so= models.IntegerField(unique=True)#3
    ngay_gio_tao= models.DateTimeField(default=datetime.now,verbose_name=u"Ngày giờ tạo",blank=True)#3
    cau_1= models.IntegerField(null=True,blank=True)#3
    cau_2= models.IntegerField(null=True,blank=True)#3
    cau_3= models.IntegerField(null=True,blank=True)#3
    tong= models.IntegerField(null=True,blank=True)#
    tai_1_xiu_0= models.IntegerField()#
    def __unicode__(self):
        return '+phien %s,cac cau %s,%s,%s+'%(self.phien_so,self.cau_1,self.cau_2,self.cau_3)
class ChartOption(models.Model):    
    Name = models.CharField(max_length=400,unique=True)
    stt = models.IntegerField()
    options_data_list = models.CharField(max_length=400,null=True,blank=True)
    is_select_or_not = models.BooleanField(default = False)
    def __unicode__(self):
        return self.Name
class MySelectChartOption(models.Model):
    Name = models.CharField(max_length=400,unique=True)
    myselect = models.ManyToManyField (ChartOption)
    
class LuuOption(models.Model):    
    Name = models.CharField(max_length=400,unique=True)
    options_data_list = models.CharField(max_length=40000,null=True,blank=True)
    def __unicode__(self):
        return self.Name
    
    