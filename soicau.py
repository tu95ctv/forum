# -*- coding: utf-8 -*- 
import os
import re
from django.core.wsgi import get_wsgi_application
from django.utils.safestring import mark_safe
from django.db.models.query import QuerySet
import urllib2
import requests
from django.db.models import Q
import operator
import threading
from time import sleep
SETTINGS_DIR = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(SETTINGS_DIR, 'media')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnDriving.settings')
application = get_wsgi_application()
from drivingtest.models import TaiXiu, TbImport
from bs4 import BeautifulSoup
from threading import Thread
dict_attr ={}

def read_line(path,split_item):
    f =  open(path, "r")
    content = f.read().decode('utf-8')
    content = content.split(split_item)
    f.close()
    return content


def read_file_from_disk (path):
    f =  open(path, "rb") 
    a = f.read().decode('utf-8')
    f.close()
    return a


def save_file_to_disk(path,content, is_over_write):
    if is_over_write:
        with open(path, "wb") as f:
            f.write(content.encode('utf-8'))
    else:
        with open(path, "ab") as f:
            f.write(content.encode('utf-8'))

html ='''<div id="LuckyDiceSoiCau" style="" class="tx_soi_cau">        <a href="javaScript:;" onclick="LuckyDiceGame.ShowHideSoiCau()" class="tx_btn_close_left"></a>
        <span class="tx_text_soicau">100 phiên gần nhất</span>
        <ul class="tx_text_tai_xiu_soicau">
            <li><img src="/miniluckydice/images/text_tai1.png"></li>
            <li>47</li>
            <li><img src="/miniluckydice/images/text_xiu1.png"></li>
            <li class="tx_mau_soicau">53</li>
        </ul>
        <ul class="tx_ketqua_soicau">
                    <li class="tx_bong_chon" title="Tài: 12 (6 3 3)"><img src="/miniluckydice/images/icon_bong3.png"></li>
                        <li title="Xỉu: 9 (2 4 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 6 (3 1 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (6 3 2)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 4 (2 1 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (6 3 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 12 (5 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 7 (2 2 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 7 (3 1 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (3 4 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (3 3 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 13 (6 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 7 (2 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (4 1 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (6 3 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (3 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (5 4 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 11 (4 4 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau tx_ketqua_soicau1">
                    <li title="Xỉu: 10 (3 4 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                    <li style="margin-top: 5px;" title="Tài: 13 (5 4 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau">
                        <li title="Xỉu: 9 (1 2 6)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (5 4 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (2 2 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 8 (2 4 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (5 3 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 13 (6 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 11 (3 5 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 14 (4 4 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (4 3 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (2 5 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 15 (6 3 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (3 5 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 16 (5 6 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 9 (3 1 5)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (3 4 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 12 (6 4 2)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (4 3 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 10 (2 5 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau tx_ketqua_soicau1 tx_float_left">
                    <li title="Xỉu: 8 (3 4 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                    <li style="margin-top: 5px;" title="Xỉu: 9 (5 2 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau">
                        <li title="Tài: 13 (3 6 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 6 (1 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (6 4 2)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 12 (5 4 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (4 1 5)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 7 (1 4 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 15 (4 6 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (2 2 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 8 (3 2 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (4 4 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 6 (2 3 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (4 3 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (2 4 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 7 (1 3 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (3 6 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 11 (5 1 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 4 (1 1 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 15 (5 5 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau tx_ketqua_soicau1 tx_float_right">
                    <li title="Xỉu: 9 (2 4 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                    <li style="margin-top: 5px;" title="Tài: 15 (6 3 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau">
                        <li title="Xỉu: 7 (2 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (3 4 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (3 4 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 7 (1 3 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (3 1 5)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 6 (3 1 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 7 (3 2 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (5 6 2)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 12 (3 5 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 6 (3 2 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 12 (5 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (3 3 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (4 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 14 (4 5 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 7 (2 2 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (2 4 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 9 (4 4 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Xỉu: 8 (3 3 2)"><img src="/miniluckydice/images/icon_bong1.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau tx_ketqua_soicau1 tx_float_left1">
                    <li title="Tài: 13 (3 6 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                    <li style="margin-top: 5px;" title="Tài: 14 (2 6 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau">
                        <li title="Xỉu: 9 (6 2 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (2 4 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (4 3 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 11 (3 5 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 12 (6 2 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 10 (3 4 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 15 (6 5 4)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 4 (2 1 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (4 3 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (2 3 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (2 5 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 11 (4 6 1)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 16 (4 6 6)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 9 (5 1 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                        <li title="Tài: 13 (4 6 3)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 13 (6 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Tài: 11 (4 2 5)"><img src="/miniluckydice/images/icon_bong2.png"></li>
                        <li title="Xỉu: 8 (2 2 4)"><img src="/miniluckydice/images/icon_bong1.png"></li>
        </ul>
        <ul class="tx_ketqua_soicau tx_ketqua_soicau1 tx_float_right" style="top: 236px;">
                    <li title="Xỉu: 10 (5 2 3)"><img src="/miniluckydice/images/icon_bong1.png"></li>
                    <li style="margin-top: 5px;" title="Xỉu: 6 (2 4 1)"><img src="/miniluckydice/images/icon_bong1.png"></li>
        </ul>
</div>
'''
from random import randint
xac_suat = {3:0.00462962962962963,4:0.0138888888888889,5:0.0277777777777778,6:0.0462962962962963,7:0.0694444444444444,8:0.0972222222222222,9:0.115740740740741,10:0.125,11:0.125,12:0.115740740740741,13:0.0972222222222222,14:0.0694444444444444,15:0.0462962962962963,16:0.0277777777777778,17:0.0138888888888889,18:0.00462962962962963}
mau_thu = 100
TAI = 1
XIU = 0
def roll_3_dice():
    tong_3_cau_lists = []
    tai_xiu_lists = []
    so_luong_tai = 0
    so_luong_xiu = 0
    for i in range(1,mau_thu+1):
        tong_3_cau = randint(1,6) + randint(1,6) + randint(1,6)
        tong_3_cau_lists.append(tong_3_cau)
        if tong_3_cau <11:
            so_luong_xiu +=1
            tai_xiu_lists.append(XIU)
        else:
            so_luong_tai +=1
            tai_xiu_lists.append(TAI)
    return tong_3_cau_lists,tai_xiu_lists
    
#Test lai xac suat cua 1 lan roll 3 dice
def test_xac_suat_tong_3_dice(tong_3_cau_lists):
    #count_3_to18_dict  = {}
    print 'tong_3_cau_lists',tong_3_cau_lists
    for i in range(3,19):
        rs_percent = tong_3_cau_lists.count(i)/float(mau_thu)
        sai_so = (rs_percent -xac_suat[i])*100/float(xac_suat[i])
        #count_3_to18_dict[rs_percent ] = i
        print u'tổng 3 cầu, phần trăm, sai số ',i,rs_percent,"%.2f%%" %sai_so
