# -*- coding: utf-8 -*-
#from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from models import Ulnew,ForumTable, PostLog, LeechSite, thongbao, postdict,autoimportdict
import forms
from drivingtest.forms import  ForumChoiceForm, UlnewForm, UlnewTable, TaiXiuXiuTaiTable, Tong3DiceTable, TaiXiuForm, TaiXiuTable,\
    ImportForm, Thoi_gian_cho_su_lap_lai_Table, AutoImportForm, SoiCauForm,\
    RepeatTable, Import100PhienForm, Tai_Xiu_Thong_Ke_Table2, TtxxTable2,\
    LinkTable, GLOBAL_BRIEF_ID_LINK_LIST, MySelectChartOptionForm,\
    ChartOptionSelectTrueOrFalseForm

from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from __main__ import sys
from fetch_website import danhsachforum, PostObject, leech_bai,\
    get_link_from_db, import_ul_txt_to_myul
from exceptions import Exception
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from drivingtest.models import TaiXiu, Notification_global_from_model_module,TbImport,\
    MySelectChartOption
from soicau import create_giong_nhau_khac_nhau_lists,\
    test_xac_suat_tong_3_dice_database, phien_100_to_html,\
    create_how_many_phien_for_same_cau, autoimport, AutoImportObject,\
    string_soi_cau, soicau_2,\
    chon_tren_hoac_duoi_cau_kep, create_repeat_table_data2, check_cau,\
    autoimport1
from django.db.models.aggregates import Min, Max, Count
import re
from django.utils import timezone
from django.db.models import CharField,DateTimeField,DateField, AutoField
from datetime import datetime
from django.utils.safestring import mark_safe
from django.utils.datastructures import MultiValueDictKeyError
VERBOSE_CLASSNAME ={'TaiXiu':u'Nguyên Nhân'} 
from django.db.models import Q

################CHUNG######################




#####OMC###############





#############################################################################

def create_table(tai_xiu_lists,show_description = 'ko xen ke type',is_created_xenKe_list = True):
    #aggregate_tx2  = tai_xiu_lists.aggregate(Max('phien_so'), Min('phien_so'),Count('phien_so'))
    #aggregate_tx2['count_tx'] = aggregate_tx2['phien_so__max']- aggregate_tx2['phien_so__min'] + 1
    rt= create_giong_nhau_khac_nhau_lists(tai_xiu_lists,show_description = 'ko xen ke type',is_created_xenKe_list = is_created_xenKe_list)
    xen_ke_or_giong_nhau_lists = rt[0]
    repeat_dict_lists = rt[3]
    txxt_dict_lists =  rt[4]
    string_tai_xiu_soi_cau = rt[5]
    repeat_table_2 = RepeatTable(repeat_dict_lists)
    taiXiuXiuTai_Table_2 = TaiXiuXiuTaiTable(txxt_dict_lists)
    return repeat_table_2,taiXiuXiuTai_Table_2,string_tai_xiu_soi_cau,xen_ke_or_giong_nhau_lists,repeat_dict_lists,txxt_dict_lists

def create_tong_hop_list_of_dict(repeat_dict_lists,repeat_dict_lists_tong_hop,count,len_END_CAN_LAY,SOMAUTHU):
            for count_row_cau_lap,row_dict in enumerate(repeat_dict_lists):
                if count==0:
                    row_dict_1_lan_lap_cua_tong_hop = {}
                else:
                    row_dict_1_lan_lap_cua_tong_hop = repeat_dict_lists_tong_hop[count_row_cau_lap]
                    
                for column_name,description in row_dict.iteritems():
                    
                    if column_name=='so_lan_lap' or column_name=='lythuyet_repeat_xac_suat_i':
                        row_dict_1_lan_lap_cua_tong_hop[column_name] = description
                    elif column_name=='mau_thu':
                        pass
                    elif count==0:
                        row_dict_1_lan_lap_cua_tong_hop[column_name] = mark_safe('<li>%s %s</li>'%(SOMAUTHU,description))
                    elif count ==len_END_CAN_LAY - 1:
                        row_dict_1_lan_lap_cua_tong_hop[column_name] = mark_safe(u'<ul>%s</ul>'%(mark_safe('<li>%s %s</li>'%(SOMAUTHU,description)) +row_dict_1_lan_lap_cua_tong_hop[column_name]))
                    else:
                        row_dict_1_lan_lap_cua_tong_hop[column_name] = mark_safe('<li>%s %s</li>'%(SOMAUTHU,description)) +row_dict_1_lan_lap_cua_tong_hop[column_name]
                if count ==0:
                    repeat_dict_lists_tong_hop.append(row_dict_1_lan_lap_cua_tong_hop)
from django.utils.timezone import localtime
def taixiuview(request):
    return render('sss')
