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
import datetime
from django.db.models.aggregates import Min
import json
SETTINGS_DIR = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(SETTINGS_DIR, 'media')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnDriving.settings')
application = get_wsgi_application()
from drivingtest.models import TaiXiu, TbImport, TenTable, ChartOption,\
    MySelectChartOption, LuuOption
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


from random import randint
xac_suat = {3:0.00462962962962963,4:0.0138888888888889,5:0.0277777777777778,6:0.0462962962962963,7:0.0694444444444444,8:0.0972222222222222,9:0.115740740740741,10:0.125,11:0.125,12:0.115740740740741,13:0.0972222222222222,14:0.0694444444444444,15:0.0462962962962963,16:0.0277777777777778,17:0.0138888888888889,18:0.00462962962962963}
mau_thu = 100000
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
    ##print'tong_3_cau_lists',tong_3_cau_lists
    for i in range(3,19):
        rs_percent = tong_3_cau_lists.count(i)/float(mau_thu)
        sai_so = (rs_percent -xac_suat[i])*100/float(xac_suat[i])
        #count_3_to18_dict[rs_percent ] = i
        ##printu'tổng 3 cầu, phần trăm, sai số ',i,rs_percent,"%.2f%%" %sai_so
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
    ##print'%s lists'%description_for_tai_xiu,tai_xiu_lists
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

                ##print'Tai'
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
    ##print'%s repeat lists'%description_for_tai,tai_repeat_lists
    ##print'%s repeat lists'%description_for_xiu,xiu_repeat_lists
    ##print'len %s repeat list,len %s repeat list'%(description_for_tai,description_for_xiu),len(tai_repeat_lists),len(xiu_repeat_lists)
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
    
    ##print'so luong %s'%description_for_taixiu_diff,xen_ke_or_giong_nhau_lists.count(XEN_KE)
    ##print'so luong %s'%description_for_taixiu_same,xen_ke_or_giong_nhau_lists.count(GIONG_NHAU)
    return xen_ke_or_giong_nhau_lists,tai_repeat_lists,xiu_repeat_lists,repeat_dict_lists,txxt_dict_list,mark_safe(string_tai_xiu_soi_cau)
def check_cau():
    count_import_khong_lien_tuc = 0
    now_phien = TaiXiu.objects.latest('phien_so').phien_so
    ##print'now_phien',now_phien
    qrs = TaiXiu.objects.all().order_by('-phien_so')
    ##printlen(qrs)
    for c,i in enumerate(qrs):
        ###printi.phien_so,i.id
        if c==0:
            bf_p = i.phien_so
        else:
            change =  bf_p - i.phien_so
            if change != 1:
                count_import_khong_lien_tuc +=1
                ##print'before %s ,now %s, change %s'%(bf_p,i.phien_so,change)
                ##print'distance bf %s now %s'%(now_phien - bf_p , now_phien - i.phien_so)
                string_return = u'so phien lien tuc %s, so phien khong duoc luu trong db %s'%(now_phien - bf_p ,change)
                #raise ValueError('fdffddf')
                ##printstring_return
                if count_import_khong_lien_tuc ==1:
                    string_return_real = string_return
            bf_p = i.phien_so
    return string_return_real
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
        ###print'entries',entries,'\n',len(entries)
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
                            ##printstr_phien_co_gia_tri_khac_truoc_1_item,'key value',key,value
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
        ##printtb
        return tb
def autoimport1(html = None,last_phien_in_100_user_import = None,ALOWED_change= False,save_or_test = True):
        ##print'dang get html...'
        if html ==None:
            html = get_html('https://phatloc.vtcgame.vn/tiendoan/OverUnderNew/OverUnderSoiCau?type=1')
        #print  html
        soup = BeautifulSoup(html)
        class_entry_name = '.td_ketqua_soicau'
        entries = soup.select(class_entry_name)
        list_100_phiens = []
        ##print'len(entries)',len(entries)
        for c,entry in enumerate(entries):
            lis = entry.select('li')
            if c==2 or c==6:
                lis.reverse()
            for li in lis:
                instance_dict = {}
                li_title = li['title']#"Tài: 12 (6 3 3)"
                ##print 'li_title',li_title
                rs = re.findall("(\S{3,4}?): (\d+) \((\d) (\d) (\d)\)",li_title)
                tai_or_xiu_string= rs[0][0]
                instance_dict['tong'] = int(rs[0][1])
                instance_dict['cau_1'] = int(rs[0][2])
                instance_dict['cau_2'] = int(rs[0][3])
                instance_dict['cau_3'] = int(rs[0][4])
                if tai_or_xiu_string ==u"Trên":
                    tai_or_xiu = 1
                elif tai_or_xiu_string ==u"Dưới":
                    tai_or_xiu = 0
                instance_dict['tai_1_xiu_0'] =tai_or_xiu
                #instance_dict['phien_so'] =phien
                list_100_phiens.append(instance_dict)
        ##print'len(list_100_phiens)',len(list_100_phiens)
        
        tb='tong ket\n,'
        ###printlist_100_phiens
        try:
            last_phien = TaiXiu.objects.latest('phien_so').phien_so
        except:
            last_phien = 'khong co'
        if last_phien_in_100_user_import:
            phien = last_phien_in_100_user_import-1
        else:#tim 
            lastest_100_cau_in_dbs = TaiXiu.objects.filter(phien_so__gt = last_phien-100 )
            same_100_html_querysets =[]
            qgroup=Q()
            
            for count,i_tim in enumerate(range(98,94,-1)):
                instance_dict = list_100_phiens[i_tim]
                qgroup = reduce(operator.and_, (Q(**{key :value}) for key,value in instance_dict.items()))
                if count ==0:
                    pass
                elif count!=0:
                    instance_dict['phien_so'] = same_100_html_querysets[0].phien_so + 1
                    qgroup_FRNAME = reduce(operator.or_, (Q(**{"phien_so" : (obj.phien_so + 1)}) for obj in same_100_html_querysets ))    
                    qgroup = qgroup & qgroup_FRNAME       
                same_100_html_querysets  = lastest_100_cau_in_dbs.filter(qgroup)
                if len(same_100_html_querysets) ==0:
                    tb ='database khong co cau nao trong 100 cau'
                    print tb
                    return tb
                    #raise ValueError ('databse chua co cau nao trong 100 cau')
            if len(same_100_html_querysets ) == 1:
                last_phien_in_100_user_import = same_100_html_querysets [0].phien_so  + i_tim
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
                        ###print'@@@@@@@@@@da co su khac biet'
                        ###printinstance_dict
                        #for k,v in instance_dict.items():
                            ###printk,getattr(instance, k)
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
        
        ###print'count',count,i_tim,same_100_html_querysets [0].phien_so ,'list_100_phiens',len(list_100_phiens),same_100_html_querysets [0]
        if last_phien == "khong co":
            ly_thuyet_se_co_so_luot_duoc_import = 100
        else:
            ly_thuyet_se_co_so_luot_duoc_import = last_phien_in_100_user_import - last_phien
        tb='tong ket</br>'
        tb += '</br>' + 'last_phien truoc khi import %s'%last_phien
        tb += '</br>' + 'last_phien sau  khi import %s'%TaiXiu.objects.latest('phien_so').phien_so
        tb += '</br>' + 'str_phien_co_gia_tri_khac_truoc %s'%str_phien_co_gia_tri_khac_truoc
        tb +='</br>' +'last_phien_in_100_user_import %s'%last_phien_in_100_user_import
        tb +='</br>' +'ly_thuyet_se_co_so_luot_duoc_import %s'%ly_thuyet_se_co_so_luot_duoc_import
        tb +='</br>' +'thuc_te_so_import %s'%thuc_te_so_import
        tb +='</br>' +'quet_qua_ma_khong_duoc_tao %s'%quet_qua_ma_khong_duoc_tao
        tb +='</br>' +'so_phien_bi_khac %s'%so_phien_bi_khac
        #print tb
        return mark_safe(tb)   