def wanting_html_create(du_tai,xac_suat_du_thieu):
           
        
        if xac_suat_du_thieu < 0:
            if xac_suat_du_thieu <-50:
                wanting_template = '<span class="wanting-in-td-level3">[%.1f (%.1f%%)]</span>'
            elif xac_suat_du_thieu < -30:
                wanting_template = '<span class="wanting-in-td-level2">[%.1f (%.1f%%)]</span>'
            else:
                wanting_template = '<span class="wanting-in-td">[%.1f (%.1f%%)]</span>' 
            template = wanting_template
        else:
            if xac_suat_du_thieu >50:
                redundant_template = '<span class="redundant-in-td-level3">[%.1f (%.1f%%)]</span>'
            elif xac_suat_du_thieu >30 :
                redundant_template = '<span class="redundant-in-td-level2">[%.1f (%.1f%%)]</span>'
            elif xac_suat_du_thieu >0:
                redundant_template = '<span class="redundant-in-td-level1">[%.1f (%.1f%%)]</span>'
            elif xac_suat_du_thieu ==0:
                redundant_template = '<span class="redundant-in-td0">[%.1f (%.1f%%)]</span>'
            template = redundant_template
        xac_suat_du_thieu = template%(du_tai,xac_suat_du_thieu) 
        return xac_suat_du_thieu
def test_xac_suat_tong_3_dice_database(tong_3_cau_lists):
    mau_thu = len(tong_3_cau_lists)
    #count_3_to18_dict  = {}
    dict_lists = []
    mydict = {}
    for i in range(3,19):
        tai_xiu_sign = "Tai" if i > 10 else "Xiu"
        extra_stuff = [s for s in tong_3_cau_lists if s.tong==i]
        rs = len(extra_stuff)
        rs_percent = rs/float(mau_thu)
        ly_thuyet = xac_suat[i]
        ly_thuyet_ung_voi_mau_thu = ly_thuyet*mau_thu
        sai_so = (rs_percent -xac_suat[i])*100/float(ly_thuyet)
        du_thieu = rs - ly_thuyet_ung_voi_mau_thu
        xac_suat_con_lai = du_thieu*100/float(mau_thu)
        xac_suat_con_lai_html = wanting_html_create(du_thieu,xac_suat_con_lai)
        #count_3_to18_dict[rs_percent ] = i
        display_html = " %s ly thuyet %.2f (%s %.2f%%)"%(rs,ly_thuyet_ung_voi_mau_thu,xac_suat_con_lai_html,sai_so)
        mydict = {'mau_thu':'%s ly thuyet %.2f %%'%(mau_thu,ly_thuyet*100),'tong':i,'tai_or_xiu':tai_xiu_sign,\
                  'phan_tram':mark_safe(display_html)}
        dict_lists.append(mydict)
    return dict_lists
# count xen ke, hoac giong nhau, tich luy
GIONG_NHAU=0
XEN_KE=1