def tai_xiu_3(request,for_only_return_dict = False):
    is_show_line = request.GET.get('is_show_line',True)
    if is_show_line =='true':
        is_show_line = True
    else:
        is_show_line = False
    taixiuform = TaiXiuForm()
    taixiutable = TaiXiuTable(TaiXiu.objects.all().order_by('-phien_so'))
    RequestConfig(request, paginate={"per_page": 15}).configure(taixiutable)
    class TbImport(object):
        thongbao = 'chua co thong bao j'
        Da_import_xong_global_from_model_module = False
        GLOBAL_BRIEF_ID_LINK_LIST = []
        GLOBAL_BRIEF_ACTIVE_LIST = []
        GLOBAL_EXACTLY_ACTIVE_LIST = []
        GLOBAL_DUBAO_ACTIVE_LIST = {'du bao tai':[],'du bao xiu': []}
        for_make_fighter_dubao_link = {'du bao tai':('',''),'du bao xiu':('','')}
    TbImport.GLOBAL_BRIEF_ID_LINK_LIST = []
    TbImport.GLOBAL_BRIEF_ACTIVE_LIST = []
    TbImport.GLOBAL_EXACTLY_ACTIVE_LIST = []
    TbImport.GLOBAL_DUBAO_ACTIVE_LIST =  {'du bao tai':[],'du bao xiu': []}
    #TbImport.for_fighter_extactly_active_list_current = ('','')
    last_cau = TaiXiu.objects.latest('phien_so')
    try:
        end_phien = int(request.GET['end'])
        filter_tx = TaiXiu.objects.filter(phien_so__gt=end_phien)
        end_phien_to_select_phien = len(filter_tx)
        select_cau = TaiXiu.objects.get(phien_so=end_phien)
    except  :#MultiValueDictKeyError
        end_phien_to_select_phien = 0
        select_cau = last_cau
    rt = string_soi_cau(select_cau.phien_so,100)
    string_soi_cau_html = rt[0] 
    soicauForm = SoiCauForm(initial = {'end_phien':select_cau.phien_so},soi_cau_html=string_soi_cau_html)
    
    END_LIST = [32,64,100,128,256,512,1024,2048,3072,4096,8192,16384,0]
    repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,\
    more_info_get_from_loop = soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),\
                                       END_LIST=END_LIST,end_phien_to_select_phien = end_phien_to_select_phien,
                                       is_show_line = is_show_line,is_in = False,
                                       TbImport = TbImport)
    data_taixiuthongke_table  = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop,
                                            END_LIST=more_info_get_from_loop['New_END_LIST'],
                                            repeatxenke_table_or_tai_xiu_tttxx_table = "create taixiu table",
                                            TbImport = TbImport)
    taixiuthongke_table = Tai_Xiu_Thong_Ke_Table2(data_taixiuthongke_table)
    
    data_ttxx_table  = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop,
                                            END_LIST=more_info_get_from_loop['New_END_LIST'],
                                            repeatxenke_table_or_tai_xiu_tttxx_table = "create ttxx table",
                                            TbImport = TbImport)
    ttxx_table = TtxxTable2(data_ttxx_table)
    
    
    
    data_table  = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop,\
                                            END_LIST=more_info_get_from_loop['New_END_LIST'],\
                                            repeat_or_xen_ke = 'repeat',TbImport = TbImport)
    repeat_table = RepeatTable(data_table)
    repeat_table.title = 'repeat_table'
    repeat_table.html_id = 'repeat_table'
    xenke_data_table = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop,END_LIST=more_info_get_from_loop['New_END_LIST'],
                                                         repeat_or_xen_ke = 'xenke',TbImport = TbImport)
    xen_ke_table = RepeatTable(xenke_data_table)
    xen_ke_table.title = 'xen_ke_table'
    xen_ke_table.html_id = 'xen_ke_table'
    above_3_tai_xius = []
    for so_cau_moc in range(1,11):
        tupple_tai_xiu_above_table = []
        for tai_or_xiu in ['tai','xiu']:
            repeat_TAI_or_XIU_lists = eval('repeat_%s_lists'%tai_or_xiu.upper())
            list_2_vs_above = chon_tren_hoac_duoi_cau_kep(repeat_TAI_or_XIU_lists,so_cau_moc=so_cau_moc)
            if list_2_vs_above:
                for xen_ke_or_repeat in ['repeat','xenke']:
                    repeat_2xiurepeat_lists,repeat_above2_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more_info_get_from_loop_above \
                    = soicau_2(qrs = list_2_vs_above,END_LIST =END_LIST,TbImport = TbImport)
                    data_table  = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop_above,
                                                            END_LIST=more_info_get_from_loop_above['New_END_LIST'],
                                                            fighter_or_single = "fighter_%s"%tai_or_xiu,
                                                            repeat_or_xen_ke = xen_ke_or_repeat,
                                                            so_cau_moc_if_fighter_for_find_cau_list_link = so_cau_moc,
                                                            TbImport = TbImport)
                    repeat_table_list_2_vs_above_cua_tai = RepeatTable(data_table)
                    title = mark_safe( u'<h4 class="above-fighter-title">Above <span style="color:green">%s %s</span> cua <span style="color:yellow">%s</span> </h4>'%(so_cau_moc,xen_ke_or_repeat,'TAI' if  tai_or_xiu== 'tai' else 'XIU'))
                    repeat_table_list_2_vs_above_cua_tai.title = title
                    tupple_tai_xiu_above_table.append(repeat_table_list_2_vs_above_cua_tai)
                    if so_cau_moc==2 and tai_or_xiu=='tai':
                        repeat_equal_tams = repeat_2xiurepeat_lists
                print 'in above ',so_cau_moc
        above_3_tai_xius.append(tupple_tai_xiu_above_table)
        
    list_2_vs_above = chon_tren_hoac_duoi_cau_kep(repeat_equal_tams,so_cau_moc=2)
    repeat_2xiurepeat_lists,repeat_above2_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more_info_get_from_loop_above \
                = soicau_2(qrs = list_2_vs_above,END_LIST =END_LIST,TbImport = TbImport)
    data_table  = create_repeat_table_data2(more_info_get_from_loop=more_info_get_from_loop_above,
                                                            END_LIST=more_info_get_from_loop_above['New_END_LIST'],
                                                            fighter_or_single = "fighter_%s"%'tai',
                                                            repeat_or_xen_ke = 'repeat',
                                                            so_cau_moc_if_fighter_for_find_cau_list_link = 2,
                                                            TbImport = TbImport)
    
    table_2qualvsmore2 = RepeatTable(data_table)
    linkTable = LinkTable(TbImport.GLOBAL_BRIEF_ID_LINK_LIST)
    linkTable_active = LinkTable(TbImport.GLOBAL_BRIEF_ACTIVE_LIST)
    exactly_act_tive_link_Table = LinkTable(TbImport.GLOBAL_EXACTLY_ACTIVE_LIST)
    dubaotai_Table = LinkTable( TbImport.GLOBAL_DUBAO_ACTIVE_LIST['du bao tai'])
    dubaoxiu_Table = LinkTable( TbImport.GLOBAL_DUBAO_ACTIVE_LIST['du bao xiu'])
    soi_cau_form_notification = form_notification_soi_cau_create(last_cau,rt)
    
    rt = string_soi_cau(last_cau.phien_so,10) 
    brief_soi_cau = u'%s <span id = "last-phien-sample">%s</span>,%s</br>%s'%(rt[0],last_cau.phien_so,localtime(last_cau.ngay_gio_tao).strftime("%d-%m-%Y %H:%M:%S"),rt[3])
    
    autoImportForm = AutoImportForm()
    
    series =  more_info_get_from_loop['series_DICT']
    categories =  more_info_get_from_loop['categories_dict']
    
    mySelectChartOptionForm = MySelectChartOptionForm(instance = MySelectChartOption.objects.get(Name = 'my select'))
    
    
    render_dict = {#'last_phien':last_phien_html,
                   #'soi_phien':end_phien_html,
                   #'string_soi_cau_html':string_soi_cau_html,\
                   'table_2qualvsmore2':table_2qualvsmore2,
                   'taixiuform':taixiuform,
                   'taixiutable':taixiutable,
                   'brief_soi_cau':brief_soi_cau,
                   'series':series,
                   'categories':categories,
                   'dubaoxiu_Table':dubaoxiu_Table,
                   "dubaotai_Table":dubaotai_Table,
                   'exactly_act_tive_link_Table':exactly_act_tive_link_Table,
                   'linkTable':linkTable,
                   'linkTable_active':linkTable_active,
                   'autoImportForm':autoImportForm,
                   'soicauForm':soicauForm,
                   'soi_cau_form_notification':mark_safe(soi_cau_form_notification),
                   'taixiuthongke_table':taixiuthongke_table,
                   'ttxx_table':ttxx_table,
                   'repeat_table':repeat_table,
                   'xen_ke_table':xen_ke_table,
                   #'repeat_table_list_2_vs_above_cua_tai':repeat_table_list_2_vs_above_cua_tai,
                   #'repeat_table_list_2_vs_above_cua_xiu':repeat_table_list_2_vs_above_cua_xiu
                   'above_3_tai_xius':above_3_tai_xius,
                   'mySelectChartOptionForm':mySelectChartOptionForm,
                   }
    if for_only_return_dict:
        return render_dict
    return render(request, 'drivingtest/taixiu_2.html', render_dict)
