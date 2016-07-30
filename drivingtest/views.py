# -*- coding: utf-8 -*-
#from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from models import Ulnew,ForumTable, PostLog, LeechSite, thongbao, postdict,autoimportdict
import forms
from drivingtest.forms import  ForumChoiceForm, UlnewForm, UlnewTable,\
    RepeatTable, TaiXiuXiuTaiTable, Tong3DiceTable, TaiXiuForm, TaiXiuTable,\
    ImportForm, Thoi_gian_cho_su_lap_lai_Table, AutoImportForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from __main__ import sys
from fetch_website import danhsachforum, PostObject, leech_bai,\
    get_link_from_db, import_ul_txt_to_myul
from exceptions import Exception
from django_tables2_reports.config import RequestConfigReport as RequestConfig
from drivingtest.models import TaiXiu, Notification_global_from_model_module,\
    Da_import_xong_global_from_model_module, Tb_import
from soicau import create_giong_nhau_khac_nhau_lists,\
    test_xac_suat_tong_3_dice_database, phien_100_to_html,\
    create_how_many_phien_for_same_cau, autoimport, AutoImportObject
from django.db.models.aggregates import Min, Max, Count
import re
from django.utils import timezone
from django.db.models import CharField,DateTimeField,DateField, AutoField
from datetime import datetime
VERBOSE_CLASSNAME ={'TaiXiu':u'Nguyên Nhân'} 
from django.db.models import Q

################CHUNG######################
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
    return repeat_table_2,taiXiuXiuTai_Table_2,string_tai_xiu_soi_cau,xen_ke_or_giong_nhau_lists