def create_giong_nhau_khac_nhau_lists(tai_xiu_lists,show_description = "khong xen ke type",is_created_xenKe_list = True):
    mau_thu = len(tai_xiu_lists)
    description_for_tai_xiu = "tai xiu" if  show_description != 'xen ke type' else  "xenkegiongnhau"
    print '%s lists'%description_for_tai_xiu,tai_xiu_lists
    xen_ke_or_giong_nhau_lists= []
    GIONG_NHAU=0
    XEN_KE=1
    so_cau_tai_giong_nhau_trong_1_nhom = 0
    so_cau_xiu_giong_nhau_trong_1_nhom = 0
    tai_repeat_lists = []
    xiu_repeat_lists = []
    xiutai=0
    xiuxiu=0
    taixiu=0
    taitai=0
    tai_sluong = 0
    xiu_sluong = 0
    string_tai_xiu_soi_cau = ''
    current_html_template = '<span class="current-in-td">%s</span>'
    not_current_html_template = '<span class="not-current-in-td">%s</span>'
    xen_ke_giong_nhau_bat_dau_tu_TAI_dict = {}
    xen_ke_giong_nhau_bat_dau_tu_XIU_dict = {}
    str_partern = '%s/%.0f %s' 
    for c,cau in enumerate(tai_xiu_lists):
        if isinstance(tai_xiu_lists, QuerySet):
            current_i = cau.tai_1_xiu_0
        else:
            current_i = cau
        if c<100:
            if 0:#c % 19==0:
                xuong_dong = '<br>'
            else:
                xuong_dong = ' '
            if current_i==1:
                #string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "tai-cau"></span>' + xuong_dong
                string_tai_xiu_soi_cau += '<span class = "tai-cau"></span>' + xuong_dong

                print 'Tai'
            else:
                #string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "xiu-cau"></span>' + xuong_dong
                string_tai_xiu_soi_cau +='<span class = "xiu-cau"></span>' + xuong_dong
        if current_i==XIU:
            so_cau_xiu_giong_nhau_trong_1_nhom += 1
            xiu_sluong +=1
        else:
            so_cau_tai_giong_nhau_trong_1_nhom +=1
            tai_sluong += 1
        if c ==0:
            bf_i = current_i
            last_cau = current_i
        else:
            if current_i !=bf_i:
                if is_created_xenKe_list:
                    xen_ke_or_giong_nhau_lists.append(XEN_KE)
                if current_i==XIU:
                    taixiu +=1
                    tai_repeat_lists.append(so_cau_tai_giong_nhau_trong_1_nhom)
                    so_cau_tai_giong_nhau_trong_1_nhom =0
                else:#chot so_luong_tai
                    xiutai +=1
                    xiu_repeat_lists.append(so_cau_xiu_giong_nhau_trong_1_nhom)
                    so_cau_xiu_giong_nhau_trong_1_nhom= 0
            else:
                if is_created_xenKe_list:
                    xen_ke_or_giong_nhau_lists.append(GIONG_NHAU)
                if current_i==XIU:
                    xiuxiu +=1
                else:
                    taitai +=1
            bf_i = current_i
    def create_current_html(last_cau,tai_repeat_list_count,tai_or_xiu = "tai"):
        if last_cau and tai_or_xiu == "tai":
                tai_repeat_list_count = current_html_template%tai_repeat_list_count
        elif not last_cau and tai_or_xiu == "xiu":
            tai_repeat_list_count = current_html_template%tai_repeat_list_count
        else:
            tai_repeat_list_count = not_current_html_template%tai_repeat_list_count
        return tai_repeat_list_count
    txxt_dict = {}        
    def tai_xiu_50_50_create_html(tai_sluong,tai_or_xiu ="tai"):
        
        mau_thu_chia_2 = mau_thu/float(2)
        so_luong_ly_thuyet = mau_thu_chia_2
        du_tai = tai_sluong-mau_thu_chia_2
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet = du_tai*100/(float(mau_thu)/2)
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(du_tai,ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
        #du_tai_html = wanting_html_create(ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
        tai_sluong = create_current_html(last_cau,tai_sluong,tai_or_xiu)
        tai_html = str_partern%(tai_sluong,so_luong_ly_thuyet,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html)
        return mark_safe(tai_html)
    tai_or_xiu_html = tai_xiu_50_50_create_html(tai_sluong)
    txxt_dict['tai'] = tai_or_xiu_html
    tai_or_xiu_html = tai_xiu_50_50_create_html(xiu_sluong,tai_or_xiu ="xiu")
    txxt_dict['xiu'] = tai_or_xiu_html
    txxt_dict.update({'mau_thu':mau_thu})
    
    txxt_map ={'xiu_tai':xiutai,'xiu_xiu':xiuxiu,'tai_xiu':taixiu,'tai_tai':taitai}
    mau_thu_chia_4 = mau_thu/float(4)
    txxt_dict_list = []     
    for k,so_luong_thuc_te in txxt_map.iteritems():
        pattern = '^xiu'
        rs = re.match(pattern, k)
        if rs:
            tai_or_xiu = 'xiu'
        else:
            tai_or_xiu = 'tai'
        so_luong_ly_thuyet = mau_thu_chia_4
        so_luong_du_thieu = so_luong_thuc_te-so_luong_ly_thuyet
        
        xac_suat_du_thieu = 100*so_luong_du_thieu/mau_thu
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet = 100*xac_suat_du_thieu/25#25: nghia la 25%
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(so_luong_du_thieu,ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
        so_luong_thuc_te_html = create_current_html(last_cau,so_luong_thuc_te,tai_or_xiu)
        txxt_dict[k] = mark_safe(str_partern%(so_luong_thuc_te_html,so_luong_ly_thuyet,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html))
    txxt_dict_list.append(txxt_dict)
    
    description_for_tai = "tai" if  show_description != 'xen ke type' else  "xen ke"
    description_for_xiu = "xiu" if  show_description != 'xen ke type' else  "giong nhau"
    print '%s repeat lists'%description_for_tai,tai_repeat_lists
    print '%s repeat lists'%description_for_xiu,xiu_repeat_lists
    print 'len %s repeat list,len %s repeat list'%(description_for_tai,description_for_xiu),len(tai_repeat_lists),len(xiu_repeat_lists)
    repeat_dict_lists = []
    for i in range(1,20):
        tai_repeat_list_count = tai_repeat_lists.count(i)
        xiu_repeat_list_count =  xiu_repeat_lists.count(i)
        if tai_repeat_list_count or xiu_repeat_list_count:
            max_i_has_value = i
    
    def create_td_repeat(tai_repeat_lists,lythuyet_repeat_xac_suat_i,tai_or_xiu = "tai"):
            
            so_luong_thuc_te = tai_repeat_lists.count(i)
            so_luong_ly_thuyet = lythuyet_repeat_xac_suat_i *mau_thu/100
            #sai_so_repeat_tai = (tai_repeat_percent  - lythuyet_repeat_xac_suat_i)*100/float(lythuyet_repeat_xac_suat_i)
            so_luong_du_thieu = (so_luong_thuc_te - so_luong_ly_thuyet)
            xac_suat_du_thieu = (so_luong_thuc_te - lythuyet_repeat_xac_suat_i*mau_thu/100)*100/mau_thu
            ti_le_xac_suat_du_thieu_xacSuatLyThuyet = 100*xac_suat_du_thieu/lythuyet_repeat_xac_suat_i#25: nghia la 25%
            ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(so_luong_du_thieu,ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
            so_luong_thuc_te_html_for_current_cau = create_current_html(last_cau,so_luong_thuc_te,tai_or_xiu = tai_or_xiu)
            td_value = str_partern%(so_luong_thuc_te_html_for_current_cau,so_luong_ly_thuyet,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html)
            return td_value
     
    for i in range(1,20):
        if i > max_i_has_value:
            continue
        repeat_dict = {}
        
        lythuyet_repeat_xac_suat_i = float(12.5/pow(2, (i-1)))
        td_value = create_td_repeat(tai_repeat_lists,lythuyet_repeat_xac_suat_i)
        repeat_dict['tai_repeat_list_count'] = mark_safe(td_value)
        td_value = create_td_repeat(xiu_repeat_lists,lythuyet_repeat_xac_suat_i,tai_or_xiu = "xiu")
        repeat_dict['xiu_repeat_list_count'] =  mark_safe(td_value)

        
        repeat_dict['so_lan_lap'] = i
        repeat_dict['mau_thu'] = mau_thu
        repeat_dict['lythuyet_repeat_xac_suat_i'] = u'%.2f%% '%(lythuyet_repeat_xac_suat_i)
        repeat_dict_lists.append(repeat_dict)
    description_for_taixiu_diff = "tai xiu xen ke" if  show_description != 'xen ke type' else  "xenkegiongnhau xen ke"
    description_for_taixiu_same = "tai xiu giong nhau" if  show_description != 'xen ke type' else  "xenkegiongnhau xen ke giong nhau"
    
    print 'so luong %s'%description_for_taixiu_diff,xen_ke_or_giong_nhau_lists.count(XEN_KE)
    print 'so luong %s'%description_for_taixiu_same,xen_ke_or_giong_nhau_lists.count(GIONG_NHAU)
    return xen_ke_or_giong_nhau_lists,tai_repeat_lists,xiu_repeat_lists,repeat_dict_lists,txxt_dict_list,mark_safe(string_tai_xiu_soi_cau)
def check_cau():
    qrs = TaiXiu.objects.all().order_by('-phien_so')
    print len(qrs)
    for c,i in enumerate(qrs):
        print i.phien_so,i.id
        if c==0:
            bf_p = i.phien_so
        else:
            ch = i.phien_so - bf_p
            if ch !=-1:
                print i.phien_so,bf_p
                raise ValueError('fdffddf')
            bf_p = i.phien_so
def phien_100_to_html():
        ALOWED_change=True
    #tai_xiu_lists = []
        soicau_html = read_file_from_disk (MEDIA_ROOT + '/taixiu/soicau.txt')
        html = soicau_html
        soup = BeautifulSoup(html)
        phien_txt = soup.select('span#sessionidTX')[0].get_text()
        phien = int(re.findall('(\d+)',phien_txt)[0]) -  1
        class_entry_name = '.tx_ketqua_soicau'
        soup  = soup.select('#LuckyDiceSoiCau')[0]
        entries = soup.select(class_entry_name)
        #print 'entries',entries,'\n',len(entries)
        so_phien_in_100 = 1
        last_phien_bat_dau_trong_html = phien
        try:
            last_phien = TaiXiu.objects.latest('phien_so').phien_so
            ly_thuyet_se_co_so_luot_duoc_import = last_phien_bat_dau_trong_html - last_phien
        except:
            last_phien = ''
            ly_thuyet_se_co_so_luot_duoc_import = ''
        
        
        thuc_te_so_import  = 0
        quet_qua_ma_khong_duoc_tao = 0
        str_phien_co_gia_tri_khac_truoc=''
        so_phien_bi_khac = 0
        for c,entry in enumerate(entries):
            
                
            lis = entry.select('li')
            if c==2 or c==6:
                lis.reverse()
            for li in lis:
                instance_dict = {}
                li_title = li['title']#"Tài: 12 (6 3 3)"
                rs = re.findall("(\S{3}?): (\d+) \((\d) (\d) (\d)\)",li_title)
                tai_or_xiu_string= rs[0][0]
                instance_dict['tong'] = int(rs[0][1])
                instance_dict['cau_1'] = int(rs[0][2])
                instance_dict['cau_2'] = int(rs[0][3])
                instance_dict['cau_3'] = int(rs[0][4])
                if tai_or_xiu_string ==u"Tài":
                    tai_or_xiu = 1
                elif tai_or_xiu_string ==u"Xỉu":
                    tai_or_xiu = 0
                instance_dict['tai_1_xiu_0'] =tai_or_xiu
                instance_dict['phien_so'] =phien
                try:
                    created = False
                    instance = TaiXiu.objects.get(phien_so = phien)
                    if instance.cau_1 is None or ALOWED_change:
                        instance.__dict__.update(instance_dict)
                        instance.save()
                        created = True
                    for (key, value) in instance_dict.items():
                        database_data = getattr(instance, key)
                        if  database_data!=value:
                            field_bi_khac = '"%s"-%s-%s'%(key,value,database_data)
                            str_phien_co_gia_tri_khac_truoc_1_item = '[%s (so thu tu %s) field khac %s]'%(str(instance.phien_so),so_phien_in_100,field_bi_khac)
                            str_phien_co_gia_tri_khac_truoc += str_phien_co_gia_tri_khac_truoc_1_item +','
                            print str_phien_co_gia_tri_khac_truoc_1_item,'key value',key,value
                            so_phien_bi_khac +=1
                            break 
                            
                except TaiXiu.DoesNotExist:
                    instance = TaiXiu(**instance_dict)
                    instance.save()
                    created = True
                if created:
                    thuc_te_so_import +=1
                else:
                    quet_qua_ma_khong_duoc_tao +=1
                #except  :
                    #if so_phien_in_100 ==100 :
                        #continue
                    #else:
                        #raise ValueError('abcfdsfd')
                phien -=1
                so_phien_in_100 +=1
        tb='tong ket\n,'
        tb += '\n,' + 'last_phien %s'%last_phien
        tb += '\n,' + 'str_phien_co_gia_tri_khac_truoc %s'%str_phien_co_gia_tri_khac_truoc
        tb +='\n,' +'last_phien_bat_dau_trong_html %s'%last_phien_bat_dau_trong_html
        tb +='\n,' +'ly_thuyet_se_co_so_luot_duoc_import %s'%ly_thuyet_se_co_so_luot_duoc_import
        tb +='\n,' +'thuc_te_so_import %s'%thuc_te_so_import
        tb +='\n,' +'quet_qua_ma_khong_duoc_tao %s'%quet_qua_ma_khong_duoc_tao
        tb +='\n,' +'so_phien_bi_khac %s'%so_phien_bi_khac
        print tb
        return tb
def tim_phien_cua_100(dict_100_phien):
    return 0000    
def autoimport(last_phien_in_100_user_import = None,ALOWED_change= False,save_or_test = True):
        html = get_html('http://vuachoibai.com/miniluckydice/MiniGameLuckyDice/LuckyDiceSoiCau')
        soup = BeautifulSoup(html)
        class_entry_name = '.tx_ketqua_soicau'
        entries = soup.select(class_entry_name)
        list_100_phiens = []
        for c,entry in enumerate(entries):
            lis = entry.select('li')
            if c==2 or c==6:
                lis.reverse()
            for li in lis:
                instance_dict = {}
                li_title = li['title']#"Tài: 12 (6 3 3)"
                rs = re.findall("(\S{3}?): (\d+) \((\d) (\d) (\d)\)",li_title)
                tai_or_xiu_string= rs[0][0]
                instance_dict['tong'] = int(rs[0][1])
                instance_dict['cau_1'] = int(rs[0][2])
                instance_dict['cau_2'] = int(rs[0][3])
                instance_dict['cau_3'] = int(rs[0][4])
                if tai_or_xiu_string ==u"Tài":
                    tai_or_xiu = 1
                elif tai_or_xiu_string ==u"Xỉu":
                    tai_or_xiu = 0
                instance_dict['tai_1_xiu_0'] =tai_or_xiu
                #instance_dict['phien_so'] =phien
                list_100_phiens.append(instance_dict)
        
        tb='tong ket\n,'
        #print list_100_phiens
        last_phien = TaiXiu.objects.latest('phien_so').phien_so
        if last_phien_in_100_user_import:
            phien = last_phien_in_100_user_import-1
        else:#tim 
            lastest_100_cau_in_dbs = TaiXiu.objects.filter(phien_so__gt = last_phien-100 )
            same_100_html_querysets =[]
            qgroup=Q()
            
            for count,i_tim in enumerate(range(98,90,-1)):
                instance_dict = list_100_phiens[i_tim]
                qgroup = reduce(operator.and_, (Q(**{key :value}) for key,value in instance_dict.items()))
                if count ==0:
                    pass
                elif count!=0:
                    instance_dict['phien_so'] = same_100_html_querysets[0].phien_so + 1
                    qgroup_FRNAME = reduce(operator.or_, (Q(**{"phien_so" : (obj.phien_so + 1)}) for obj in same_100_html_querysets ))    
                    qgroup = qgroup & qgroup_FRNAME       
                
                same_100_html_querysets  = lastest_100_cau_in_dbs.filter(qgroup)
                    
                if len(same_100_html_querysets ) == 1:
                    last_phien_in_100_user_import = same_100_html_querysets [0].phien_so  + i_tim
                    #print 'same_100_html_querysets [0] %s,instance_dict %s'%(same_100_html_querysets [0],instance_dict)
                    break
                elif len(same_100_html_querysets) ==0:
                    raise ValueError ('databse chua co cau nao trong 100 cau')
            phien = last_phien_in_100_user_import
        str_phien_co_gia_tri_khac_truoc = ''
        so_phien_bi_khac=0
        thuc_te_so_import = 0
        quet_qua_ma_khong_duoc_tao =0
        so_phien_in_100 = 1
        for instance_dict in list_100_phiens:
            instance_dict['phien_so'] = phien
            try:
                created = False
                instance = TaiXiu.objects.get(phien_so = phien)
                if instance.cau_1 is None or ALOWED_change:
                    instance.__dict__.update(instance_dict)
                    instance.save()
                    created = True
                for (key, value) in instance_dict.items():
                    database_data = getattr(instance, key)
                    if  database_data!=value:
                        #print '@@@@@@@@@@da co su khac biet'
                        #print instance_dict
                        #for k,v in instance_dict.items():
                            #print k,getattr(instance, k)
                        field_bi_khac = '"%s"-%s-%s'%(key,value,database_data)
                        str_phien_co_gia_tri_khac_truoc_1_item = '[%s (so thu tu %s) field khac %s (tong o html %s,tong o db %s ]'%(str(instance.phien_so),so_phien_in_100,field_bi_khac,instance_dict['tong'],instance.tong)
                        str_phien_co_gia_tri_khac_truoc += str_phien_co_gia_tri_khac_truoc_1_item +','
                        so_phien_bi_khac +=1
                        break 
                        
            except TaiXiu.DoesNotExist:
                instance = TaiXiu(**instance_dict)
                if save_or_test:
                    instance.save()
                created = True
            if created:
                thuc_te_so_import +=1
            else:
                quet_qua_ma_khong_duoc_tao +=1
            #except  :
                #if so_phien_in_100 ==100 :
                    #continue
                #else:
                    #raise ValueError('abcfdsfd')
            phien -=1
            so_phien_in_100 +=1
        
        #print 'count',count,i_tim,same_100_html_querysets [0].phien_so ,'list_100_phiens',len(list_100_phiens),same_100_html_querysets [0]
        ly_thuyet_se_co_so_luot_duoc_import = last_phien_in_100_user_import - last_phien
        tb='tong ket</br>'
        tb += '</br>' + 'last_phien %s'%TaiXiu.objects.latest('phien_so').phien_so
        tb += '</br>' + 'str_phien_co_gia_tri_khac_truoc %s'%str_phien_co_gia_tri_khac_truoc
        tb +='</br>' +'last_phien_in_100_user_import %s'%last_phien_in_100_user_import
        tb +='</br>' +'ly_thuyet_se_co_so_luot_duoc_import %s'%ly_thuyet_se_co_so_luot_duoc_import
        tb +='</br>' +'thuc_te_so_import %s'%thuc_te_so_import
        tb +='</br>' +'quet_qua_ma_khong_duoc_tao %s'%quet_qua_ma_khong_duoc_tao
        tb +='</br>' +'so_phien_bi_khac %s'%so_phien_bi_khac
        print tb
        return mark_safe(tb)
def xoa_100_cai_cu_nhat():
    qrs = TaiXiu.objects.all().order_by('id')[:100]
    print len(qrs)
    for x in qrs:
        x.delete()
def check_continous():
    qrs = TaiXiu.objects.all().order_by('phien_so')
    khong_lts={}
    for c,x in enumerate(qrs):
        if c==0:
            bf =  x.phien_so
        else:
            rs = x.phien_so - bf
            print rs,x.phien_so
            
            if rs > 1:
                khong_lts.update({x.phien_so:(rs,bf)})
                print x.phien_so
            bf = x.phien_so
    print 'khong_lts',khong_lts
def xoa_from(end=799357):
    qrs = TaiXiu.objects.filter(phien_so__lte =end )
    print len(qrs)
    for x in qrs:
        x.delete()
    qrs = TaiXiu.objects.filter(phien_so__lte =end )
    print len(qrs)                
def create_how_many_phien_for_same_cau():
    re_lists = []
    for i in range(1,20):
        lythuyet_repeat_xac_suat_i = float(12.5/pow(2, (i-1)))
        so_phien_can_thiet=100*1/lythuyet_repeat_xac_suat_i
        #so_phut
        so_phut = so_phien_can_thiet *1.5
        so_gio = so_phut/float(60)
        so_ngay = so_gio/24
        print i ,so_phien_can_thiet,'so phut',so_phut,'sogio',so_gio,'so ngay',so_ngay
        re_dict = {'so_lan_lap':i,'xac_suat':lythuyet_repeat_xac_suat_i,'so_phien_can_thiet':so_phien_can_thiet, 'so_phut':so_phut,'so_gio':so_gio,'so_ngay':so_ngay}
        re_lists.append(re_dict)
    return re_lists


def read_html_dice():
    html = read_file_from_disk(MEDIA_ROOT +'/taixiu/html.txt')
    rs = re.findall('<script src="(.*?)"', html, re.IGNORECASE)
    #print 'rs',rs
    
    if 1:
        for i in rs:
            print i
    return rs
    #print html  
def get_html(url):    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = None 
    for i in xrange(13):
        try:
            html = opener.open(url).read()
            break
        except:
            print 'Get html.. again for timeout'
    return html   
def check_dice_in_script():
    for i in read_html_dice():
        print i
        if '//vuachoibai.com' in i:
            i = i.replace('//','')
            continue
        if 'vuachoibai.com' not in i:
            i = 'http://vuachoibai.com/' + i
        script =  get_html(i)
        if 'dice' in script or 'Dice' in script:
            print 'da tim thay',i
        else:
            print 'sorry'
            
            
class AutoImportObject(Thread):
    def __init__(self):
        Thread.__init__(self)
        #self._stop = threading.Event()
        self.stop = False
    def stop(self):
        #self._stop.set()
        self.stop = True
    def stopped(self):
        return self._stop.isSet()
    def run(self):
        so_lan_quet = 0
        while (not self.stop) :
            try:
                print 'begin '
                TbImport.thongbao = autoimport() + '\n so lan quet %s',so_lan_quet
                TbImport.Da_import_xong_global_from_model_module = True
                i = 5
                while i:
                    print i
                    i =i-1
                    sleep(0,2)
                so_lan_quet += 1
            except:
                sleep(4)
def chon_tren_hoac_duoi(repeat_XIU_lists,so_be = 0, so_lon =2):
    list_new = []
    for i in repeat_XIU_lists:
        if i == so_lon:
            list_new.append(1)
        elif i >so_lon or (so_be !=0 and i <so_lon and i >=so_be):
            list_new.append(0)
    return list_new
def chon_tren_hoac_duoi_cau_kep(repeat_XIU_lists,so_cau_moc=3):
    list_new = []
    for x in repeat_XIU_lists:
        if x.so_luong_cau == so_cau_moc:
            x.tai_1_xiu_0 =1
            #list_new.append(1)
            list_new.append(x)
        elif (x.so_luong_cau >so_cau_moc ):
            x.tai_1_xiu_0 =0
            #list_new.append(0)
            list_new.append(x)
    return list_new
class Caukep():
    def __init__(self,phien_bat_dau=None,\
                 so_luong_cau=None,\
                 same_or_different=None,\
                 bat_dau_la_tai_hay_xiu=None,\
                 ket_thuc_la_tai_hay_xiu = None,\
                 tai_1_xiu_0 = None,):
        self.phien_so = phien_bat_dau
        self.so_luong_cau = so_luong_cau
        self.same_or_different = same_or_different
        self.bat_dau_la_tai_hay_xiu = bat_dau_la_tai_hay_xiu
        self.ket_thuc_la_tai_hay_xiu = ket_thuc_la_tai_hay_xiu
        self.tai_1_xiu_0 = tai_1_xiu_0
    def __repr__(self):
        return u'(%s, phien bat dau: %s,sluong:%s,tai1xiu0 %s)'%("TAI begin" if self.bat_dau_la_tai_hay_xiu else "XIU begin" ,self.phien_so,self.so_luong_cau,self.tai_1_xiu_0)
def soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),END_LIST = [100,256,512,1024,2048,0],is_print = True):
    TAI  =1
    XIU = 0
    if 0 in END_LIST:
        END_LIST.remove(0)
        END_LIST.append(len(qrs))
    more_info_get_from_loop = {'max_tai':0,'max_xiu':0,'dict_thong_ke_repeat_TAI_list_of_mau_thu':{}}
    END_LIST_index = 0
    END_LIST_index_xen_ke= 0
    dict_thong_ke_repeat_TAI  ={}
    dict_thong_ke_repeat_XIU ={}
    so_luong_cau_XIU_trong_nhom = 0
    so_luong_cau_TAI_trong_nhom = 0
    dict_thong_ke_XEN_KE_XIU = {}
    dict_thong_ke_XEN_KE_TAI = {}
    so_luong_cau_XEN_KE_trong_nhom = 0
    CAU_LIST_show_xenke = []
    repeat_TAI_lists = []
    repeat_XIU_lists = []
    XEN_KE_TAI_lists= []
    XEN_KE_XIU_lists = []
    cau_same_gan_nhat =None
    xen_ke_or_giong_nhau_lists = []
    GIONG_NHAU = 0
    is_chot_XEN_KE=False
    is_chot_REPEAT  =False
    dict_thong_ke_repeat_TAI_list_of_mau_thu = {}
    dict_thong_ke_repeat_XIU_list_of_mau_thu = {}
    dict_thong_ke_xen_ke_TAI_list_of_mau_thu = {}
    dict_thong_ke_xen_ke_XIU_list_of_mau_thu = {}
    cho_phep_tach_REPEAT_neu_du_so_luong = False
    cho_phep_tach_XEN_KE_neu_du_so_luong = False
    before_state_same_or_different = "different"
    for c,cau in enumerate(qrs):
        if is_chot_XEN_KE and is_chot_REPEAT:
            break
        if not isinstance(qrs, int):
            current_value = cau.tai_1_xiu_0
            qrs_is_queryset = True
        else:
            current_value = cau
            qrs_is_queryset = False
        
        if current_value ==TAI:
            so_luong_cau_TAI_trong_nhom +=1
        else:
            so_luong_cau_XIU_trong_nhom +=1
        if c == 0:
            last_cau_value = current_value
            before_value = current_value
            before_cau_for_repeat = cau
            before_dice_for_xen_ke = cau
            #CAU_LIST_show_repeat.append(current_value)
            #CAU_LIST_show_xenke.append(current_value)
        else:
            if current_value != before_value:
                if not is_chot_REPEAT:
                    #CAU_LIST_show_repeat.append(current_value)
                    if before_value == TAI: #current_value la tai
                        try:
                            dict_thong_ke_repeat_TAI[so_luong_cau_TAI_trong_nhom] +=1
                        except KeyError:
                            dict_thong_ke_repeat_TAI[so_luong_cau_TAI_trong_nhom] =1
                        if so_luong_cau_TAI_trong_nhom > more_info_get_from_loop['max_tai']:
                            more_info_get_from_loop['max_tai'] = so_luong_cau_TAI_trong_nhom
                        if qrs_is_queryset:
                            so_luong_cau_TAI_trong_nhom = Caukep(before_cau_for_repeat.phien_so,\
                                                                 so_luong_cau_TAI_trong_nhom,\
                                                                 same_or_different=0,\
                                                                 bat_dau_la_tai_hay_xiu = before_cau_for_repeat.tai_1_xiu_0)
                        repeat_TAI_lists.append(so_luong_cau_TAI_trong_nhom)
                        so_luong_cau_TAI_trong_nhom = 0
                    else:
                        try:
                            dict_thong_ke_repeat_XIU[so_luong_cau_XIU_trong_nhom] +=1
                        except KeyError:
                            dict_thong_ke_repeat_XIU[so_luong_cau_XIU_trong_nhom] =1
                        if so_luong_cau_XIU_trong_nhom > more_info_get_from_loop['max_xiu']:
                            more_info_get_from_loop['max_xiu'] = so_luong_cau_XIU_trong_nhom
                        if qrs_is_queryset:
                            so_luong_cau_XIU_trong_nhom = Caukep(before_cau_for_repeat.phien_so,\
                                                                 so_luong_cau_XIU_trong_nhom,\
                                                                 same_or_different=0,\
                                                                 bat_dau_la_tai_hay_xiu =before_cau_for_repeat.tai_1_xiu_0)
                        repeat_XIU_lists.append(so_luong_cau_XIU_trong_nhom)   
                        so_luong_cau_XIU_trong_nhom = 0
                    before_value = current_value
                    before_cau_for_repeat = cau
                    cho_phep_tach_REPEAT_neu_du_so_luong = True
                if not is_chot_XEN_KE:        
                    #CAU_LIST_show_xenke.append(current_value)
                    so_luong_cau_XEN_KE_trong_nhom +=1
                    if before_state_same_or_different == "same":
                        before_dice_for_xen_ke = cau_same_gan_nhat
                        before_state_same_or_different = "different"
                    
            else:
                if not is_chot_REPEAT:
                    #CAU_LIST_show_repeat.append(current_value)
                    pass
                if not is_chot_XEN_KE:
                    before_state_same_or_different = "same"
                    cau_same_gan_nhat = cau
                    #CAU_LIST_show_xenke.append(current_value)
                    #xen_ke_or_giong_nhau_lists.append(GIONG_NHAU)
                    if so_luong_cau_XEN_KE_trong_nhom :
                        if current_value ==TAI:
                            try:
                                dict_thong_ke_XEN_KE_TAI[so_luong_cau_XEN_KE_trong_nhom] +=1
                            except KeyError:
                                dict_thong_ke_XEN_KE_TAI[so_luong_cau_XEN_KE_trong_nhom] =1
                            if qrs_is_queryset:
                                so_luong_cau_XEN_KE_trong_nhom = Caukep(before_dice_for_xen_ke.phien_so,\
                                                                        so_luong_cau_XEN_KE_trong_nhom,\
                                                                        same_or_different=1,\
                                                                        bat_dau_la_tai_hay_xiu =cau.tai_1_xiu_0)
                            XEN_KE_TAI_lists.append(so_luong_cau_XEN_KE_trong_nhom)      
                            
                        elif current_value ==XIU:
                            try:
                                dict_thong_ke_XEN_KE_XIU[so_luong_cau_XEN_KE_trong_nhom] +=1
                            except KeyError:
                                dict_thong_ke_XEN_KE_XIU[so_luong_cau_XEN_KE_trong_nhom] =1
                            if qrs_is_queryset:
                                so_luong_cau_XEN_KE_trong_nhom = Caukep(before_dice_for_xen_ke.phien_so,\
                                                                        so_luong_cau_XEN_KE_trong_nhom,\
                                                                        same_or_different=1,\
                                                                        bat_dau_la_tai_hay_xiu =cau.tai_1_xiu_0)
                            XEN_KE_XIU_lists.append(so_luong_cau_XEN_KE_trong_nhom)
                        so_luong_cau_XEN_KE_trong_nhom = 0  
                    cho_phep_tach_XEN_KE_neu_du_so_luong = True 
                            
            if c >= END_LIST[END_LIST_index]-1 and cho_phep_tach_REPEAT_neu_du_so_luong or c==len(qrs):
                cho_phep_tach_REPEAT_neu_du_so_luong = False
                copy_dict  = dict_thong_ke_repeat_TAI.copy()
                dict_thong_ke_repeat_TAI_list_of_mau_thu [END_LIST[END_LIST_index]] = copy_dict
                copy_dict  = dict_thong_ke_repeat_XIU.copy()
                dict_thong_ke_repeat_XIU_list_of_mau_thu [END_LIST[END_LIST_index]] = copy_dict
                END_LIST_index +=1
                if END_LIST_index ==len(END_LIST):
                    is_chot_REPEAT  = True                
            if c >= END_LIST[END_LIST_index_xen_ke]-1 and cho_phep_tach_XEN_KE_neu_du_so_luong or c==len(qrs):
                        cho_phep_tach_XEN_KE_neu_du_so_luong = False
                        copy_dict  = dict_thong_ke_XEN_KE_TAI.copy()
                        dict_thong_ke_xen_ke_TAI_list_of_mau_thu [END_LIST[END_LIST_index_xen_ke]] = copy_dict
                        copy_dict  = dict_thong_ke_XEN_KE_XIU.copy()
                        dict_thong_ke_xen_ke_XIU_list_of_mau_thu[END_LIST[END_LIST_index_xen_ke]] = copy_dict
                        END_LIST_index_xen_ke +=1
                        if END_LIST_index_xen_ke ==len(END_LIST):
                            is_chot_XEN_KE  = True
    more_info_get_from_loop['dict_thong_ke_repeat_TAI_list_of_mau_thu']=dict_thong_ke_repeat_TAI_list_of_mau_thu                       
    more_info_get_from_loop['dict_thong_ke_repeat_XIU_list_of_mau_thu']=dict_thong_ke_repeat_XIU_list_of_mau_thu 
    more_info_get_from_loop['last_cau_value']=last_cau_value                      
    #print 'CAU_LIST_show_repeat',CAU_LIST_show_repeat
    if is_print:
        #print 'CAU_LIST_show_xenke',CAU_LIST_show_xenke
        #print 'repeat_TAI_lists,repeat_XIU_lists',repeat_TAI_lists,repeat_XIU_lists
        #print 'xen_ke_or_giong_nhau_lists',xen_ke_or_giong_nhau_lists
        #print max(k for k, v in dict_thong_ke_repeat_TAI.iteritems())
        print 'dict_thong_ke_repeat_TAI_list_of_mau_thu',dict_thong_ke_repeat_TAI_list_of_mau_thu
        print 'dict_thong_ke_repeat_XIU_list_of_mau_thu',dict_thong_ke_repeat_XIU_list_of_mau_thu
        print 'dict_thong_ke_xen_ke_TAI_list_of_mau_thu',dict_thong_ke_xen_ke_TAI_list_of_mau_thu
        print 'dict_thong_ke_xen_ke_XIU_list_of_mau_thu',dict_thong_ke_xen_ke_XIU_list_of_mau_thu 
    return   repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more_info_get_from_loop
def string_soi_cau(end_phien,so_cau_can_soi):
    qrs = TaiXiu.objects.filter(phien_so__lte = end_phien).order_by('-phien_so')
    string_tai_xiu_soi_cau = ''
    for c,cau in enumerate(qrs):
        print c
        if c == so_cau_can_soi-1:
            return mark_safe(string_tai_xiu_soi_cau)
        current_i = cau.tai_1_xiu_0
        if 0:#c % 19==0:
            xuong_dong = '<br>'
        else:
            xuong_dong = ' '
        if current_i==1:
            #string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "tai-cau"></span>' + xuong_dong
            string_tai_xiu_soi_cau += '<span class = "tai-cau"></span>' + xuong_dong
        else:
            #string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "xiu-cau"></span>' + xuong_dong
            string_tai_xiu_soi_cau +='<span class = "xiu-cau"></span>' + xuong_dong
def wanting_html2(xac_suat_du_thieu,du_tai=None):
        
        if xac_suat_du_thieu < 0:
            if xac_suat_du_thieu <-50:
                wanting_template = '<span class="wanting-in-td-level3">%s</span>'
            elif xac_suat_du_thieu < -30:
                wanting_template = '<span class="wanting-in-td-level2">%s</span>'
            else:
                wanting_template = '<span class="wanting-in-td">%s</span>' 
            template = wanting_template
        else:
            if xac_suat_du_thieu >50:
                redundant_template = '<span class="redundant-in-td-level3">%s</span>'
            elif xac_suat_du_thieu >30 :
                redundant_template = '<span class="redundant-in-td-level2">%s</span>'
            elif xac_suat_du_thieu >0:
                redundant_template = '<span class="redundant-in-td-level1">%s</span>'
            elif xac_suat_du_thieu ==0:
                redundant_template = '<span class="redundant-in-td0">%s</span>'
            template = redundant_template
        if du_tai:
            template_select = '%.1f'
            template = template%template_select
            xac_suat_du_thieu = template%(du_tai) 
        else:
            template_select = '%.1f%%' 
            template = template%template_select
            xac_suat_du_thieu = template%(xac_suat_du_thieu) 
        return xac_suat_du_thieu
def tr_header_tai_or_xiu(header_component,tai_xiu_name):
                return u'<td>%s %s</td>'%(header_component,tai_xiu_name)
current_html_template = '<span class="current-in-td">%s</span>'
not_current_html_template = '<span class="not-current-in-td">%s</span>' 
def create_current_html2(last_cau,tai_repeat_list_count,tai_or_xiu = "tai"):
        if last_cau and tai_or_xiu == "tai":
                tai_repeat_list_count = current_html_template%tai_repeat_list_count
        elif not last_cau and tai_or_xiu == "xiu":
            tai_repeat_list_count = current_html_template%tai_repeat_list_count
        else:
            tai_repeat_list_count = not_current_html_template%tai_repeat_list_count
        return tai_repeat_list_count   
def create_repeat_table_data():
    END_LIST = [32,64,100,256,512,1024,2048,0]
    repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more_info_get_from_loop = soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),END_LIST=END_LIST,is_print = True)
    print more_info_get_from_loop
    TAI_XIU_SHOW_individual = True
    table_big_data = []
    max_tai_xiu = max([more_info_get_from_loop['max_tai'],more_info_get_from_loop['max_xiu']])
    last_cau_value = more_info_get_from_loop['last_cau_value']
    for i_repeat in range(1,max_tai_xiu + 1):
        print 'i_repeat',i_repeat
        row_dict_data_for_one_i_repeat = {}
        row_dict_data_for_one_i_repeat['i_repeat'] = i_repeat
        Probability_theory = float(12.5/pow(2, (i_repeat-1)))
        row_dict_data_for_one_i_repeat['Probability_theory'] = u'%.3f %%'%(Probability_theory)
        
        if TAI_XIU_SHOW_individual:
            SHOW_individual_info = {'table_body_html':['',''],\
                                    'tr_tai_and_xiu_1_mauthu_of_i_repeat':['','']}
            table_body_html = [] 
        else:
            table_body_html=''
        #redundant_or_lack_in_middle_before = {0:0,1:0}
        before_dict = {0:{},1:{}}
        for count,MAU_THU in enumerate(END_LIST):
            #tr_small_table = tr_small_table +'<td>%s</td>'%MAU_THU
            if TAI_XIU_SHOW_individual:
                tr_tai_and_xiu_1_mauthu_of_i_repeat_list = []
            else:
                tr_tai_and_xiu_1_mauthu_of_i_repeat ='' 
            for count_tai_xiu_list,dict_thong_ke_repeat in enumerate(['dict_thong_ke_repeat_TAI_list_of_mau_thu','dict_thong_ke_repeat_XIU_list_of_mau_thu']):
                if count_tai_xiu_list:
                    tai_or_xiu = "xiu"
                else:
                    tai_or_xiu = "tai"
                dict_so_luong_of_14_lan_repeat = more_info_get_from_loop[dict_thong_ke_repeat][MAU_THU]
                try:
                    repeat_n = dict_so_luong_of_14_lan_repeat[i_repeat]
                except KeyError:
                    repeat_n = 0
                repeat_n_theory = Probability_theory*MAU_THU/100
                redundant_or_lack = (repeat_n -  repeat_n_theory)
                redundant_or_lack_percent = (repeat_n -  repeat_n_theory)*100/repeat_n_theory   
                if count == 0:
                    redundant_or_lack_in_middle= ''
                    mau_thu_in_middle= ''
                    repeat_n_theory_in_middle= ''
                    percent_in_middle = ''
                    before_dict[count_tai_xiu_list]['redundant_or_lack_in_middle_before']= redundant_or_lack
                    before_dict[count_tai_xiu_list]['MAU_THU_in_middle_before'] = MAU_THU
                    before_dict[count_tai_xiu_list]['repeat_n_theory_in_middle_before'] = repeat_n_theory
                else:
                    redundant_or_lack_in_middle = redundant_or_lack - before_dict[count_tai_xiu_list]['redundant_or_lack_in_middle_before']
                    mau_thu_in_middle= MAU_THU - before_dict[count_tai_xiu_list]['MAU_THU_in_middle_before']
                    repeat_n_theory_in_middle = repeat_n_theory - before_dict[count_tai_xiu_list]['repeat_n_theory_in_middle_before']
                    percent_in_middle = redundant_or_lack_in_middle*100/repeat_n_theory_in_middle
                    before_dict[count_tai_xiu_list]['redundant_or_lack_in_middle_before'] = redundant_or_lack
                    before_dict[count_tai_xiu_list]['MAU_THU_in_middle_before'] = MAU_THU
                    before_dict[count_tai_xiu_list]['repeat_n_theory_in_middle_before'] = repeat_n_theory
                if redundant_or_lack_in_middle!='':
                    middle_descriptions = (u'%s/%.1f'%(wanting_html2(percent_in_middle,redundant_or_lack_in_middle),repeat_n_theory_in_middle),wanting_html2(percent_in_middle))
                    middle_description = ''.join(map(lambda x:'<td>%s</td>'%x,middle_descriptions))
                    middle_description = '<table class="up-margin">%s</table>'%middle_description
                else:
                    middle_description =''
                td_tai_or_xius= ( MAU_THU,create_current_html2(last_cau_value,repeat_n,tai_or_xiu) ,u'%.1f'%repeat_n_theory,wanting_html2(redundant_or_lack_percent,redundant_or_lack),wanting_html2(redundant_or_lack_percent),middle_description)
                td_tai_or_xiu = ''.join(map(lambda x:'<td>%s</td>'%x,td_tai_or_xius))
                if TAI_XIU_SHOW_individual:
                    SHOW_individual_info['tr_tai_and_xiu_1_mauthu_of_i_repeat'][count_tai_xiu_list] = td_tai_or_xiu
                else:
                    tr_tai_and_xiu_1_mauthu_of_i_repeat = tr_tai_and_xiu_1_mauthu_of_i_repeat + td_tai_or_xiu
            if TAI_XIU_SHOW_individual:
                for x in range(0,2):
                    SHOW_individual_info['table_body_html'][x] += '<tr>' + SHOW_individual_info['tr_tai_and_xiu_1_mauthu_of_i_repeat'][x] + '</tr>'
            else:
                table_body_html = table_body_html + '<tr>' + tr_tai_and_xiu_1_mauthu_of_i_repeat + '</tr>'
        header_components = ['Sample','Real','theory_n','redudant or lack','r_l percent','middle des']
        if TAI_XIU_SHOW_individual:
            tr_header = ''.join(map(lambda x:u'<td>%s</td>'%x,header_components))
            table_header = '<thead><tr>%s</tr></thead>'%tr_header
            for x in range(0,2):
                SHOW_individual_info['table_body_html'][x]= u'<table class="table-bordered">%s<tbody>%s</tbody></table>'%(tr_header,SHOW_individual_info['table_body_html'][x])
            new_table_html = u'<table class="table-bordered"><thead><tr><td>TÀI</td><td>XỈU</td><tr></thead><tbody><tr><td>%s</td><td>%s</td></tr></tbody></table>'%(SHOW_individual_info['table_body_html'][0],SHOW_individual_info['table_body_html'][1])
            table_description_html = mark_safe(new_table_html)
            
            #table_description_html = mark_safe(''.join(SHOW_individual_info['table_body_html']))
        else:
            
            tai_xiu_names = ['TAI','XIU']
            tr_header=''
            
            for tai_xiu_name in tai_xiu_names:
                for header_component in  header_components:
                    tr_header +=tr_header_tai_or_xiu(header_component,tai_xiu_name)
                
            #tr_header = '<td>Sample Tài</td><td>Real Tài</td><td>Theory Tài</td><td>r or lack</td><td>percent</td><td>middle des</td><td>Sample Xỉu</td><td>Real xỉu</td><td>theory xỉu</td><td>r or lack xỉu</td><td>percent r or l</td><td>middle des</td>'
            table_header = '<thead><tr>%s</tr></thead>'%tr_header
            table_body_html = u'<tbody>%s</tbody>'%table_body_html
            table_description_html = mark_safe(u'<table class="">%s%s</table>'%(table_header,table_body_html))
        row_dict_data_for_one_i_repeat['tai_xiu_repeat_description'] = table_description_html
        table_big_data.append(row_dict_data_for_one_i_repeat)
    return table_big_data