so_luong_truy_suat = 0
def import100phien(request):
    global so_luong_truy_suat
    import100PhienForm = Import100PhienForm()
    so_luong_truy_suat +=1
    print 'import 100 phien',so_luong_truy_suat
    return render(request, 'drivingtest/import100PhienForm.html', {'import100PhienForm':import100PhienForm})
def selectchart(request):
    mySelectChartOptionForm = MySelectChartOptionForm(instance = MySelectChartOption.objects.get(Name = 'my select'))
    return render(request, 'drivingtest/selectchart.html', {'mySelectChartOptionForm':mySelectChartOptionForm})
def chartoption(request):
    #mySelectChartOptionForm = MySelectChartOptionForm(instance = MySelectChartOption.objects.get(Name = 'my select'))
    form = ChartOptionSelectTrueOrFalseForm()
    return render(request, 'drivingtest/chartoption.html', {'form':form})

import json as simplejson
def autocomplete(request):
    results=[]
    for doitac in [1,2,3,4,5,6,7,8,9,10,15,20,25,30,40,50,60,70,80,90,100,200,300,400]:
            doitac_dict = {}
            doitac_dict['label'] = doitac
            doitac_dict['desc'] = ''
            doitac_dict['id'] = doitac
            results.append(doitac_dict)
    to_json = {
                "key_for_list_of_item_dict": results,
            }
    return HttpResponse(simplejson.dumps(to_json), content_type='application/json')
class FilterToGenerateQ():
    No_AUTO_FILTER_FIELDS=[]
    def __init__(self,request,FormClass,ModelClass,form_cleaned_data):
        self.form_cleaned_data = form_cleaned_data
        self.EXCLUDE_FIELDS = getattr(FormClass.Meta,'exclude', [])
        #self.No_AUTO_FILTER_FIELDS = No_AUTO_FILTER_FIELDS
        self.ModelClass = ModelClass
        self.request = request
    def generateQgroup(self):
        qgroup=Q()
        for f in self.ModelClass._meta.fields :
            try:
                if not self.request.GET[f.name] or self.form_cleaned_data[f.name]==None  or  (f.name  in self.EXCLUDE_FIELDS) or  (f.name  in self.No_AUTO_FILTER_FIELDS)  :
                    continue
            except :#MultiValueDictKeyError
                continue
            functionname = 'generate_qobject_for_exit_model_field_'+f.name
            no_auto_function = getattr(self, functionname,None)
            if no_auto_function:
                g_no_auto = no_auto_function(f.name)
                qgroup &=g_no_auto
            elif isinstance(f,CharField):
                if self.form_cleaned_data[f.name]==u'*':
                    qgroup &= ~Q(**{'%s__isnull'%f.name:True}) & ~Q(**{'%s__exact'%f.name:''})
                elif self.form_cleaned_data[f.name]==u'!':
                    qgroup &= Q(**{'%s__isnull'%f.name:True}) | Q(**{'%s__exact'%f.name:''})
                else:
                    qgroup &=Q(**{'%s__icontains'%f.name:self.form_cleaned_data[f.name]})
            elif isinstance(f,DateTimeField) or  isinstance(f,DateField) or  isinstance(f,AutoField):
                pass
            else:
                qgroup &=Q(**{'%s'%f.name: self.form_cleaned_data[f.name]})
        #MANYTOMANYFIELDS
        for f in self.ModelClass._meta.many_to_many :
            try:
                if not self.request.GET[f.name]:
                    continue
            except :#MultiValueDictKeyError
                continue
            if (f.name not in self.EXCLUDE_FIELDS) and (f.name not in self.No_AUTO_FILTER_FIELDS):
                qgroup &=Q(**{'%s__in'%f.name:self.form_cleaned_data[f.name]})
        
        q_out_field = getattr(self,'generate_qobject_for_NOT_exit_model_fields',None)
        if q_out_field:
            q_outer_field = self.generate_qobject_for_NOT_exit_model_fields()
            qgroup &= q_outer_field       
        return qgroup