def autoimport_vuachoibai(html = None,last_phien_in_100_user_import = None,ALOWED_change= False,save_or_test = True):
        ##print'dang get html...'
        if html ==None:
            html = get_html('https://phatloc.vtcgame.vn/tiendoan/OverUnderNew/OverUnderSoiCau?type=1')
        #print  html
        soup = BeautifulSoup(html)
        class_entry_name = '.tx_ketqua_soicau'
        entries = soup.select(class_entry_name)
        list_100_phiens = []
        ##print'len(entries)',len(entries)
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
        ##print'len(list_100_phiens)',len(list_100_phiens)
        tb='tong ket\n,'
        ###printlist_100_phiens
        try:
            last_phien = TaiXiu.objects.latest('phien_so').phien_so
        except:
            last_phien = 'khong co'
        if last_phien_in_100_user_import:
            phien = last_phien_in_100_user_import-1
        else:#tim 
            lastest_100_cau_in_dbs = TaiXiu.objects.filter(phien_so__gt = last_phien-100 )
            same_100_html_querysets =[]
            qgroup=Q()
            
            for count,i_tim in enumerate(range(98,94,-1)):
                instance_dict = list_100_phiens[i_tim]
                qgroup = reduce(operator.and_, (Q(**{key :value}) for key,value in instance_dict.items()))
                if count ==0:
                    pass
                elif count!=0:
                    instance_dict['phien_so'] = same_100_html_querysets[0].phien_so + 1
                    qgroup_FRNAME = reduce(operator.or_, (Q(**{"phien_so" : (obj.phien_so + 1)}) for obj in same_100_html_querysets ))    
                    qgroup = qgroup & qgroup_FRNAME       
                same_100_html_querysets  = lastest_100_cau_in_dbs.filter(qgroup)
                if len(same_100_html_querysets) ==0:
                    tb ='database khong co cau nao trong 100 cau'
                    ##printtb
                    return tb
                    #raise ValueError ('databse chua co cau nao trong 100 cau')
            if len(same_100_html_querysets ) == 1:
                last_phien_in_100_user_import = same_100_html_querysets [0].phien_so  + i_tim
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
                        ###print'@@@@@@@@@@da co su khac biet'
                        ###printinstance_dict
                        #for k,v in instance_dict.items():
                            ###printk,getattr(instance, k)
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
        
        ###print'count',count,i_tim,same_100_html_querysets [0].phien_so ,'list_100_phiens',len(list_100_phiens),same_100_html_querysets [0]
        if last_phien == "khong co":
            ly_thuyet_se_co_so_luot_duoc_import = 100
        else:
            ly_thuyet_se_co_so_luot_duoc_import = last_phien_in_100_user_import - last_phien
        tb='tong ket</br>'
        tb += '</br>' + 'last_phien truoc khi import %s'%last_phien
        tb += '</br>' + 'last_phien sau  khi import %s'%TaiXiu.objects.latest('phien_so').phien_so
        tb += '</br>' + 'str_phien_co_gia_tri_khac_truoc %s'%str_phien_co_gia_tri_khac_truoc
        tb +='</br>' +'last_phien_in_100_user_import %s'%last_phien_in_100_user_import
        tb +='</br>' +'ly_thuyet_se_co_so_luot_duoc_import %s'%ly_thuyet_se_co_so_luot_duoc_import
        tb +='</br>' +'thuc_te_so_import %s'%thuc_te_so_import
        tb +='</br>' +'quet_qua_ma_khong_duoc_tao %s'%quet_qua_ma_khong_duoc_tao
        tb +='</br>' +'so_phien_bi_khac %s'%so_phien_bi_khac
        #print tb
        return mark_safe(tb)
    
    
def autoimport(html = None,last_phien_in_100_user_import = None,ALOWED_change= False,save_or_test = True):
    #print 'give me somthing info'
    anhxa = {'gameSessionID':'phien_so','dice1':'cau_1','dice2':'cau_2','dice3':'cau_3','locationIDWin':'tai_1_xiu_0','diceSum':'tong'}
    j= get_html('https://phatloc.vtcgame.vn/tiendoan/api/Minigame/GetSoiCau?type=1')
    
    if j == None:
        #print 'deo co j trong data'
        return None
    #print 'before'
    d = json.loads(j)
    #print 'd,d = json.loads(j)',d
    so_luong_duoc_import = 0
    for cau_dict in d:
        new_anh_xa_obj = {}
        for k,v in cau_dict.iteritems():
            if k != 'locationIDWin':
                new_anh_xa_obj[anhxa[k]] = v 
            else:
                new_anh_xa_obj[anhxa[k]] = v -1
        ###printnew_anh_xa_obj
        try:
            TaiXiu.objects.get(phien_so = new_anh_xa_obj['phien_so'])
        except TaiXiu.DoesNotExist:
            new_instance = TaiXiu(**new_anh_xa_obj)
            new_instance.save()
            so_luong_duoc_import +=1
            ##printso_luong_duoc_import
    tb = u'so_luong_duoc_import %s'%so_luong_duoc_import
    ##printtb        
    return  tb
def xoa_100_cai_cu_nhat():
    qrs = TaiXiu.objects.all().order_by('id')[:100]
    ##printlen(qrs)
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
            ##printrs,x.phien_so
            
            if rs > 1:
                khong_lts.update({x.phien_so:(rs,bf)})
                ##printx.phien_so
            bf = x.phien_so
    ##print'khong_lts',khong_lts
def xoa_from(end=835038):
    qrs = TaiXiu.objects.filter(phien_so__lte =end )
    ##printlen(qrs)
    for x in qrs:
        x.delete()
    qrs = TaiXiu.objects.filter(phien_so__lte =end )
    ##printlen(qrs)                
def create_how_many_phien_for_same_cau():
    re_lists = []
    for i in range(1,20):
        lythuyet_repeat_xac_suat_i = float(12.5/pow(2, (i-1)))
        so_phien_can_thiet=100*1/lythuyet_repeat_xac_suat_i
        #so_phut
        so_phut = so_phien_can_thiet *1.5
        so_gio = so_phut/float(60)
        so_ngay = so_gio/24
        ##printi ,so_phien_can_thiet,'so phut',so_phut,'sogio',so_gio,'so ngay',so_ngay
        re_dict = {'so_lan_lap':i,'xac_suat':lythuyet_repeat_xac_suat_i,'so_phien_can_thiet':so_phien_can_thiet, 'so_phut':so_phut,'so_gio':so_gio,'so_ngay':so_ngay}
        re_lists.append(re_dict)
    return re_lists


def read_html_dice():
    html = read_file_from_disk(MEDIA_ROOT +'/taixiu/html.txt')
    rs = re.findall('<script src="(.*?)"', html, re.IGNORECASE)
    ###print'rs',rs
    
    if 1:
        for i in rs:
            #print i
            pass
    return rs
    ###printhtml  
def get_html(url):    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    html = None 
    for i in xrange(13):
        try:
            html = opener.open(url,timeout=4).read()
            break
        except:
            ##print'Get html.. again for timeout'
            sleep(1)
    return html   
def check_dice_in_script():
    for i in read_html_dice():
        ##printi
        if '//vuachoibai.com' in i:
            i = i.replace('//','')
            continue
        if 'vuachoibai.com' not in i:
            i = 'http://vuachoibai.com/' + i
        script =  get_html(i)
        if 'dice' in script or 'Dice' in script:
            pass
            #print'da tim thay',i
        else:
            pass
            
def insert_item_end_list_delete_begin(ls,end_item):    
    ls.insert(len(ls),end_item)
    ls.remove(ls[0])            
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
        #print 'bat dau'
        TbImport.thongbao = 'begin running'
        so_lan_quet = 0
        thoi_diem_bao_duongs = []
        while (not self.stop) :
            print 'dang soi cau%s'%so_lan_quet
            html = None
            thoi_gian_bao_duong = 0
            while html==None:
                html = get_html('https://phatloc.vtcgame.vn/tiendoan/OverUnderNew/OverUnderSoiCau?type=1')
                                #'http://vuachoibai.com/miniluckydice/MiniGameLuckyDice/LuckyDiceSoiCau')
                if html==None:#baoduong
                    sleep_time_bao_duong =3 
                    thoi_gian_bao_duong +=sleep_time_bao_duong
                    if thoi_gian_bao_duong==sleep_time_bao_duong:
                        if len(thoi_diem_bao_duongs)<10:
                            thoi_diem_bao_duongs.append([datetime.datetime.now(),sleep_time_bao_duong])
                        else:
                            insert_item_end_list_delete_begin(thoi_diem_bao_duongs,[datetime.datetime.now(),sleep_time_bao_duong])
                    else:
                        thoi_diem_bao_duongs[-1][1] = thoi_gian_bao_duong
                    sleep(sleep_time_bao_duong)
                else:
                    pass
            tb=autoimport1(html = html)
            sleep(1)
            TbImport.thongbao =  tb + u'\n so lan quet %s thoi diem bao duong %s'%(so_lan_quet,u' '.join(u'%s %s'%(x,y) for (x,y) in thoi_diem_bao_duongs) )
            sleep(1)
            so_lan_quet += 1
            #print 'not self.stop', self.stop

def chon_tren_hoac_duoi(repeat_XIU_lists,so_be = 0, so_lon =2):
    list_new = []
    for i in repeat_XIU_lists:
        if i == so_lon:
            list_new.append(1)
        elif i >so_lon or (so_be !=0 and i <so_lon and i >=so_be):
            list_new.append(0)
    return list_new
