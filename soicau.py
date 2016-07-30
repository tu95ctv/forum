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
from drivingtest.models import TaiXiu, Tb_import
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
def wanting_html_create(xac_suat_du_thieu):
        wanting_template = '<span class="wanting-in-td">(%.2f%%)</span>'    
        redundant_template = '<span class="redundant-in-td">(%.2f%%)</span>'
        if xac_suat_du_thieu < 0:
            xac_suat_du_thieu = wanting_template%xac_suat_du_thieu
        else:
            xac_suat_du_thieu = redundant_template%xac_suat_du_thieu 
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
        xac_suat_con_lai = wanting_html_create(xac_suat_con_lai)
        #count_3_to18_dict[rs_percent ] = i
        print u'tong 3 cau, phan tram, sai so, du_thieu ',i,rs_percent,"%.2f%%" %sai_so,du_thieu
        display_html = " %s ly thuyet %.2f ( %.2f %s %.2f%%)"%(rs,ly_thuyet_ung_voi_mau_thu,du_thieu,xac_suat_con_lai,sai_so)
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
    xen_ke_giong_nhau_bat_dau_tu_TAI_dict = {}
    xen_ke_giong_nhau_bat_dau_tu_XIU_dict = {}
    
    for c,cau in enumerate(tai_xiu_lists):
        if isinstance(tai_xiu_lists, QuerySet):
            current_i = cau.tai_1_xiu_0
        else:
            current_i = cau
        if c<100:
            if c % 19==0:
                xuong_dong = '<br>'
            else:
                xuong_dong = ' '
            if current_i==1:
                string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "tai-cau"></span>' + xuong_dong
                print 'Tai'
            else:
                string_tai_xiu_soi_cau += str(c+1)+' '+'<span class = "xiu-cau"></span>' + xuong_dong
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
        return tai_repeat_list_count
    txxt_dict = {}        
    def tai_xiu_50_50_create_html(tai_sluong,tai_or_xiu ="tai"):
        str_partern = '%s/%.0f [%.1f (%.2f%%) %s]' 
        mau_thu_chia_2 = mau_thu/float(2)
        so_luong_ly_thuyet = mau_thu_chia_2
        du_tai = tai_sluong-mau_thu_chia_2
        phan_tram_du_tai = du_tai*100/float(mau_thu)
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet = du_tai*100/(float(mau_thu)/2)
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
        tai_sluong = create_current_html(last_cau,tai_sluong,tai_or_xiu)
        tai_html = str_partern%(tai_sluong,so_luong_ly_thuyet,du_tai,phan_tram_du_tai,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html)
        return mark_safe(tai_html)
    tai_or_xiu_html = tai_xiu_50_50_create_html(tai_sluong)
    txxt_dict['tai'] = tai_or_xiu_html
    tai_or_xiu_html = tai_xiu_50_50_create_html(xiu_sluong,tai_or_xiu ="xiu")
    txxt_dict['xiu'] = tai_or_xiu_html
    txxt_dict.update({'mau_thu':mau_thu})
    
    txxt_map ={'xiu_tai':xiutai,'xiu_xiu':xiuxiu,'tai_xiu':taixiu,'tai_tai':taitai}
    mau_thu_chia_4 = mau_thu/float(4)
    str_txxt_partern = '%s/%.1f [%.1f %s %s]'
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
        ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
        xac_suat_du_thieu_html = '%.1f%%'%(xac_suat_du_thieu )#wanting_html_create(xac_suat_du_thieu)
        so_luong_thuc_te_html = create_current_html(last_cau,so_luong_thuc_te,tai_or_xiu)
        txxt_dict[k] = mark_safe(str_txxt_partern%(so_luong_thuc_te_html,so_luong_ly_thuyet,so_luong_du_thieu,xac_suat_du_thieu_html,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html))
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
            str_partern = '%s/%.1f [%.1f %s %s]'
            so_luong_thuc_te = tai_repeat_lists.count(i)
            so_luong_ly_thuyet = lythuyet_repeat_xac_suat_i *mau_thu/100
            #sai_so_repeat_tai = (tai_repeat_percent  - lythuyet_repeat_xac_suat_i)*100/float(lythuyet_repeat_xac_suat_i)
            so_luong_du_thieu = (so_luong_thuc_te - so_luong_ly_thuyet)
            xac_suat_du_thieu = (so_luong_thuc_te - lythuyet_repeat_xac_suat_i*mau_thu/100)*100/mau_thu
            ti_le_xac_suat_du_thieu_xacSuatLyThuyet = 100*xac_suat_du_thieu/lythuyet_repeat_xac_suat_i#25: nghia la 25%
            ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html = wanting_html_create(ti_le_xac_suat_du_thieu_xacSuatLyThuyet)
            xac_suat_du_thieu_html = '%.1f%%'%(xac_suat_du_thieu )#wanting_html_create(xac_suat_du_thieu)
            so_luong_thuc_te_html_for_current_cau = create_current_html(last_cau,so_luong_thuc_te,tai_or_xiu = tai_or_xiu)
            td_value = str_partern%(so_luong_thuc_te_html_for_current_cau,so_luong_ly_thuyet,so_luong_du_thieu,xac_suat_du_thieu_html,ti_le_xac_suat_du_thieu_xacSuatLyThuyet_html)
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
        print 'entries',entries,'\n',len(entries)
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
        #print 'entries',entries,'\n',len(entries)
        


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
        tb='tong ket\n,'
        tb += '\n,' + 'last_phien %s'%TaiXiu.objects.latest('phien_so').phien_so
        tb += '\n,' + 'str_phien_co_gia_tri_khac_truoc %s'%str_phien_co_gia_tri_khac_truoc
        tb +='\n,' +'last_phien_in_100_user_import %s'%last_phien_in_100_user_import
        tb +='\n,' +'ly_thuyet_se_co_so_luot_duoc_import %s'%ly_thuyet_se_co_so_luot_duoc_import
        tb +='\n,' +'thuc_te_so_import %s'%thuc_te_so_import
        tb +='\n,' +'quet_qua_ma_khong_duoc_tao %s'%quet_qua_ma_khong_duoc_tao
        tb +='\n,' +'so_phien_bi_khac %s'%so_phien_bi_khac
        print tb
        return tb    
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
def soicau_2():
    TAI  =1
    XIU = 0
    qrs = TaiXiu.objects.all().order_by('-phien_so')[0:100]
    thong_ke_lan_lap_TAI  ={}
    thong_ke_lan_lap_XIU ={}
    so_luong_cau_XIU_trong_nhom = 0
    so_luong_cau_TAI_trong_nhom = 0
    before_diff_same_value 
    for c,cau in enumerate(qrs):
        current_value = cau.tai_1_xiu_0 
        if current_value ==TAI:
            so_luong_cau_TAI_trong_nhom +=1
        else:
            so_luong_cau_XIU_trong_nhom +=1
        if c == 0:
            before_value = current_value
            before_DIFFERENT_SAME_value = current_value
        else:
            if current_value != before_value:
                if before_value == TAI: #current_value la tai
                    try:
                        thong_ke_lan_lap_TAI[so_luong_cau_TAI_trong_nhom] +=1
                    except KeyError:
                        thong_ke_lan_lap_TAI[so_luong_cau_TAI_trong_nhom] =1
                    so_luong_cau_TAI_trong_nhom = 0
                else:
                    try:
                        thong_ke_lan_lap_XIU[so_luong_cau_XIU_trong_nhom] +=1
                    except KeyError:
                        thong_ke_lan_lap_XIU[so_luong_cau_XIU_trong_nhom] =1   
                    so_luong_cau_XIU_trong_nhom = 0
                before_value = current_value
    
    print thong_ke_lan_lap_TAI,thong_ke_lan_lap_XIU 
    print max(k for k, v in thong_ke_lan_lap_TAI.iteritems())
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
            print 'begin '
            Tb_import.thongbao = autoimport() + '\n so lan quet %s',so_lan_quet
            Tb_import.Da_import_xong_global_from_model_module = True
            #print '****Da_import_xong_global_from_model_module',Tb_import.Da_import_xong_global_from_model_module
            i = 5
            while i:
                print i
                i =i-1
                sleep(1)
            so_lan_quet += 1 
if __name__ == '__main__':
    #phien_100_to_html()
    #check_continous()
    #xoa_from()
    #create_how_many_phien_for_same_cau()
    #soicau_2()
    #xen_ke_or_giong_nhau_lists,tai_repeat_lists,xiu_repeat_lists,repeat_dict_lists,txxt_dict_list,string_tai_xiu_soi_cau = create_giong_nhau_khac_nhau_lists(TaiXiu.objects.all().order_by('-phien_so'),show_description = "khong xen ke type",is_created_xenKe_list = True)
    #print len(xen_ke_or_giong_nhau_lists)
    #soicau_2()
    #check_dice_in_script()
    #print get_html('vuachoibai.com/event/Scripts/jquery.ui.touch-punch.min.js')
    #read_html_dice()
    #check_dice_in_script()
    
    #r = requests.get('http://vuachoibai.com/miniluckydice/MiniGameLuckyDice/LuckyDiceSoiCau')
    #print r.text
    autoimport(last_phien_in_100_user_import = None,ALOWED_change= False,save_or_test = True)
    pass
    

    