def loc_query_for_table_notification(form_for_loc,request):
    count=0
    loc_query=''
    for k,f in form_for_loc.fields.items():
        try:
            v = request.GET[k]
        except:
            continue
        if v:
            try:
                label = f.label +''
            except TypeError:
                label = k
            count +=1
            if count==1:
                loc_query = label + '=' + v
            else:
                loc_query = loc_query + '&'+label + '=' + v
    return  loc_query  
def form_notification_soi_cau_create(last_cau,rt):
                    check_cau_string = check_cau()
                    select_cau,begin_cau = rt[1],rt[2]
                    last_phien_html =u'<span style="color:blue" id ="last-phien">%s</span>,%s'%(last_cau.phien_so,localtime(last_cau.ngay_gio_tao).strftime("%d-%m-%Y %H:%M:%S"))
                    end_phien_muon_soi_html =u'<span class="end-phien-muon-soi">%s</span>,%s'%(select_cau.phien_so,localtime(select_cau.ngay_gio_tao).strftime("%d-%m-%Y %H:%M:%S"))
                    khoang_cach_2_phien = u'%s'%(last_cau.phien_so - select_cau.phien_so)
                    khoang_cach_id = (last_cau.id - select_cau.id)
                    form_notification = u'last_phien_in_database:%s</br>end_phien_muon_soi:%s</span></br>Khoảng cách 2 phiên: %s</br>Khoảng cách 2 id: %s'\
                    %(last_phien_html,end_phien_muon_soi_html,khoang_cach_2_phien,khoang_cach_id)
                    khoang_cach_soi_cau = u'</br>khoang cach 2 phien can soi: %s, </br>khoang cach 2 id can soi %s'%(select_cau.phien_so -begin_cau.phien_so,select_cau.id -begin_cau.id )
                    return check_cau_string + '<br>' + rt[3]+ '</br>' +  form_notification   + khoang_cach_soi_cau