def chon_tren_hoac_duoi_cau_kep(repeat_XIU_lists,so_cau_moc=2):
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
    def __init__(self,phien_ket_thuc=None,\
                 so_luong_cau=None,\
                 same_or_different=None,\
                 bat_dau_la_tai_hay_xiu=None,\
                 ket_thuc_la_tai_hay_xiu = None,\
                 tai_1_xiu_0 = None,
                 phien_bat_dau=None):
        self.phien_so = phien_ket_thuc
        self.phien_bat_dau = phien_bat_dau
        self.so_luong_cau = so_luong_cau
        self.same_or_different = same_or_different
        self.bat_dau_la_tai_hay_xiu = bat_dau_la_tai_hay_xiu
        self.ket_thuc_la_tai_hay_xiu = ket_thuc_la_tai_hay_xiu
        self.tai_1_xiu_0 = tai_1_xiu_0
    def __repr__(self):
        return u'(%s, phien bat dau: %s,sluong:%s,tai1xiu0 %s)'%("TAI begin" if self.bat_dau_la_tai_hay_xiu else "XIU begin" ,self.phien_so,self.so_luong_cau,self.tai_1_xiu_0)
def soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),END_LIST = [32,64,100,256,512,1024,2048,3423434,0],\
             end_phien_to_select_phien=0,is_show_line = False,is_in= False,SAVE_CHART_OPTION = False,TbImport=TbImport):
    LUU_OPTIONS = []
    ONE_OPTION = []
    len_qrs = len(qrs)
    new_end_list = []
    stt_for_option_save = 0
    SAVE_CHART_OPTION_for_only_one_sample_enough = False
    #,'tai':{},'xiu':{},'tai_tai':{},'tai_xiu':{},'xiu_tai':{},'xiu_xiu':{}
    space_MANY_number_sample_list_DICT = {'repeat-tai':{},'repeat-xiu':{},'xenke-tai':{},'xenke-xiu':{},'tai_xiu_ttxx':{}}
    space_MANY_number_sample_dict_BEFORE_DICT = {'repeat-tai':{},'repeat-xiu':{},'xenke-tai':{},'xenke-xiu':{},'tai_xiu_ttxx':{}}
    S_SAMPLEs = [25,50,100,128,200,512,1024]
    SPACE_LENGTH_DICT ={256:12}
    SPACE_LENGTH_DICT_update ={}
    CACH_DI_TIENS = ['gap doi',{1:20,2:25,3:50,4:100}]
    #CACH_DI_TIENS = ['gap doi']
    MAX_SPACE_LENGTH = 40
    series = []#
    series_DICT = {'repeat-tai':{},'repeat-xiu':{},'xenke-tai':{},'xenke-xiu':{},'tai_xiu_ttxx':{}}#{256:series,100:series}
    max_sample_in_END_LIST = len_qrs - end_phien_to_select_phien
    for x in END_LIST:
        if x > max_sample_in_END_LIST :
            x = 0
        if x==0:
            x = max_sample_in_END_LIST 
            if x not in new_end_list:
                new_end_list.append(x)
        elif x <=max_sample_in_END_LIST:
            if x not in new_end_list:
                new_end_list.append(x)
    new_end_list.sort()
    max_sample_in_END_LIST = new_end_list[-1]
    END_LIST  = new_end_list      
    TAI  =1
    XIU = 0
    if 0 in END_LIST:
        END_LIST.remove(0)
        END_LIST.append(len(qrs))
    more_info_get_from_loop = {'max_tai':0,'max_xiu':0,'max_xen_ke_tai':0,'max_xen_ke_xiu':0,'dict_thong_ke_repeat_TAI_list_of_mau_thu':{}}
    END_LIST_index = 0
    END_LIST_index_xen_ke= 0
    
    dict_thong_ke_repeat_TAI  ={}
    dict_thong_ke_repeat_XIU ={}
    dict_thong_ke_XEN_KE_XIU = {}
    dict_thong_ke_XEN_KE_TAI = {}
    dict_thong_ke_so_luong_tai_xiu = {'tai':0,'xiu':0}
    dict_thong_ke_so_luong_ttxx = {'taitai':0,'taixiu':0,'xiutai':0,'xiuxiu':0}
    #dat_tien_template = {2:10, 3:20, 4:40, 5:80, 6:160}
    dat_tien_template = {1:1, 2:2, 3:4, 4:8, 5:16, 6:32, 7:64, 8:128, 9:256, 10:512, 11:1024, 12:2048}
    #dat_tien_template = {1:11, 2:22, 3:33, 4:44, 5:55, 6:66, 7:77, 8:88, 9:256, 10:512, 11:1024, 12:2048}
    CHOI_TOI_delta_lists = [2,3,4]
    CHOI_TOI_delta = 4
    NOT_SHOW_LINE = True
    MIN_CHOI = min(dat_tien_template.keys(), key=int) 
    min_choi_Range = [1,2,3,4]
    so_luong_cau_XIU_trong_nhom = 0
    so_luong_cau_TAI_trong_nhom = 0
    so_luong_cau_XEN_KE_trong_nhom = 0
    repeat_TAI_lists = []
    repeat_XIU_lists = []
    XEN_KE_TAI_lists= []
    XEN_KE_XIU_lists = []
    cau_same_gan_nhat =None
    dict_thong_ke_repeat_TAI_list_of_mau_thu = {}#{32:{1:3,2:2},64:{},100,256,512,1024,2048}
    dict_thong_ke_repeat_XIU_list_of_mau_thu = {}
    dict_thong_ke_xen_ke_TAI_list_of_mau_thu = {}
    dict_thong_ke_xen_ke_XIU_list_of_mau_thu = {}
    
    
    dict_thong_ke_tai_xiu_many_sample = {} #{32:{'tai':13,'xiu':19},64:{'tai':33,'xiu':31}}
    dict_thong_ke_ttxx_many_sample = {} #{32:{'tai':13,'xiu':19},64:{'tai':33,'xiu':31}}
    before_state_same_or_different = "different"
    END_LIST_index_for_tinh_so_luong_tai_xiu = 0
    
    current_group_cau_sign = {'repeat tai':0,'repeat xiu':0,'xenke tai':0,'xenke xiu':0,'taitai':False,'taixiu':False,'xiutai':False,'xiuxiu':False}
    is_already_set_first_for_current_repeat = False
    is_already_set_first_for_current_xenke = False
    is_first_for_current_ttxx = False
    first_is_xenke = False
    input_is_queryset = isinstance(qrs, QuerySet)
    select_key_min_choi_or_not_dict = {}
    for c,cau in enumerate(qrs[end_phien_to_select_phien:end_phien_to_select_phien + max_sample_in_END_LIST]):
        if  isinstance(cau, int):
            current_value = cau
            qrs_is_queryset = False
        else:
            current_value = cau.tai_1_xiu_0
            qrs_is_queryset = True
        if current_value ==TAI:
            so_luong_cau_TAI_trong_nhom +=1
            dict_thong_ke_so_luong_tai_xiu['tai'] +=1
        else:
            so_luong_cau_XIU_trong_nhom +=1
            dict_thong_ke_so_luong_tai_xiu['xiu'] +=1
        if c == 0:
            last_cau_value = current_value
            before_value = current_value
            before_cau_for_repeat = cau
            before_cau_for_xen_ke = cau
        else:
            if current_value != before_value:
                    if before_value == TAI: #current_value la xiu
                        dict_thong_ke_so_luong_ttxx['xiutai'] +=1
                        if not is_first_for_current_ttxx:
                            current_group_cau_sign['xiutai'] = True
                            is_first_for_current_ttxx = True
                        try:
                            dict_thong_ke_repeat_TAI[so_luong_cau_TAI_trong_nhom] +=1
                        except KeyError:
                            dict_thong_ke_repeat_TAI[so_luong_cau_TAI_trong_nhom] =1
                        so_luong_cau_TAI_trong_nhom_number = so_luong_cau_TAI_trong_nhom
                        if so_luong_cau_TAI_trong_nhom > more_info_get_from_loop['max_tai']:
                            more_info_get_from_loop['max_tai'] = so_luong_cau_TAI_trong_nhom
                        if qrs_is_queryset:
                            so_luong_cau_TAI_trong_nhom = Caukep(before_cau_for_repeat.phien_so,\
                                                                 so_luong_cau_TAI_trong_nhom,\
                                                                 same_or_different=0,\
                                                                 bat_dau_la_tai_hay_xiu = before_cau_for_repeat.tai_1_xiu_0,\
                                                                 phien_bat_dau=cau.phien_so)
                        
                        if not is_already_set_first_for_current_repeat:   
                            current_group_cau_sign ['repeat tai'] = so_luong_cau_TAI_trong_nhom_number
                            if input_is_queryset:
                                TbImport.for_make_fighter_dubao_link = {'du bao tai':{'repeat tai':so_luong_cau_TAI_trong_nhom_number + 1},\
                                                                                  'du bao xiu':{'repeat xiu':1}}
                            is_already_set_first_for_current_repeat = True
                            if so_luong_cau_TAI_trong_nhom_number ==1:
                                first_is_xenke = True
                        else:
                            repeat_TAI_lists.append(so_luong_cau_TAI_trong_nhom)
                        so_luong_cau_TAI_trong_nhom = 0
                    elif before_value == XIU:
                        dict_thong_ke_so_luong_ttxx['taixiu'] +=1
                        if not is_first_for_current_ttxx:
                            current_group_cau_sign['taixiu'] = True
                            is_first_for_current_ttxx = True
                        try:
                            dict_thong_ke_repeat_XIU[so_luong_cau_XIU_trong_nhom] +=1
                        except KeyError:
                            dict_thong_ke_repeat_XIU[so_luong_cau_XIU_trong_nhom] =1
                        so_luong_cau_XIU_trong_nhom_number = so_luong_cau_XIU_trong_nhom
                        if so_luong_cau_XIU_trong_nhom > more_info_get_from_loop['max_xiu']:
                            more_info_get_from_loop['max_xiu'] = so_luong_cau_XIU_trong_nhom
                        if qrs_is_queryset:
                            so_luong_cau_XIU_trong_nhom = Caukep(before_cau_for_repeat.phien_so,\
                                                                 so_luong_cau_XIU_trong_nhom,\
                                                                 same_or_different=0,\
                                                                 bat_dau_la_tai_hay_xiu =before_cau_for_repeat.tai_1_xiu_0,\
                                                                 phien_bat_dau=cau.phien_so)
                        if not is_already_set_first_for_current_repeat:   
                            current_group_cau_sign ['repeat xiu'] = so_luong_cau_XIU_trong_nhom_number
                            if input_is_queryset:
                                TbImport.for_make_fighter_dubao_link = {'du bao tai':{'repeat tai': 1},\
                                                                                  'du bao xiu':{'repeat xiu':so_luong_cau_XIU_trong_nhom_number + 1}}
                                ##print'$$$$$$$$$$$$$$$$$$$5',so_luong_cau_XIU_trong_nhom_number
                            is_already_set_first_for_current_repeat = True
                            if so_luong_cau_XIU_trong_nhom_number ==1:
                                first_is_xenke = True
                        else:
                            repeat_XIU_lists.append(so_luong_cau_XIU_trong_nhom)   
                        so_luong_cau_XIU_trong_nhom = 0
                    before_value = current_value
                    before_cau_for_repeat = cau
                    #cho_phep_tach_repeat_or_xenke = 'repeat'
                    so_luong_cau_XEN_KE_trong_nhom +=1
                    if before_state_same_or_different == "same":
                        before_cau_for_xen_ke = cau_same_gan_nhat
                        before_state_same_or_different = "different"
            elif current_value == before_value:
                    before_state_same_or_different = "same"
                    cau_same_gan_nhat = cau
                    if current_value ==TAI:
                        dict_thong_ke_so_luong_ttxx['taitai'] +=1
                        if not is_first_for_current_ttxx:
                            current_group_cau_sign['taitai'] = True
                            is_first_for_current_ttxx = True
                        if so_luong_cau_XEN_KE_trong_nhom >0 :
                            try:
                                dict_thong_ke_XEN_KE_TAI[so_luong_cau_XEN_KE_trong_nhom] +=1
                            except KeyError:
                                dict_thong_ke_XEN_KE_TAI[so_luong_cau_XEN_KE_trong_nhom] =1
                            if not is_already_set_first_for_current_xenke and first_is_xenke:
                                current_group_cau_sign['xenke tai'] = so_luong_cau_XEN_KE_trong_nhom
                                
                                
                                is_already_set_first_for_current_xenke = True
                            if so_luong_cau_XEN_KE_trong_nhom > more_info_get_from_loop['max_xen_ke_tai']:
                                more_info_get_from_loop['max_xen_ke_tai'] = so_luong_cau_XEN_KE_trong_nhom
                            if qrs_is_queryset:
                                so_luong_cau_XEN_KE_trong_nhom = Caukep(before_cau_for_xen_ke.phien_so,\
                                                                        so_luong_cau_XEN_KE_trong_nhom,\
                                                                        same_or_different=1,\
                                                                        bat_dau_la_tai_hay_xiu =cau.tai_1_xiu_0,
                                                                        phien_bat_dau=cau.phien_so)
                            XEN_KE_TAI_lists.append(so_luong_cau_XEN_KE_trong_nhom)      
                    elif current_value ==XIU:
                        dict_thong_ke_so_luong_ttxx['xiuxiu'] +=1
                        if not is_first_for_current_ttxx:
                            current_group_cau_sign['xiuxiu'] = True
                            is_first_for_current_ttxx = True
                        if so_luong_cau_XEN_KE_trong_nhom > 0:
                            try:
                                dict_thong_ke_XEN_KE_XIU[so_luong_cau_XEN_KE_trong_nhom] +=1
                            except KeyError:
                                dict_thong_ke_XEN_KE_XIU[so_luong_cau_XEN_KE_trong_nhom] =1
                            if not is_already_set_first_for_current_xenke and first_is_xenke:
                                key = 'xenke xiu'
                                current_group_cau_sign[key] = so_luong_cau_XEN_KE_trong_nhom
                                '''
                                if input_is_queryset:
                                    #TbImport.for_make_fighter_dubao_link = {'du bao tai':{'repeat tai': 1},\
                                                                                  #'du bao xiu':{'repeat xiu':so_luong_cau_XIU_trong_nhom_number + 1}}
                                    #last_cau_value
                                    if last_cau_value ==1:
                                        last_cau_value_str = 'tai'
                                    else:
                                        last_cau_value_str = 'xiu'
                                    for du_bao in ['tai','xiu']:
                                        if du_bao != last_cau_value_str:
                                            key_du_bao = 'du bao ' + du_bao
                                            v_tam = TbImport.for_make_fighter_dubao_link[key_du_bao]
                                            v_tam.update({key:so_luong_cau_XEN_KE_trong_nhom+1})
                                            
                                '''
                                is_already_set_first_for_current_xenke = True
                            if so_luong_cau_XEN_KE_trong_nhom > more_info_get_from_loop['max_xen_ke_xiu']:
                                more_info_get_from_loop['max_xen_ke_xiu'] = so_luong_cau_XEN_KE_trong_nhom
                            if qrs_is_queryset:
                                so_luong_cau_XEN_KE_trong_nhom = Caukep(before_cau_for_xen_ke.phien_so,\
                                                                        so_luong_cau_XEN_KE_trong_nhom,\
                                                                        same_or_different=1,\
                                                                        bat_dau_la_tai_hay_xiu =cau.tai_1_xiu_0,
                                                                        phien_bat_dau=cau.phien_so)
                            XEN_KE_XIU_lists.append(so_luong_cau_XEN_KE_trong_nhom)
                    so_luong_cau_XEN_KE_trong_nhom = 0  
                    #cho_phep_tach_repeat_or_xenke = 'xenke' 
            for S_SAMPLE in S_SAMPLEs:
                SPACE_LENGTH  = SPACE_LENGTH_DICT.setdefault(S_SAMPLE,0)
                divmod_result = divmod(c, S_SAMPLE)
                if divmod_result[1]==S_SAMPLE-1 and (SPACE_LENGTH ==0 or divmod_result[0]<max(SPACE_LENGTH,MAX_SPACE_LENGTH)   ):
                    for i in ['repeat-tai','repeat-xiu','xenke-tai','xenke-xiu','tai_xiu_ttxx']:
                        space_1_number_sample_dict_before = space_MANY_number_sample_dict_BEFORE_DICT[i].get(S_SAMPLE, {})
                        if i =='repeat-tai':
                            dict_thong_ke_tam = dict_thong_ke_repeat_TAI
                        elif i =='repeat-xiu':
                            dict_thong_ke_tam = dict_thong_ke_repeat_XIU
                        elif i =='xenke-tai':
                            dict_thong_ke_tam = dict_thong_ke_XEN_KE_TAI
                        elif i =='xenke-xiu':
                            dict_thong_ke_tam = dict_thong_ke_XEN_KE_XIU
                        elif i =='tai_xiu_ttxx':
                            dict_thong_ke_tam = {}
                            dict_thong_ke_tam.update(dict_thong_ke_so_luong_tai_xiu)
                            dict_thong_ke_tam.update(dict_thong_ke_so_luong_ttxx)
                            
                        
                        
                        space_1_number_sample_dict_now = {key: dict_thong_ke_tam[key] - space_1_number_sample_dict_before.get(key, 0) for key in dict_thong_ke_tam.keys()}
                        try:
                            space_MANY_number_sample_list_DICT[i][S_SAMPLE].append(space_1_number_sample_dict_now)
                        except KeyError:
                            space_MANY_number_sample_list_DICT[i][S_SAMPLE] = [space_1_number_sample_dict_now]
                        space_1_number_sample_dict_before = dict_thong_ke_tam.copy()
                        space_MANY_number_sample_dict_BEFORE_DICT[i][S_SAMPLE] = space_1_number_sample_dict_before
                    
                    SPACE_LENGTH_DICT_update[S_SAMPLE] = SPACE_LENGTH_DICT_update.setdefault(S_SAMPLE,0) +1
            if c == END_LIST[END_LIST_index_for_tinh_so_luong_tai_xiu]-1:
                copy_dict = dict_thong_ke_so_luong_tai_xiu.copy()
                dict_thong_ke_tai_xiu_many_sample[END_LIST[END_LIST_index_for_tinh_so_luong_tai_xiu]]  = copy_dict
                copy_dict = dict_thong_ke_so_luong_ttxx.copy()
                dict_thong_ke_ttxx_many_sample[END_LIST[END_LIST_index_for_tinh_so_luong_tai_xiu]]  = copy_dict
                END_LIST_index_for_tinh_so_luong_tai_xiu +=1  
            #if c >= END_LIST[END_LIST_index]-1 and cho_phep_tach_repeat_or_xenke=='repeat' or c==max_sample_in_END_LIST - 1:
            if c >= END_LIST[END_LIST_index]-1  or c==max_sample_in_END_LIST - 1:
                #cho_phep_tach_REPEAT_neu_du_so_luong = False
                copy_dict  = dict_thong_ke_repeat_TAI.copy()
                dict_thong_ke_repeat_TAI_list_of_mau_thu [END_LIST[END_LIST_index]] = copy_dict
                copy_dict  = dict_thong_ke_repeat_XIU.copy()
                dict_thong_ke_repeat_XIU_list_of_mau_thu [END_LIST[END_LIST_index]] = copy_dict
                END_LIST_index +=1

                if  c==max_sample_in_END_LIST - 1:
                    if  END_LIST_index !=len(END_LIST):
                        for i in range(END_LIST_index,len(END_LIST)):
                            dict_thong_ke_repeat_XIU_list_of_mau_thu [END_LIST[i]] = copy_dict
            if c >= END_LIST[END_LIST_index_xen_ke]-1  or c==max_sample_in_END_LIST - 1:
            #if c >= END_LIST[END_LIST_index_xen_ke]-1 and cho_phep_tach_repeat_or_xenke=='xenke' or c==max_sample_in_END_LIST - 1:
                #cho_phep_tach_XEN_KE_neu_du_so_luong = False
                copy_dict  = dict_thong_ke_XEN_KE_TAI.copy()
                dict_thong_ke_xen_ke_TAI_list_of_mau_thu [END_LIST[END_LIST_index_xen_ke]] = copy_dict
                copy_dict  = dict_thong_ke_XEN_KE_XIU.copy()
                dict_thong_ke_xen_ke_XIU_list_of_mau_thu[END_LIST[END_LIST_index_xen_ke]] = copy_dict
                END_LIST_index_xen_ke +=1
                if  c==max_sample_in_END_LIST - 1:
                    if  END_LIST_index !=len(END_LIST):
                        for i in range(END_LIST_index,len(END_LIST)):
                            dict_thong_ke_repeat_XIU_list_of_mau_thu [END_LIST[i]] = copy_dict
    
    SPACE_LENGTH_DICT.update(SPACE_LENGTH_DICT_update)
    
    
    categories_dict = {}
    for S_SAMPLE in S_SAMPLEs:
        #print 'S_SAMPLE',S_SAMPLE
        for chart_type in ['repeat-tai','repeat-xiu','xenke-tai','xenke-xiu','tai_xiu_ttxx']:
            try:
                list_of_thong_ke_dict_many_space = space_MANY_number_sample_list_DICT[chart_type][S_SAMPLE]#
            except KeyError:
                continue
            series = []
            if chart_type =='tai_xiu_ttxx':
                range_for_lines = ['tai','xiu','taitai','taixiu','xiutai','xiuxiu']#[{'xiuxiu': 23, 'xi
            else:
                range_for_lines = range(1,20)
                data_of_result_list_dict = {'MIN_CHOI 2':[],'MIN_CHOI 1':[],'MIN_CHOI 3':[],'MIN_CHOI 4':[]}
            result_tongs = {}
            len_range_for_lines = len(range_for_lines) - 1 
            so_lan_thang_thuas_for_min_choi_dict = {}
            for line_count,one_repeat_line in enumerate(range_for_lines):
                cho_phep_ton_tai_this_line = False
                name_and_data_of_one_Repeat_line_dict = {}
                if chart_type == 'repeat-tai' or chart_type =='repeat-xiu': 
                    Probability_theory = float(12.5/pow(2, (one_repeat_line-1)))
                elif chart_type == 'xenke-tai' or chart_type =='xenke-xiu': 
                    Probability_theory = float(12.5/pow(2, (one_repeat_line)))
                elif chart_type == 'tai_xiu_ttxx':
                    if one_repeat_line == 'tai'or one_repeat_line =='xiu':
                        Probability_theory = 50
                    else:
                        Probability_theory = 25
                chart_line_name =    '%s-%s'%(chart_type,one_repeat_line)
                name_and_data_of_one_Repeat_line_dict["name"] ="%s-xs_%.2f_s"%(chart_line_name,Probability_theory*S_SAMPLE/100)
                space_lists_datas = []
                
                len_list_of_thong_ke_dict_many_space = len(list_of_thong_ke_dict_many_space) - 1
                for space_for_spot_count_tinh_result,space_i_dict in enumerate(list_of_thong_ke_dict_many_space):
                    if line_count ==0:
                        try:
                            categories_dict[S_SAMPLE].append('%s_%s'%(space_for_spot_count_tinh_result,space_for_spot_count_tinh_result*S_SAMPLE))
                        except KeyError:
                            categories_dict[S_SAMPLE] = ['0'] 
                    try:
                        repeat_value = space_i_dict[one_repeat_line]
                        cho_phep_ton_tai_this_line = True
                    except KeyError:
                        repeat_value = 0
                    space_lists_datas.append(repeat_value)
                    
                    # tinh ket qua thắng thua
                    if chart_type !='tai_xiu_ttxx':
                        for min_choi_i in min_choi_Range:
                            for CHOI_TOI_delta in CHOI_TOI_delta_lists:
                                cau_choi_toi = min_choi_i + CHOI_TOI_delta -1
                                
                                for count_cach_di_tien,cach_di_tien in enumerate(CACH_DI_TIENS):
                                #####
                                    if cach_di_tien =='gap doi':
                                        key_min_choi = 'MIN_CHOI %s to %s'%(min_choi_i,cau_choi_toi)
                                    else:
                                        key_min_choi = 'MIN_CHOI %s to %s di tien'%(min_choi_i,cau_choi_toi)
                                    select = select_key_min_choi_or_not_dict.get(key_min_choi,None)
                                    if SAVE_CHART_OPTION_for_only_one_sample_enough ==False or select ==None:
                                        stt_for_option_save +=1
                                        try:
                                            instance = ChartOption.objects.get(Name = key_min_choi )
                                            select = instance.is_select_or_not
                                            select_key_min_choi_or_not_dict [key_min_choi] = select
                                            if 1: 
                                                #print 'check coi co option chart nay chua',key_min_choi
                                                instance.stt = stt_for_option_save
                                                instance.save()
                                        except ChartOption.DoesNotExist:
                                            if SAVE_CHART_OPTION:
                                                instance = ChartOption(Name = key_min_choi,stt=stt_for_option_save)
                                                instance.save()
                                                #print 'da saved'
                                            select = False
                                            select_key_min_choi_or_not_dict [key_min_choi]  = False
                                            
                                    if select ==False:
                                        continue
                                    
                                    try:
                                        data_of_result_list = data_of_result_list_dict.setdefault(key_min_choi,[])
                                        result_dat_tam = data_of_result_list[space_for_spot_count_tinh_result]
                                    except IndexError:
                                        result_dat_tam = 0
                                    if one_repeat_line >= min_choi_i :
                                        CON_DEO_CHOI = min_choi_i + CHOI_TOI_delta
                                        #thua = sum (pow(2,count) for count,min_choi_i in enumerate(range(min_choi_i,one_repeat_line if one_repeat_line< CON_DEO_CHOI else CON_DEO_CHOI)))
                                        if cach_di_tien =='gap doi':
                                            thua = sum (pow(2,count) for count,min_choi_i in enumerate(range(min_choi_i,one_repeat_line if one_repeat_line< CON_DEO_CHOI else CON_DEO_CHOI)))
                                        else:
                                            thua = sum (cach_di_tien[count + 1] for count,min_choi_i in enumerate(range(min_choi_i,one_repeat_line if one_repeat_line< CON_DEO_CHOI else CON_DEO_CHOI)))
                                            thua = thua/float(20)
                                        if one_repeat_line < CON_DEO_CHOI:
                                            #thang = pow(2,one_repeat_line - min_choi_i )
                                            if cach_di_tien =='gap doi':
                                                thang = pow(2,one_repeat_line - min_choi_i )
                                            else:
                                                thang = cach_di_tien[one_repeat_line-min_choi_i + 1]
                                                thang = thang/float(20)
                                        else:
                                            thang = 0
                                        thang_or_thua_delta = (thang - thua)*repeat_value
                                        result_dat_tam += thang_or_thua_delta
                                        
                                        result_tong = result_tongs.setdefault(key_min_choi,0)
                                        result_tong +=thang_or_thua_delta
                                        result_tongs[key_min_choi] = result_tong
                                        
                                    try:
                                        data_of_result_list_dict[key_min_choi][space_for_spot_count_tinh_result] = result_dat_tam
                                    except IndexError:
                                        data_of_result_list_dict[key_min_choi].append(result_dat_tam)
                                    if line_count ==len_range_for_lines:
                                        lists = so_lan_thang_thuas_for_min_choi_dict.setdefault(key_min_choi,[0,0])
                                        if result_dat_tam > 0:
                                            keyindex = 0
                                        elif result_dat_tam < 0:
                                            keyindex = 1
                                        else:
                                            keyindex = None
                                        if keyindex != None:
                                            try:
                                                kq_truoc = lists[keyindex]
                                            except IndexError:
                                                kq_truoc = 0
                                            kq_truoc +=1   
                                            lists[keyindex] = kq_truoc  
                                    if line_count ==len_range_for_lines and space_for_spot_count_tinh_result ==len_list_of_thong_ke_dict_many_space:#ket thuc vong lon, vong nho
                                        result_danh = {}
                                        so_lan_thang_thua = 'thang %s thua %s'%(so_lan_thang_thuas_for_min_choi_dict[key_min_choi][0],so_lan_thang_thuas_for_min_choi_dict[key_min_choi][1])
                                        result_danh["name"] = chart_type +' ket qua ' + key_min_choi + '(' + str(CHOI_TOI_delta) + ')'+ ' %s'%result_tongs[key_min_choi] +' ' + so_lan_thang_thua
                                        result_danh['data'] = data_of_result_list_dict[key_min_choi] 
                                        series.append(result_danh)
                                ######
                        SAVE_CHART_OPTION_for_only_one_sample_enough = True                
                
                name_and_data_of_one_Repeat_line_dict["data"] = space_lists_datas
                if cho_phep_ton_tai_this_line and is_show_line :#NOT_SHOW_LINE
                    series.append(name_and_data_of_one_Repeat_line_dict)
            #phai loop qua het repeat range moi co duoc result
            
       
            series_DICT[chart_type][S_SAMPLE] = series
        
    if input_is_queryset:
        TbImport.current_group_cau_sign = current_group_cau_sign
        TbImport.how_many_current_is_repeat_tai_or_xiu =current_group_cau_sign
        
        if last_cau_value ==1:
            last_cau_value_str = 'tai'
        else:
            last_cau_value_str = 'xiu'
        for du_bao in ['tai','xiu']:
            key_du_bao = 'du bao ' + du_bao
            if du_bao != last_cau_value_str:
                for xen_ke in ['tai','xiu']:
                    xen_ke_key = 'xenke ' + xen_ke
                    xen_ke_tai_or_xiu_current_count = current_group_cau_sign[xen_ke_key]
                    if xen_ke_tai_or_xiu_current_count:# ton tai 1 xen ke
                        break
                if xen_ke_tai_or_xiu_current_count:
                    du_bao_xen_ke_tai_or_xiu__count = xen_ke_tai_or_xiu_current_count+1
                else:
                    xen_ke_key = 'xenke ' + last_cau_value_str
                    du_bao_xen_ke_tai_or_xiu__count = 1
                v_tam = TbImport.for_make_fighter_dubao_link[key_du_bao]
                v_tam.update({xen_ke_key:du_bao_xen_ke_tai_or_xiu__count})
            else:
                pass#bo qua ko can phai them key xen ke tai 
                #for xen_ke in ['tai','xiu']:
                    #current_group_cau_sign = {'repeat tai':0,'repeat xiu':0,'xenke tai':0,'xenke xiu':0,'taitai':False,'taixiu':False,'xiutai':False,'xiuxiu':False}
                    #xen_ke_tai_or_xiu_count = current_group_cau_sign['xenke ' + xen_ke]
                    #TbImport.for_make_fighter_dubao_link[key_du_bao]
    print 'TbImport.for_make_fighter_dubao_link',TbImport.for_make_fighter_dubao_link                
    more_info_get_from_loop['dict_thong_ke_repeat_TAI_list_of_mau_thu']=dict_thong_ke_repeat_TAI_list_of_mau_thu                       
    more_info_get_from_loop['dict_thong_ke_repeat_XIU_list_of_mau_thu']=dict_thong_ke_repeat_XIU_list_of_mau_thu
    more_info_get_from_loop['dict_thong_ke_xen_ke_TAI_list_of_mau_thu']=dict_thong_ke_xen_ke_TAI_list_of_mau_thu                       
    more_info_get_from_loop['dict_thong_ke_xen_ke_XIU_list_of_mau_thu']=dict_thong_ke_xen_ke_XIU_list_of_mau_thu
    more_info_get_from_loop['dict_thong_ke_tai_xiu_many_sample']=dict_thong_ke_tai_xiu_many_sample
    more_info_get_from_loop['dict_thong_ke_ttxx_many_sample']=dict_thong_ke_ttxx_many_sample 
    more_info_get_from_loop['last_cau_value']=last_cau_value
    more_info_get_from_loop['current_group_cau_sign']=current_group_cau_sign
    more_info_get_from_loop['series_DICT']=series_DICT
    more_info_get_from_loop['categories_dict']=categories_dict
    max_xen_ke = max([more_info_get_from_loop['max_xen_ke_tai'],more_info_get_from_loop['max_xen_ke_xiu']])
    max_tai_xiu = max([more_info_get_from_loop['max_tai'],more_info_get_from_loop['max_xiu']])
    more_info_get_from_loop['max_xen_ke'] = max_xen_ke
    more_info_get_from_loop['max_tai_xiu'] = max_tai_xiu
    more_info_get_from_loop['New_END_LIST'] = new_end_list                          
    if is_in:
        pass
        print'current_group_cau_sign',current_group_cau_sign
        print'dict_thong_ke_repeat_TAI_list_of_mau_thu',dict_thong_ke_repeat_TAI_list_of_mau_thu
        print'dict_thong_ke_repeat_XIU_list_of_mau_thu',dict_thong_ke_repeat_XIU_list_of_mau_thu
        print'dict_thong_ke_xen_ke_TAI_list_of_mau_thu',dict_thong_ke_xen_ke_TAI_list_of_mau_thu
        print'dict_thong_ke_xen_ke_XIU_list_of_mau_thu',dict_thong_ke_xen_ke_XIU_list_of_mau_thu 
        ##print'@@@space_MANY_number_sample_list_DICT',space_MANY_number_sample_list_DICT
        ##print'@@@series_DICT',series_DICT
        #print'@@@SPACE_LENGTH_DICT',SPACE_LENGTH_DICT
        #print'@@@categories_dict',categories_dict
    return   repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more_info_get_from_loop