if __name__ == '__main__':
    #autoimport(last_phien_in_100_user_import = 807649,ALOWED_change= True,save_or_test = True)
    '''

    repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists = soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),END_LIST = [0],is_print = True)
    print 'repeat_TAI_lists',repeat_TAI_lists[0:10]
    print 'repeat_XIU_lists',repeat_XIU_lists[0:10]
    filter_con_11xenkeTAI= filter(lambda x: x.so_luong_cau==11, XEN_KE_TAI_lists)
    print 'filter_con_11xenkeTAI',filter_con_11xenkeTAI
    
    
    print 'len(repeat_XIU_lists)',len(repeat_XIU_lists)
    list_2_vs_above = chon_tren_hoac_duoi_cau_kep(repeat_XIU_lists,so_cau_moc=2)
    print 'chon_tren_hoac_duoi_cau_kep',list_2_vs_above[0:10]
    print 'len(list_2_vs_above)',len(list_2_vs_above)
    repeat_2xiurepeat_lists,repeat_above2_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists = soicau_2(list_2_vs_above,END_LIST = [0],is_print = True)
    print 'repeat_2xiurepeat_lists',repeat_2xiurepeat_lists[0:3]
    print 'len(repeat_2xiurepeat_lists)',len(repeat_2xiurepeat_lists)
    filter_con_12repeat_2conxiu = filter(lambda x: x.so_luong_cau==12, repeat_2xiurepeat_lists)
    print 'filter_con_12repeat_2conxiu',filter_con_12repeat_2conxiu 
    
    raise ValueError
    print 'len(repeat_TAI_lists)',len(repeat_TAI_lists)
    list_3_vs_above = chon_tren_hoac_duoi_cau_kep(repeat_TAI_lists)
    print 'chon_tren_hoac_duoi_cau_kep',list_3_vs_above[0:10]
    print 'len(list_3_vs_above)',len(list_3_vs_above)
    repeat_TAI_lists,repeat_XIU_lists = soicau_2(list_3_vs_above,END_LIST = [0],is_print = True)
    '''
    
    ''''<%(cls)s bound=%(bound)s, valid=%(valid)s, fields=(%(fields)s)>' % {
            'cls': self.__class__.__name__,
            'bound': self.is_bound,
            'valid': is_valid,
            'fields': ';'.join(self.fields),
        }
    '''
    #autoimport(last_phien_in_100_user_import = 809903,ALOWED_change= False,save_or_test = True)
    print create_repeat_table_data()
    pass