def modelmanager(request,modelmanager_name,entry_id):
    #tham so loc nam trong GET, ngoai tham so loc ra thi con tham so which_table_or _form tham so modal hay normal form, neu co nhung tham so nhu tramid
    #hay query_main_search_by_button thi chac chan khong co tham so loc
    # khi loc ma method = Request thi parameter GET  gui di chi toan la fiedl khong co add extra parameter cua table
    # chi co add them extra parameter cua table khi post Edit
    #khi co tramid thi khong co loc
    #khi co tram id thi khong co query_main_search_by_button
    #form_name = modelmanager
    status_code = 200
    url = '/omckv2/modelmanager/'+ modelmanager_name +'/'+entry_id+'/'
    form_table_template =request.GET.get('form-table-template')
    is_form = True if  (request.GET.get('is_form',None) =='true')else False
    is_table = True if  (request.GET.get('is_table',None) =='true')else False
    is_download_table = True if 'downloadtable' in request.GET else False
    if is_download_table:
        is_form = False
    is_another_template = False
    dict_render ={}
    form = None
    table2 = None
    need_valid=False
    need_save_form  =False
    data=None
    initial=None
    instance=None
    form_notification = None
    #table_notification = u'<h2 class="table_notification"> Danh sách được hiển thị ở table bên dưới  </h2>'
    loc = True if 'loc' in request.GET else False
    loc_pass_agrument=False
    force_allow_edit = False
    #khong_show_2_nut_cancel_va_loc = False
    table_name = request.GET.get('table_name') if request.method =='POST' else None
    khong_show_2_nut_cancel_va_loc = request.GET.get('khong_show_2_nut_cancel_va_loc',None)
    if khong_show_2_nut_cancel_va_loc ==None:
        khong_show_2_nut_cancel_va_loc = True if table_name else False
    else:
        khong_show_2_nut_cancel_va_loc = True
    next_continue_handle_form = True
    #FORM HANDLE
    #if which_form_or_table!="table only" or loc or (is_download_table and loc): #get Form Class
    if is_form : # or loc or (is_download_table and loc)
        form_name= modelmanager_name
        print '@@@@@@@@@@@@modelmanager_name',modelmanager_name
        FormClass = eval('forms.' + form_name)#repeat same if loc
        ModelOfForm_Class_name = re.sub('Form$','',form_name,1)
        if form_name =='NhanTinUngCuuForm':# only form not model form
            form = FormClass(initial = {'noi_dung_tin_nhan':'abc'})
            form.modal_title_style = 'background-color:#337ab7'
            form.modal_prefix_title  = 'Nội Dung Nhắn Tin'
            form_notification= u'<h2 class="form-notification text-primary">Nhấn nút copy, sẽ copy nội dung tn vào clipboard</h2>'
            dict_render = {'form':form,'form_notification':form_notification}
        
        elif form_name =="SoiCauForm":
            form = FormClass(request.POST)
            is_form_valid = form.is_valid()
            if not is_form_valid :
                form_notification = u'<h2 class="form-notification text-danger">Nhập Form sai, vui lòng check lại </h2>'
                status_code = 400
            else:
                rt= string_soi_cau(form.cleaned_data['end_phien'],form.cleaned_data['so_cau_can_soi'])
                soi_cau_html = rt[0]
                last_cau = TaiXiu.objects.latest('phien_so')
                form_notification = form_notification_soi_cau_create(last_cau,rt)
                form = FormClass(request.POST,soi_cau_html = soi_cau_html)
            dict_render = {'form':form,'form_notification':form_notification}  
        elif form_name =="Import100PhienForm":
            form = FormClass(request.POST)
            is_form_valid = form.is_valid()
            if not is_form_valid :
                form_notification = u'<h2 class="form-notification text-danger">Nhập Form sai, vui lòng check lại </h2>'
                print 'nhap form sai vui long check lai'
                status_code = 400
            else:
                tb = autoimport1(last_phien_in_100_user_import = form.cleaned_data['current_phien_plus_one'],ALOWED_change= True,save_or_test = True)
                form = FormClass(request.POST)
                form_notification = u'<h2 class="form-notification text-primary">%s,OK auto import with manual current phien ,%s</br>%s</h2>'%(datetime.now(),tb,TaiXiu.objects.latest('phien_so').phien_so)
            dict_render = {'form':form,'form_notification':form_notification}          
        elif form_name =='AutoImportForm':
            form = FormClass()
            which_start_or_stop_btn = request.GET['which-start-or-stop-btn']
            if which_start_or_stop_btn=="Start":
                try:
                    luong = autoimportdict["luong autoimport"]
                    if luong.is_alive():
                        can_khoi_tao = False
                    else:
                        can_khoi_tao = True
                except:
                    can_khoi_tao = True
                
                if not can_khoi_tao :
                    dict_render = {'form':form,'form_notification':u'<span class="form-notification text-primary">STARTED!,luong da chay roi!! ,%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))}
                else:
                    autoimportdict["luong autoimport"] = AutoImportObject()
                    autoimportdict["luong autoimport"].start()
                    if 1:#TbImport.Da_import_xong_global_from_model_module:
                        dict_render = {}
                        dict_render.update ({'form':form,'form_notification':u'<span class="form-notification text-primary">START ,%s,%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"),TbImport.thongbao)})
            elif which_start_or_stop_btn=="Stop" :
                try:
                    autoimportdict["luong autoimport"].stop  = True
                    dict_render = {'form':form,'form_notification':u'<span class="form-notification text-primary">Stop ,%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))}
                except Exception as e:
                    dict_render = {'form':form,'form_notification':u'<span class="form-notification text-primary">Chua co luon sao bam Stop!!!%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))}
            elif which_start_or_stop_btn=="thongbao":   
                is_another_template = True
                dict_render  = tai_xiu_3(request,for_only_return_dict = True)
                #dict_render = {}
                #dict_render.update ({'form':form,'form_notification':u'<span class="form-notification text-primary">Thong bao::: ,%s,%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"),TbImport.thongbao)})
                dict_render.update ({'autoImportForm':form,'form_notification':u'<span class="form-notification text-primary">Thong bao::: ,%s,%s</span>'%(datetime.now().strftime("%d-%m-%Y %H:%M:%S"),TbImport.thongbao)})
            elif which_start_or_stop_btn=="poll":
                try:
                    just_poll = request.GET['just_poll']
                except:
                    just_poll = 'nhan nut poll'
                if just_poll=="true":
                    last_phien = TaiXiu.objects.latest('phien_so').phien_so
                    return render(request, 'drivingtest/poll.html',{'last_phien':last_phien})
                elif just_poll=="false":
                    tudong_hay_nhan_nut_poll = 'tu dong'
                else:
                    tudong_hay_nhan_nut_poll = 'nhan nut poll'
                is_another_template = True
                dict_render  = tai_xiu_3(request,for_only_return_dict = True)
                dict_render.update ({'autoImportForm':form,'form_notification':u'<span class="form-notification text-primary">%s:,%s,%s</span>'%(tudong_hay_nhan_nut_poll,datetime.now(),TbImport.thongbao)})   
        elif form_name =='ChartOptionSelectTrueOrFalseForm':
            print 'okkkkkkkkkkkkk...'
            print request.body
            form = ChartOptionSelectTrueOrFalseForm()
            
            mySelectChartOption =  MySelectChartOption.objects.get(Name = 'my select')
            for option in mySelectChartOption.myselect.all():
                is_select = request.POST.get(option.Name,False)
                if is_select:
                    is_select = True
                option.is_select_or_not = is_select
                option.save()
                print '***is_select',option.Name,is_select
            
            dict_render =   {'form':form,'form_notification':'ban ok'}   
        else:
            
            #print 'request.POST',request.POST
            if request.method=='POST':
                need_valid =True
                need_save_form=True
                data = request.POST
            elif request.method=='GET':
                if loc:
                    #print 'request.GET',request.GET
                    need_valid =True
                    data = request.GET
                    loc_pass_agrument = True #tham so nay de loai bo loi required khi valid form
                else:
                    if entry_id=='new':
                        form_notification = u'<h2 class="form-notification text-primary">Form trống để tạo instance <span class="name-class-notification">%s</span> mới </h2>'%(VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name))
                    else:
                        form_notification = u'<h2 class="form-notification text-warning"> Đang hiển thị form của Đối tượng <span class="name-class-notification">%s</span> có ID là %s</h2>'%(VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name),entry_id)
                        if 'force_allow_edit' in request.GET:
                            force_allow_edit=True # chuc nang cua is_allow_edit la de display nut edit hay khong
            ModelOfForm_Class = FormClass.Meta.model # repeat same if loc
            
            if entry_id !="new":# check 1 so truong hop tra ngay ve ket qua status_code=403(forbid)
                try:
                    int(entry_id)
                    instance = ModelOfForm_Class.objects.get(id = entry_id)
                except ValueError:#not interger, tuc la 1 chuoi
                    #if ModelOfForm_Class_name =='Tram':
                    form_notification = u'<h2 class="form-notification text-danger">khogn tim thay</h2>'
                    dict_render = {'form':None,'form_notification':form_notification}
                    status_code = 200
                    next_continue_handle_form = False
                if request.method=="POST":# hoac la need_save_form
                    print instance.id
                    if 'is_delete' in request.POST and instance.nguoi_tao != request.user :
                        dict_render.update({'info_for_alert_box':u'Bạn không có quyền xóa instance MLL or Comment của người khác'})
                        status_code = 403
                    elif  'is_delete' in request.POST:#instance.nguoi_tao == request.user
                        #ModelOfForm_Class = FormClass.Meta.model # repeat same if loc
                        instance = ModelOfForm_Class.objects.get(id = entry_id)
                        delta = (timezone.now() - instance.ngay_gio_tao).seconds/60
                        set_allowed_delta_time = 12
                        if delta <set_allowed_delta_time:
                            instance.delete()
                            form_notification = u'<h2 class="form-notification text-danger">Đã xóa comment này, delta %s</h2>'%str(delta)
                            dict_render = {'form':None,'form_notification':form_notification}
                            status_code = 200
                            next_continue_handle_form = False
                        else:
                            dict_render.update({'info_for_alert_box':\
                                                u'Hết thời gian để xóa instance nay vi no đã tạo được {0} giây, trong khi bạn chỉ được xóa trong vòng {1}\
                                                '.format(str(delta),str(set_allowed_delta_time))})
                            status_code = 403
                            #form_notification = u'<h2 class="form-notification text-warning">Het thoi gian xoa%s</h2>'%str(delta.seconds/60)
                    elif form_name=="CommentForm" and instance.nguoi_tao != request.user :
                        dict_render.update({'info_for_alert_box':u'Bạn không có quyền thay đổi comment của người khác'})
                        status_code = 403
            if next_continue_handle_form and status_code ==200:
                form = FormClass(data=data,instance = instance,initial=initial,loc =loc_pass_agrument,form_table_template=form_table_template,force_allow_edit=force_allow_edit,request = request,\
                                 khong_show_2_nut_cancel_va_loc = khong_show_2_nut_cancel_va_loc)
                if need_valid:
                    is_form_valid = form.is_valid()
                    if not is_form_valid :
                        form_notification = u'<h2 class="form-notification text-danger">Nhập Form sai, vui lòng check lại </h2>'
                        status_code = 400
                if need_save_form and status_code ==200:
                    instance = form.save(commit=True)
                    id_string =  str(instance.id)
                    if entry_id =="new":
                        form_notification = u'<h2 class="form-notification text-success">Bạn vừa tạo thành công 1 Đối tượng <span class="name-class-notification">%s</span> có ID là %s,bạn có thế tiếp tục edit nó</h2>'%(VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name),id_string)
                    else:
                        form_notification = u'<h2 class="form-notification text-success">Bạn vừa Edit thành công 1 Đối tượng <span class="name-class-notification">%s</span>  có ID là %s,bạn có thế tiếp tục edit nó</h2>'%(VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name),id_string)
                    #reload form with newinstance
                    form = FormClass(instance = instance,request=request,khong_show_2_nut_cancel_va_loc=khong_show_2_nut_cancel_va_loc)###############3
                #if not is_download_table:
                if  status_code !=403:
                    #form.update_action_and_button()        
                    dict_render = {'form':form,'form_notification':form_notification}
    #TABLE handle
    if is_download_table or(is_table  and status_code == 200):
        per_page = 15
        if table_name:# and request.method=='POST'
            TableClass = eval('forms.' + table_name)
            ModelofTable_Class = TableClass.Meta.model
            ModelofTable_Class_name = re.sub('Table','',request.GET['table_name'],1)
        else:
            if modelmanager_name =='FindCauListForm':
                no_model = True
            else:
                no_model = False
            if modelmanager_name =='BCNOSSForm':
                is_groups = []
                groups_fields=['group_ngay','is_group_tinh','is_group_BSC_or_RNC','is_group_BTS_Type','is_group_BTS_thiet_bi','is_group_object']
                for x in groups_fields:
                    is_group_1_item = request.GET.get(x,None)
                    if is_group_1_item:
                        kqs = re.subn(r'^is_group_','',x)
                        if kqs[1]:
                            is_groups.append(kqs[0])
                        else:
                            is_groups.append(is_group_1_item)
                if is_groups:
                    table_name = 'ThongKeNgayThangTable'
                    TableClass = eval('forms.' + table_name)
                else:
                    table_name = re.sub('Form$','Table',modelmanager_name)
                    TableClass = eval('forms.' + table_name)
            else:
                table_name = re.sub('Form$','Table',modelmanager_name)
                TableClass = eval('forms.' + table_name)
            # find modelClass and name
            if not no_model:
                if not is_form:#table only
                    ModelofTable_Class_name = re.sub('Form$','',modelmanager_name,1)
                    ModelofTable_Class = TableClass.Meta.model
                else:
                    ModelofTable_Class_name = ModelOfForm_Class_name
                    ModelofTable_Class = ModelOfForm_Class
                
        #print 'table_nametable_nametable_nametable_name',table_name
        if loc:
            
            if loc_pass_agrument:#truong hop nhan nut loc
                FormClass_for_loc =  FormClass
            else:
                FormClass_for_loc_name =  re.sub('Table$','Form',table_name)
                FormClass_for_loc= eval('forms.' + FormClass_for_loc_name)
            
            form_for_loc = FormClass_for_loc(data=request.GET,loc=True)
            if form_for_loc.is_valid():#alway valid but you must valid to get form.cleaned_data:
                print '######form cua get loc valid'
            else:
                print 'form.errors',form_for_loc.errors.as_text()
            FiterClass= FilterToGenerateQ
            #print '@@@@@form.cleaned_data',form_for_loc.cleaned_data
            qgroup_instance= FiterClass(request,FormClass_for_loc,ModelofTable_Class,form_for_loc.cleaned_data)
            qgroup = qgroup_instance.generateQgroup()
            
            #if (table_name=='ThongKeNgayThangTable') :
            if modelmanager_name == 'BCNOSSForm':
                is_include_code_8 = form_for_loc.cleaned_data['is_include_code_4_7_8']
                if is_include_code_8:
                    qgroup = qgroup
                else:#mac dinh la exclude 478
                    qgroup = qgroup & (~Q(code_loi=8)&~Q(code_loi=7)&~Q(code_loi=4))
                querysets = ModelofTable_Class.objects.filter(qgroup).distinct()
            else:
                querysets = ModelofTable_Class.objects.filter(qgroup).distinct().order_by('-id')
            if loc_pass_agrument:#loc bang nut loc co tra ve form va table
                form_notification =u'<h2 class="form-notification text-info">  Số kết quả lọc là <span class="soluong-notif">%s</span> trong database <span class="name-class-notification">%s</span> <h2>'%(len(querysets),VERBOSE_CLASSNAME[ModelofTable_Class_name])
                dict_render.update({'form_notification':form_notification})
            loc_query = loc_query_for_table_notification(form_for_loc,request)
            table_notification = u'<h2 class="table_notification"> Số kết quả lọc là <span class="soluong-notif">%s</span> query tìm <span class="query-tim">"%s"</span> trong database <span class="name-class-notification">%s</span>  được hiển thị ở table bên dưới</h2>'%(len(querysets),loc_query,VERBOSE_CLASSNAME[ModelofTable_Class_name])
        
        
        else: # if !loc and ...
            
            if modelmanager_name =='FindCauListForm':
                i_repeat = request.GET['i_repeat']
                fighter_or_single = request.GET['fighter_or_single']
                MAU_THU = request.GET['MAU_THU']
                tai_or_xiu = request.GET['tai_or_xiu']
                repeat_or_xen_ke = request.GET['repeat_or_xen_ke']
                print 'fighter_or_single@@@@',fighter_or_single
                if fighter_or_single=="single":
                    repeat_TAI_lists,repeat_XIU_lists,xenke_TAI_lists,xenke_XIU_lists,more = soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),END_LIST = [int(MAU_THU)],is_in = False)
                else:
                    rs = re.findall('fighter_(.+?)$', fighter_or_single)
                    if rs and repeat_or_xen_ke=='repeat':
                        so_cau_moc_if_fighter_for_find_cau_list_link = int(request.GET['so_cau_moc_if_fighter_for_find_cau_list_link'])
                        repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,more \
                        = soicau_2(qrs = TaiXiu.objects.all().order_by('-phien_so'),
                                   END_LIST = [0],
                                   is_in = False)
                        for_fighter_tai_or_xiu_list = eval('repeat_%s_lists'%rs[0].upper())
                        list_2_vs_above = chon_tren_hoac_duoi_cau_kep(for_fighter_tai_or_xiu_list,so_cau_moc=so_cau_moc_if_fighter_for_find_cau_list_link)
                        repeat_TAI_lists,repeat_XIU_lists,XEN_KE_TAI_lists,XEN_KE_XIU_lists,\
                        more_info_get_from_loop = soicau_2(qrs = list_2_vs_above,END_LIST =[0],is_in = False)
                eval_str = '%s_%s_lists'%(repeat_or_xen_ke,tai_or_xiu.upper())
                print eval_str
                input_list = eval(eval_str)
                filter_so_luong_cau= filter(lambda x: x.so_luong_cau==int(i_repeat), input_list)
                so_luong_cau_tim_duoc =  len(filter_so_luong_cau)
                filter_so_luong_cau = filter_so_luong_cau[0:10]
                querysets =[]
                for x in filter_so_luong_cau:
                    one_row_dict = {}
                    one_row_dict['so_lan_lap'] = x.so_luong_cau
                    one_row_dict['phien_bat_dau'] = mark_safe(u'<a href="/tai_xiu_3/?end=%s">%s</a>'%(x.phien_bat_dau,x.phien_bat_dau))
                    one_row_dict['phien_ket_thuc'] = mark_safe(u'<a href="/tai_xiu_3/?end=%s">%s</a>'%(x.phien_so ,x.phien_so ))
                    khoang_cach_bat_dau_ket_thuc = len(TaiXiu.objects.filter(phien_so__gt=x.phien_bat_dau,phien_so__lt=x.phien_so))
                    one_row_dict['khoang_cach'] = khoang_cach_bat_dau_ket_thuc
                    one_row_dict['khoang_cach_den_last_phien'] = TaiXiu.objects.latest('phien_so').phien_so - x.phien_so
                    querysets.append(one_row_dict)
                #querysets =[{'so_lan_lap':1,'phien_bat_dau':2,'phien_ket_thuc':3}]
                table_notification = u'<h2 class="table_notification">Số lượng cầu tìm được : %s </br>group cầu %s (cầu)</br>,mẫu thử %s,Type: %s,%s,%s</h2>'\
                %(so_luong_cau_tim_duoc,i_repeat,MAU_THU,fighter_or_single,repeat_or_xen_ke,tai_or_xiu)
            else:
                querysets = ModelofTable_Class.objects.all().order_by('-id')
                table_notification = u'<h2 class="table_notification">Tất cả  đối tượng <span class="soluong-notif">(%s)</span> trong database <span class="name-class-notification">%s</span> được hiển thị ở table bên dưới</h2>'%(len(querysets),VERBOSE_CLASSNAME[ModelofTable_Class_name])
        
        
        if status_code != 400:
            table = TableClass(querysets)
            RequestConfig(request, paginate={"per_page": 15}).configure(table)
            dict_render.update({'table':table,'table_notification':table_notification})
    if is_download_table:
        is_dl_bcn = request.GET.get('download-bcn',None)
        if request.GET['downloadtable'] == 'csv':
            return table.as_xls_d4_in_form_py_csv(request)
        elif request.GET['downloadtable'] == 'xls':
            return table.as_xls_d4_in_form_py_xls(request)
    else:
        if is_another_template:
            if form_name =='AutoImportForm':
                pattern = 'drivingtest/taixiu_2.html'
        else:   
            if form_table_template =='form on modal' :# and not click order-sort
                if form:
                    form.verbose_form_name =VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name)
                pattern = 'drivingtest/form_table_manager_for_modal.html'
            else:
                if form_name =='AutoImportForm':
                    #pattern ='drivingtest/form_table_manager_cho_fixed_header.html'
                    pattern ='drivingtest/form_table_manager.html'
                else:
                    pattern ='drivingtest/form_table_manager.html'
        return render(request, pattern,dict_render,status=status_code)
            