def string_soi_cau(end_phien,so_cau_can_soi,description_is_brief_return = False):
    qrs = TaiXiu.objects.filter(phien_so__lte = end_phien).order_by('-phien_so')
    string_tai_xiu_soi_cau = ''
    sluong_tai = 0
    sluong_xiu = 0
    tile_sample = 100
    max_t = max([tile_sample,so_cau_can_soi])
    ##print'max_t',max_t
    for c,cau in enumerate(qrs):
        if c ==0:
            end_cau = cau
        xuong_dong=''
        current_i = cau.tai_1_xiu_0
        if current_i==1:
            sluong_tai +=1
            string_tai_xiu_soi_cau += '<span class = "tai-cau cau-for-tooltip" title="%s %s id_delta %s"></span>'%(cau.phien_so,(cau.phien_so-end_cau.phien_so-1),(cau.id-end_cau.id-1)) + xuong_dong
        else:
            sluong_xiu +=1
            string_tai_xiu_soi_cau +='<span class = "xiu-cau cau-for-tooltip"  title="%s %s id_delta %s" ></span>'%(cau.phien_so,(cau.phien_so-end_cau.phien_so-1),(cau.id-end_cau.id-1))+ xuong_dong
        if c == so_cau_can_soi-1:
            return_value =  [mark_safe(u'<div class="soi-cau-trang-den">%s</div>'%string_tai_xiu_soi_cau),end_cau,cau]#aggregate_result['phien_so__min'],aggregate_result['id__min']
        if c==tile_sample-1:
            ti_le_tai_xiu_trong_100_cau = u'100-tai:%s,xiu:%s'%(sluong_tai,sluong_xiu) 
        if c== max_t-1:
            ###print'return_value',return_value
            return_value.append(ti_le_tai_xiu_trong_100_cau)
            return return_value