def taixiu(request,for_only_return_dict = False):
    
    IS_display_xen_ke = True
    rp_tx_combines = []
    END_CAN_LAY = [0,512,256,128,100,68,64,32,16]
    END_CAN_LAY.reverse()
    last_phien_so =  TaiXiu.objects.latest('phien_so').phien_so
    taixiu_table = TaiXiuTable(TaiXiu.objects.all().order_by('-phien_so'))
    RequestConfig(request, paginate={"per_page": 15}).configure(taixiu_table) 
    for END in END_CAN_LAY:
        if END:
            tai_xiu_lists = TaiXiu.objects.all().order_by('-phien_so')[0:END]
        else:
            tai_xiu_lists = TaiXiu.objects.all().order_by('-phien_so')
        repeat_table,taiXiuXiuTai_Table,string_tai_xiu_soi_cau,xen_ke_or_giong_nhau_lists = create_table(tai_xiu_lists)
        repeat_table.so_mau = END
        taiXiuXiuTai_Table.len = len(tai_xiu_lists)
        one_tuple = [taiXiuXiuTai_Table,repeat_table]
        taiXiuXiuTai_Table_xk=None
        repeat_table_xk = None
        
        if END ==128:
            tai_xiu_lists_100=tai_xiu_lists
            string_tai_xiu_soi_cau_100 = string_tai_xiu_soi_cau
        if IS_display_xen_ke:
            xen_ke_or_giong_nhau_lists
            repeat_table_xk,taiXiuXiuTai_Table_xk,string_tai_xiu_soi_cau,xen_ke_or_giong_nhau_lists_xk = create_table(xen_ke_or_giong_nhau_lists,show_description = 'xen ke type',is_created_xenKe_list = False)    
        
        one_tuple.extend((taiXiuXiuTai_Table_xk,repeat_table_xk))
        rp_tx_combines.append(one_tuple)
    
    tong_3_dict_lists = test_xac_suat_tong_3_dice_database(tai_xiu_lists_100)
    tong_3_table = Tong3DiceTable(tong_3_dict_lists)
    autoImportForm = AutoImportForm()
    
    if not for_only_return_dict:
        thoi_gian_cho_su_lap_lai_Table = Thoi_gian_cho_su_lap_lai_Table(create_how_many_phien_for_same_cau())
        taiXiuForm = TaiXiuForm ()
        importForm = ImportForm()
        render_dict = {'thoi_gian_cho_su_lap_lai_Table':thoi_gian_cho_su_lap_lai_Table,\
                                                       'importForm':importForm,\
                                                       'taiXiuForm':taiXiuForm,'taixiu_table':taixiu_table,\
                                                       
                                                       'tong_3_table':tong_3_table,\
                                                       'rp_tx_combines':rp_tx_combines,
                                                       'string_tai_xiu_soi_cau_100':string_tai_xiu_soi_cau_100,\
                                                       'last_phien_so':last_phien_so,\
                                                       'autoImportForm':autoImportForm}
    else:
        render_dict ={
                                                       'tong_3_table':tong_3_table,\
                                                       'rp_tx_combines':rp_tx_combines,
                                                       'string_tai_xiu_soi_cau_100':string_tai_xiu_soi_cau_100,\
                                                       'last_phien_so':last_phien_so,\
                                                       }
        return render_dict
    
    return render(request, 'drivingtest/taixiu.html', render_dict)


 
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
        FormClass = eval('forms.' + form_name)#repeat same if loc
        ModelOfForm_Class_name = re.sub('Form$','',form_name,1)
        print 'form_name @@@@@@@@@@@@2',form_name
        if form_name =='NhanTinUngCuuForm':# only form not model form
            form = FormClass(initial = {'noi_dung_tin_nhan':'abc'})
            form.modal_title_style = 'background-color:#337ab7'
            form.modal_prefix_title  = 'Nội Dung Nhắn Tin'
            form_notification= u'<h2 class="form-notification text-primary">Nhấn nút copy, sẽ copy nội dung tn vào clipboard</h2>'
            dict_render = {'form':form,'form_notification':form_notification}
        elif form_name =='ImportForm':
            print 'ok','import100phienForm'
            #len_x = request.POST['text_html_100phien']
            tb = phien_100_to_html()
            form = FormClass(initial= {'text_html_100phien':tb})
            
            dict_render = {'form':form,'form_notification':u'<h2 class="form-notification text-primary">OK ,%s,%s</h2>'%(datetime.now(),tb)}
            
            
           
                
                
                
                
        elif form_name =='AutoImportForm':
            form = FormClass()
            which_start_or_stop_btn = request.GET['which-start-or-stop-btn']
            if which_start_or_stop_btn=="Start":
                
                #tb = autoimport()
                
                try:
                    luong = autoimportdict["luong autoimport"]
                    if luong.is_alive():
                        can_khoi_tao = False
                    else:
                        can_khoi_tao = True
                except:
                    can_khoi_tao = True
                
                if not can_khoi_tao :
                    dict_render = {'form':form,'form_notification':u'<h2 class="form-notification text-primary">luong da chay roi!! ,%s</h2>'%(datetime.now())}
                else:
                    Da_import_xong_global_from_model_module = False
                    print '@@@@@@@@@Da_import_xong_global_from_model_module',Da_import_xong_global_from_model_module
                    autoimportdict["luong autoimport"] = AutoImportObject()
                    autoimportdict["luong autoimport"].login_flag = 1
                    autoimportdict["luong autoimport"].start()
                    print '@@@@@@@@@Da_import_xong_global_from_model_module',Da_import_xong_global_from_model_module
                    if Tb_import.Da_import_xong_global_from_model_module:
                        is_another_template = True
                        dict_render  = taixiu(request,for_only_return_dict = True)
                        dict_render.update ({'autoImportForm':form,'form_notification':u'<h2 class="form-notification text-primary">OK ,%s,%s</h2>'%(datetime.now(),Tb_import.thongbao)})
            elif which_start_or_stop_btn=="Stop":
                try:
                    Da_import_xong_global_from_model_module = False
                    autoimportdict["luong autoimport"].stop  = True
                    autoimportdict["luong autoimport"].join()
                    dict_render = {'form':form,'form_notification':u'<h2 class="form-notification text-primary">Stop ,%s</h2>'%(datetime.now())}
                except Exception as e:
                    
                    dict_render = {'form':form,'form_notification':u'<h2 class="form-notification text-primary">Chua co luon sao bam Stop!!!%s</h2>'%(datetime.now())}
            elif which_start_or_stop_btn=="thongbao":   
                dict_render.update ({'form':form,'form_notification':u'<h2 class="form-notification text-primary">thong bao::: ,%s,%s,luong dang live?%s</h2>'%(datetime.now(),Tb_import.thongbao,autoimportdict["luong autoimport"].is_alive())})
                
                
                
                
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
                        form_notification = u'<h2 class="form-notification text-primary">Form trống để tạo instance <span class="name-class-notification">%s</span> mới </h2>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name])
                    else:
                        form_notification = u'<h2 class="form-notification text-warning"> Đang hiển thị form của Đối tượng <span class="name-class-notification">%s</span> có ID là %s</h2>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],entry_id)
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
                    print '@@@@@@@@@@@@@@@@@@@@@@@i wnat see'
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
                        form_notification = u'<h2 class="form-notification text-success">Bạn vừa tạo thành công 1 Đối tượng <span class="name-class-notification">%s</span> có ID là %s,bạn có thế tiếp tục edit nó</h2>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],id_string)
                    else:
                        form_notification = u'<h2 class="form-notification text-success">Bạn vừa Edit thành công 1 Đối tượng <span class="name-class-notification">%s</span>  có ID là %s,bạn có thế tiếp tục edit nó</h2>'%(VERBOSE_CLASSNAME[ModelOfForm_Class_name],id_string)
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
            
            querysets = ModelofTable_Class.objects.all().order_by('-id')
            table_notification = u'<h2 class="table_notification">Tất cả  đối tượng <span class="soluong-notif">(%s)</span> trong database <span class="name-class-notification">%s</span> được hiển thị ở table bên dưới</h2>'%(len(querysets),VERBOSE_CLASSNAME[ModelofTable_Class_name])
        if status_code != 400:
            table = TableClass(querysets)
            RequestConfig(request, paginate={"per_page": per_page}).configure(table)
            dict_render.update({'table':table,'table_notification':table_notification})
    if is_download_table:
        is_dl_bcn = request.GET.get('download-bcn',None)
        if request.GET['downloadtable'] == 'csv':
            return table.as_xls_d4_in_form_py_csv(request)
        elif request.GET['downloadtable'] == 'xls':
            return table.as_xls_d4_in_form_py_xls(request)
    else:
        if is_another_template:
            if form_name =='AutoImportForm' and which_start_or_stop_btn=="Start":
                pattern = 'drivingtest/taixiu.html'
        else:
            if form_table_template =='form on modal' and is_form :# and not click order-sort
                if form:
                    form.verbose_form_name =VERBOSE_CLASSNAME.get(ModelOfForm_Class_name,ModelOfForm_Class_name)
                pattern = 'drivingtest/form_table_manager_for_modal.html'
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









   