def index(request):
    forum_choice_form = ForumChoiceForm()
    #print 'danh sach',[(x['url'],x['url']) for x in danhsachforum]
    #forum_choice_form.fields['forumchoice'].choices = [(x['url'],x['url']) for x in danhsachforum]

    table = UlnewTable(Ulnew.objects.all().order_by('-id'))
    RequestConfig(request, paginate={"per_page": 40}).configure(table)
    
    leechsites = LeechSite.objects.all()
    for leechsite in leechsites:
        leechsite.leech_categories=[]
        one_cate = leechsite.music
        if one_cate:
            leechsite.leech_categories.append(one_cate)
        one_cate = leechsite.tv_show 
        if one_cate:
            leechsite.leech_categories.append(one_cate)
        one_cate = leechsite.anime
        if one_cate:
            leechsite.leech_categories.append(one_cate)
        one_cate = leechsite.movie
        if one_cate:
            leechsite.leech_categories.append(one_cate)
    context_dict = {'forum_choice_form':forum_choice_form,'table': table,'leechsites':leechsites}

    return render_to_response("drivingtest/index.html",
                          context_dict, context_instance=RequestContext(request))

def select_forum(request):
    notification = u'{0}'.format(request.POST['forumchoice'])
    btn = request.POST['btn']
    form = ForumChoiceForm(request.POST)
    form.is_valid()
    forumchoices = form.cleaned_data['forumchoice']
    print forumchoices
    print 'site_user_choose',forumchoices
    print request.POST
    if btn == 'start':
        if 'choiceallentry' in request.POST:
            print 'ban chon het topic'
            entry_id_lists = ['all']
        else:
            entry_id_lists = request.POST.getlist('selection')
        print 'entry_id_lists',entry_id_lists
        for forum_obj in forumchoices:
            try:
                if postdict[forum_obj].is_alive():
                    print 'luong dang chay bam stop cai da'
                    return render(request, 'drivingtest/notice.html', {'notification':'luong dan chay bam stop cai da'})
                else:
                    pass
            except:
                print 'New program...let post '
            postdict[forum_obj] = PostObject(forum_obj,entry_id_lists)
            postdict[forum_obj].login_flag = 1
            postdict[forum_obj].start()
            print 'chuan bi vao ct post o view'
    elif btn == 'stop':
        print 'dang stop...o view'
        for forum_obj in forumchoices:
            try:
                postdict[forum_obj].stop  = True
                print 'type of postdict sau stop ',type(postdict)
                postdict[forum_obj].join()
                notification = 'luong da stop xong, bat dau chay'
                print 'luong da stop xong, bat dau chay'
            except Exception as e:
                print 'luong chua ton tai' ,e
    return render(request, 'drivingtest/notice.html', {'notification':notification})

    