# co dung 04:00 01/09/
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
        if du_tai !=None:
            template_select = '%.1f'
            template = template%template_select
            xac_suat_du_thieu = template%(du_tai) 
        else:
            template_select = '%.1f%%' 
            template = template%template_select
            xac_suat_du_thieu = template%(xac_suat_du_thieu) 
        return xac_suat_du_thieu

current_html_template = '<span class="current-in-td">%s</span>'
not_current_html_template = '<span class="not-current-in-td">%s</span>' 
def create_current_html_depend_last_cau(last_cau,value,tai_or_xiu = "tai"):
        if last_cau and tai_or_xiu == "tai":
                rt = current_html_template%value
        elif not last_cau and tai_or_xiu == "xiu":
            rt = current_html_template%value
        else:
            rt = not_current_html_template%value
        return rt
def create_modal_link(repeat_n,i_repeat,MAU_THU,fighter_or_single,tai_or_xiu,repeat_or_xen_ke,so_cau_moc_if_fighter_for_find_cau_list_link):
    link = '/omckv2/modelmanager/FindCauListForm/new/?i_repeat=%s&MAU_THU=%s&fighter_or_single=%s&tai_or_xiu=%s&repeat_or_xen_ke=%s%s'\
    %(i_repeat,MAU_THU,fighter_or_single,tai_or_xiu,repeat_or_xen_ke,
      '&so_cau_moc_if_fighter_for_find_cau_list_link=%s'%so_cau_moc_if_fighter_for_find_cau_list_link if so_cau_moc_if_fighter_for_find_cau_list_link else ''
      )
    link = '<a class="show-modal-table-link" href=%s>%s</a>'%(link,repeat_n)
    return link
    return mark_safe(link)