def leech(request):
    notification = u'{0}'.format(request.POST)
    print 'type of notification',type(notification)
    print notification
    cate_page = request.POST['cate-select']
    begin_page = int(request.POST['rangepagebegin'])
    end_page = int(request.POST['rangepageend'])
    #notification = 'notification'
    leech_bai(cate_page, begin_page, end_page)
    return render(request, 'drivingtest/notice.html', {'notification':notification})
def importul(request):
    #notification = u'dang import ul'
    txt = get_link_from_db()
    import_ul_txt_to_myul(txt)
    log=thongbao.log 
    return render(request, 'drivingtest/notice.html', {'notification':thongbao.thongbao,'log':log})
def get_thongbao(request):
    try:
        notification = thongbao.thongbao
        log = thongbao.thongbao
    except Exception as e:
        print e
        notification = thongbao.thongbao
    return render(request, 'drivingtest/notice.html', {'notification':notification,'log':log})
def stop_post(request):
    site_will_post = request.POST['forumchoice']
    print 'site_will_stop',site_will_post
    print 'type of site_will_post', type(site_will_post)
    for site in danhsachforum:
        if site['url'] == site_will_post:
            dict_site = site
    print >>sys.stderr ,'you choice',dict_site
    print 'so luong hien dang ton tai',len(postdict)
    try:
        exit_thread = postdict[dict_site['url']]
        if exit_thread.is_alive():
            postdict[dict_site['url']].stop()
            postdict[dict_site['url']].join()
            notification = 'luong da stop xong, bat dau chay'
            print 'luong da stop xong, bat dau chay'
    except Exception as e:
        print 'luong chua ton tai' ,e
    return render(request, 'drivingtest/notice.html', {'notification':notification})
def edit_entry(request,entry_id):
    entry = Ulnew.objects.get(id = entry_id)
    entryformsave = UlnewForm(request.POST,instance = entry)
    entryformsave.save()
    if entryformsave.is_valid():
        print 'valid'
    else:
        print entryformsave.errors
    notification = 'ban dang sua entry'
    return render(request, 'drivingtest/notice.html', {'notification':notification})
import bbcode
def get_description(request):
    parser = bbcode.Parser()
    parser.add_simple_formatter('img', '<img  src="%(value)s">',replace_links=False)
    if request.method == 'GET':
        entry_id = request.GET['entry_id']
    entry = Ulnew.objects.get(id = entry_id)
    dllink=''
    if  entry.rg:
        dllink = dllink + '\n[code]' + entry.rg + '[/code]\n'
    if  entry.ul:
        dllink = dllink + '\n[code]' + entry.ul + '[/code]\n'    
    content = entry.description  + dllink
    html = parser.format(content)
    entry_form = UlnewForm(instance = entry) 
    notification =  html
    return render(request, 'drivingtest/load_entry.html', {'notification':notification,'form':entry_form,'entry_id':entry_id})



stop_auto_import = True
run_auto_import = False
def user_login(request):
    print request
    
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/omckv2/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('drivingtest/login.html', {}, context) 
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/omckv2/')







   