def create_span_order_to_color(value,color):
    return u'<span style="color:%s">%s</span>'%(color,value)
current_group_html_template = '<span class="current-in-td">%s</span>'
not_current_group_html_template = '<span class="not-current-in-td">%s</span>' 
def color_current_sign(is_color,value):
        if is_color:
                value = current_group_html_template%value
        else:
            value = not_current_group_html_template%value
        return value

def create_repeat_table_data2(more_info_get_from_loop=None,
                              END_LIST=None,\
                              repeat_or_xen_ke = 'repeat',# để chọn dict xen ke hay repeat từ more_info
                              fighter_or_single = "single",
                              so_cau_moc_if_fighter_for_find_cau_list_link = None,
                              repeatxenke_table_or_tai_xiu_tttxx_table = "create repeat or xenke table",
                              TbImport = TbImport,
                              ):
    #current_group_cau_sign = {'repeat tai':0,'repeat xiu':0,'xenke tai':0,'xenke xiu':0,'taitai':False,'taixiu':False,'xiutai':False,'xiuxiu':False}
    print 'abc'
    current_group_cau_sign = more_info_get_from_loop['current_group_cau_sign']
    is_color = None
    if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
        if repeat_or_xen_ke == 'repeat':
            tai_xiu_list_or_xen_ke_lists_name_for_choose_type = ['dict_thong_ke_repeat_TAI_list_of_mau_thu','dict_thong_ke_repeat_XIU_list_of_mau_thu']
            max_tai_xiu = more_info_get_from_loop['max_tai_xiu']
            
        else:
            tai_xiu_list_or_xen_ke_lists_name_for_choose_type = ['dict_thong_ke_xen_ke_TAI_list_of_mau_thu','dict_thong_ke_xen_ke_XIU_list_of_mau_thu']
            max_tai_xiu = more_info_get_from_loop['max_xen_ke']
        i_repeat_range = range(1,max_tai_xiu + 1)
    elif repeatxenke_table_or_tai_xiu_tttxx_table == "create taixiu table" :
        tai_xiu_list_or_xen_ke_lists_name_for_choose_type = ['dict_thong_ke_tai_xiu_many_sample']
        i_repeat_range = ['tai','xiu']
        row_Probability_theory_dict ={}
        row_td_contain_table_data_dict ={}
    elif repeatxenke_table_or_tai_xiu_tttxx_table == "create ttxx table" :
        tai_xiu_list_or_xen_ke_lists_name_for_choose_type = ['dict_thong_ke_ttxx_many_sample']
        i_repeat_range = ['taitai','taixiu','xiutai','xiuxiu']
        row_Probability_theory_dict ={}
        row_td_contain_table_data_dict ={}
        
        
    table_big_data_lists = []
    last_cau_value = more_info_get_from_loop['last_cau_value']
    
    header_components = ['xs','Sam','Real','theory','r_l','r_l %','middle des']
    tr_header = ''.join(map(lambda x:u'<td>%s</td>'%x,header_components))
    table_header = '<thead><tr>%s</tr></thead>'%tr_header
        
        
    for i_repeat in i_repeat_range:
        exclude_now_table_body_html_for_tai_or_xiu = []
        row_dict_data_for_one_i_repeat = {}
        if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
            if repeat_or_xen_ke == 'repeat':
                Probability_theory = float(12.5/pow(2, (i_repeat-1)))
            else:
                Probability_theory = float(12.5/pow(2, (i_repeat)))
            row_dict_data_for_one_i_repeat['Probability_theory'] = u'%.3f %%'%(Probability_theory)
            row_dict_data_for_one_i_repeat['i_repeat'] = i_repeat
        else:
            row_dict_data_for_one_i_repeat['i_repeat'] = i_repeat
            tai_or_xiu = 'tai' if re.match('^tai', i_repeat) else 'xiu'
            
            if i_repeat =='tai' or i_repeat=="xiu":
                Probability_theory = 50
            else:
                Probability_theory = 25
            row_Probability_theory_dict[i_repeat] = u'%.3f %%'%(Probability_theory)
        link_row_data_table = {'link_tai':'','link_xiu':''}
        link_row_data_table_active = {'link_tai':'','link_xiu':''}
        for count_tai_xiu,dict_thong_ke_repeat_name in enumerate(tai_xiu_list_or_xen_ke_lists_name_for_choose_type):
            table_body_html_for_tai_or_xiu = ''
            
            # DEFINE COLOR
            if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
                if count_tai_xiu==0:
                    tai_or_xiu = "tai"
                else:
                    tai_or_xiu = "xiu"
                cau_sign_key = repeat_or_xen_ke + ' ' + tai_or_xiu
                current_group_cau = current_group_cau_sign [cau_sign_key]
                if current_group_cau == i_repeat:
                    is_color = True
                else:
                    is_color = False
                def create_symbol():
                    if 'fighter' in fighter_or_single:
                        if tai_or_xiu =='tai':
                            taixiu_or_bangLonHon = 'equal'
                            taixiu_or_bangLonHon_show = create_span_order_to_color(taixiu_or_bangLonHon, '#B5AFAE')
                        else:
                            taixiu_or_bangLonHon = 'greater'
                            taixiu_or_bangLonHon_show = create_span_order_to_color(taixiu_or_bangLonHon, '#F29DFA')
                        fighter_or_single_for_id = u'%s%s'%(fighter_or_single,so_cau_moc_if_fighter_for_find_cau_list_link)
                        
                        if fighter_or_single == 'fighter_tai':
                            fighter_or_single_show = u'<span style="color:red">fighter_</span><span style="color:black">tai%s</span>'
                        else:
                            fighter_or_single_show = u'<span style="color:red">fighter_</span><span style="color:Fuchsia">xiu%s</span>'
                        fighter_or_single_for_show = fighter_or_single_show%so_cau_moc_if_fighter_for_find_cau_list_link
                    else:
                        taixiu_or_bangLonHon = tai_or_xiu
                        taixiu_or_bangLonHon_show = taixiu_or_bangLonHon
                        fighter_or_single_for_id = fighter_or_single
                        fighter_or_single_for_show = fighter_or_single
                    i_repeat_show = u'<span style="color:green">%stimes</span>'%i_repeat
                    if repeat_or_xen_ke == 'xenke':
                        repeat_or_xen_ke_show = u''.join([create_span_order_to_color(x,'black') if c%2==0 else create_span_order_to_color(x,'white') for c,x in enumerate(repeat_or_xen_ke)])
                    else:
                        repeat_or_xen_ke_show = repeat_or_xen_ke
                    return (u'%s-%s-%s-%stimes'%(repeat_or_xen_ke,taixiu_or_bangLonHon,fighter_or_single_for_id,i_repeat),\
                            u'%s-%s-%s-%s'%(repeat_or_xen_ke_show,taixiu_or_bangLonHon_show,fighter_or_single_for_show,i_repeat_show),)
                symbol = create_symbol()
                symbol_id = symbol[0]
                symbol_view = symbol[1]
                row_dict_data_for_one_i_repeat['symbol_%s'%tai_or_xiu] = mark_safe(u'<span id = "%s">%s</span>'%(symbol_id,symbol_view))
                link_row_data_table['link_%s'%tai_or_xiu]  = mark_safe(u'<a href = "#%s">%s</a>'%(symbol_id,color_current_sign(is_color,symbol_view)))
                if is_color:
                    link_row_data_table_active['link_%s'%tai_or_xiu] = mark_safe(u'<a href = "#%s">%s</a>'%(symbol_id,color_current_sign(is_color,symbol_view)))
                    TbImport.GLOBAL_BRIEF_ACTIVE_LIST.append(link_row_data_table_active)
                    if 'fighter' in fighter_or_single:####fighter
                        fighter_tai_or_xiu_strim_from_argument = re.findall('fighter_(.*?$)',fighter_or_single)[0]
                        if so_cau_moc_if_fighter_for_find_cau_list_link == TbImport.how_many_current_is_repeat_tai_or_xiu['repeat ' +fighter_tai_or_xiu_strim_from_argument] :
                            TbImport.GLOBAL_EXACTLY_ACTIVE_LIST.append(link_row_data_table_active)
                        for k_dubaotai_or_dubaoxiu,v in TbImport.for_make_fighter_dubao_link.iteritems():
                            if so_cau_moc_if_fighter_for_find_cau_list_link == v.get('repeat ' + fighter_tai_or_xiu_strim_from_argument,0) :#'du bao tai','du bao xiu'    
                                TbImport.GLOBAL_DUBAO_ACTIVE_LIST[k_dubaotai_or_dubaoxiu].append(link_row_data_table_active) 
                        #TbImport.for_make_fighter_dubao_link = {'du bao tai':('repeat tai',so_luong_cau_TAI_trong_nhom_number + 1),\
                                                                                  #'du bao xiu':('repeat xiu',1),}        
                    else:#single
                        TbImport.GLOBAL_EXACTLY_ACTIVE_LIST.append(link_row_data_table_active)
                else:
                    if fighter_or_single =='single':  
                        for k_dubaotai_or_dubaoxiu,v in TbImport.for_make_fighter_dubao_link.iteritems():
                                key_du_bao = repeat_or_xen_ke + ' ' + tai_or_xiu
                                print key_du_bao,v.get(key_du_bao,0),i_repeat
                                if i_repeat == v.get(key_du_bao,0) :
                                    du_bao_row = {'link_tai':'','link_xiu':''}
                                    key = 'link_%s'%tai_or_xiu
                                    du_bao_row.update({key:link_row_data_table[key]})
                                    TbImport.GLOBAL_DUBAO_ACTIVE_LIST[k_dubaotai_or_dubaoxiu].append(du_bao_row)
            else:
                if i_repeat !='tai' and i_repeat !='xiu':
                    is_color = current_group_cau_sign [i_repeat]
                else:
                    is_color = False
            ### END DEFIND IS_COLOR
            
            
            for count_in_loop_qua_mau_thu,MAU_THU in enumerate(END_LIST):
                
                dict_tai_or_xiu_repeat_of_nhieu_mau_thu =  more_info_get_from_loop[dict_thong_ke_repeat_name]#{32:{},64..}
                dict_so_luong_of_1_in_14_lan_repeat =dict_tai_or_xiu_repeat_of_nhieu_mau_thu[MAU_THU] # {1:15,2:8,..}
                try:
                    repeat_n = dict_so_luong_of_1_in_14_lan_repeat[i_repeat]
                except KeyError:
                    repeat_n = 0
                repeat_n_theory = Probability_theory*MAU_THU/100
                repeat_n_theory_html = color_current_sign(is_color,  u'%.1f'%repeat_n_theory)
                redundant_or_lack = (repeat_n -  repeat_n_theory)  
                  
                if fighter_or_single =='single':
                    MAU_THU_html = MAU_THU
                    Probability_theory_html = u'%.3f %%'%(Probability_theory)
                else:
                    Probability_theory_fighter_gap_so_voi_single = 2*float(12.5/pow(2, (so_cau_moc_if_fighter_for_find_cau_list_link-1)))
                    Probability_theory_fighter = Probability_theory*Probability_theory_fighter_gap_so_voi_single/100
                    single_tuong_duong = so_cau_moc_if_fighter_for_find_cau_list_link + i_repeat +1
                    Probability_theory_html = u'%.3f %% =s%s'%(Probability_theory_fighter,single_tuong_duong)
                    MAU_THU_cau_single = 100*repeat_n_theory/Probability_theory_fighter#MAU_THU_Cau_kep*100/Probability_theory_fighter_gap_so_voi_single
                    MAU_THU_html = u'%s-%.0f'%(MAU_THU,MAU_THU_cau_single)
                def create_tr_from_redundant_or_lack(repeat_n,for_exclude=False):
                    redundant_or_lack = (repeat_n -  repeat_n_theory)
                    redundant_or_lack_percent = redundant_or_lack*100/repeat_n_theory   
                    if count_in_loop_qua_mau_thu == 0:
                        middle_description =''
                    else:
                        if for_exclude:
                            redundant_or_lack_in_middle = redundant_or_lack + 1 - redundant_or_lack_in_middle_before
                        else:
                            redundant_or_lack_in_middle = redundant_or_lack  - redundant_or_lack_in_middle_before
                        repeat_n_theory_in_middle = repeat_n_theory - repeat_n_theory_in_middle_before
                        percent_in_middle = redundant_or_lack_in_middle*100/repeat_n_theory_in_middle
                        middle_descriptions = (u'%s/%.1f'%(wanting_html2(percent_in_middle,redundant_or_lack_in_middle),repeat_n_theory_in_middle),wanting_html2(percent_in_middle))
                        middle_description = ''.join(map(lambda x:'<td>%s</td>'%x,middle_descriptions))
                        middle_description = '<table class="up-margin">%s</table>'%middle_description
                    #end for middle
                    tr_tai_or_xiu_tr_s= ( Probability_theory_html,MAU_THU_html,\
                                      create_current_html_depend_last_cau(last_cau_value,
                                                           create_modal_link(repeat_n,i_repeat,MAU_THU,
                                                                             fighter_or_single,
                                                                             tai_or_xiu,
                                                                             repeat_or_xen_ke,
                                                                             so_cau_moc_if_fighter_for_find_cau_list_link),
                                                           tai_or_xiu) ,\
                                      repeat_n_theory_html,
                                      wanting_html2(redundant_or_lack_percent,redundant_or_lack),
                                      wanting_html2(redundant_or_lack_percent),
                                      middle_description)
                    tr_tai_or_xiu = ''.join(map(lambda x:'<td>%s</td>'%x,tr_tai_or_xiu_tr_s))
                    return tr_tai_or_xiu
                
                
                tr_tai_or_xiu =  create_tr_from_redundant_or_lack(repeat_n)   
                if is_color and repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
                    repeat_n_exclude_now = repeat_n  -1
                    exclude_now_tr_tai_or_xiu = create_tr_from_redundant_or_lack(repeat_n_exclude_now,for_exclude=True)
                    exclude_now_table_body_html_for_tai_or_xiu.append(exclude_now_tr_tai_or_xiu)
                redundant_or_lack_in_middle_before = redundant_or_lack
                repeat_n_theory_in_middle_before = repeat_n_theory
                # cong nhieu row cua mau thu lai
                table_body_html_for_tai_or_xiu += '<tr>' + tr_tai_or_xiu + '</tr>'
                    
            
        # hoan thien tr thanh table choi moi tai hoac xiu voi theader va tbody sau cung <table>, ngoai vong lap mau thu
            table_body_html_for_tai_or_xiu= u'<table class="last-td-not-table table-bordered">%s<tbody>%s</tbody></table>'%(table_header,table_body_html_for_tai_or_xiu)
            if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
                if is_color:
                    exclude_now_table_body_html_for_tai_or_xiu = u''.join('<tr>%s</tr>'%td for td in exclude_now_table_body_html_for_tai_or_xiu )
                    exclude_now_table_body_html_for_tai_or_xiu = u'<h4 style="color:orange">Nếu không tính cầu hiện tại</h4><table class="last-td-not-table table-bordered">%s<tbody>%s</tbody></table>'%(table_header,exclude_now_table_body_html_for_tai_or_xiu)
                    table_body_html_for_tai_or_xiu += '</br>' +  exclude_now_table_body_html_for_tai_or_xiu
            else:
                new_table_html = table_body_html_for_tai_or_xiu
            if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
                row_dict_data_for_one_i_repeat['%s_repeat_description'%tai_or_xiu] = mark_safe(table_body_html_for_tai_or_xiu)
                
            else:
                row_td_contain_table_data_dict[i_repeat] = mark_safe(new_table_html)
        if repeatxenke_table_or_tai_xiu_tttxx_table == "create repeat or xenke table":
            table_big_data_lists.append(row_dict_data_for_one_i_repeat)
            TbImport.GLOBAL_BRIEF_ID_LINK_LIST.append(link_row_data_table)
    if repeatxenke_table_or_tai_xiu_tttxx_table != "create repeat or xenke table":
        table_big_data_lists = [row_Probability_theory_dict,row_td_contain_table_data_dict]
    return table_big_data_lists

if __name__ == '__main__':
    repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,\
    more_info_get_from_loop = soicau_2(is_in=True,SAVE_CHART_OPTION = True,TbImport=TbImport)
    xenke_data_table = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop,END_LIST=more_info_get_from_loop['New_END_LIST'],
                                                         repeat_or_xen_ke = 'xenke',TbImport = TbImport)
    print TbImport.GLOBAL_DUBAO_ACTIVE_LIST