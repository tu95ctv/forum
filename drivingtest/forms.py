# -*- coding: utf-8 -*-
'print in form 4'
from django import forms
from drivingtest.models import Ulnew, PostLog, ForumTable, TaiXiu
#from crispy_forms.layout import Submit, Field
import django_tables2 as tables
#from django.utils.safestring import mark_safe
#from django.utils.html import   strip_tags
from django.forms.fields import FileField
#from datetime import datetime
from django.core.exceptions import ValidationError
#from toold4 import luu_doi_tac_toold4
#from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
#from django.core.validators import RegexValidator
#from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Layout,HTML, Div
#from crispy_forms.bootstrap import TabHolder, Tab
#from django.template.context import Context, RequestContext
#from django.template.loader import get_template
#import re
from django_tables2_reports.tables import TableReport
from django.utils.safestring import mark_safe
from crispy_forms.layout import Submit, Layout, Div, HTML
from datetime import datetime

#from django.template.base import Template
#from exceptions import IndexError
#from django_tables2_reports.config import RequestConfigReport
#from django.http.response import HttpResponse, StreamingHttpResponse
#import xlwt
#import collections
#from django_tables2_reports.csv_to_xls.xlwt_converter import write_row
#import csv

D4_DATETIME_FORMAT = '%H:%M %d/%m/%Y'#danh cho form va widget





#END TABLE###########END TABLE####################END TABLE#############END TABLE####END TABLE########END TABLE#######END TABLE#####
#UL
        
        









#TRANGPHUKIEN------------------------------------------







#ULLLLLLL---------------------------

class ForumChoiceForm(forms.Form):
    CHOICES = [(x.id,x.url) for x in ForumTable.objects.all()]
    #forumchoice = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple,label="Xin chon forum")
    forumchoice = forms.ModelMultipleChoiceField(ForumTable.objects.all(),widget=forms.CheckboxSelectMultiple,label="Xin chon forum")
    def __init__(self, *args, **kwargs):
        super(ForumChoiceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        #self.helper.layout = Layout(Div('chon_loai_de_quan_ly'))
        self.helper.form_tag = False
class UlnewForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    description= forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}))
    class Meta:
        model = Ulnew
        fields = '__all__' 
#Table for UL
#PersonTable(tables.Table)
class FindCauListTable(TableReport):
    so_lan_lap = tables.Column(verbose_name=u"Số lần lặp")
    phien_bat_dau = tables.Column(verbose_name=u"Phiên bắt đầu")
    phien_ket_thuc = tables.Column(verbose_name=u"Phiên kết thúc")
    khoang_cach = tables.Column(verbose_name=u"Khoảng cách") 
    class Meta:
        attrs = {"class": "table-bordered","id": "FindCauList"}
class RepeatTable(TableReport):
    so_lan_lap = tables.Column(verbose_name=u"Repeat Times")
    mau_thu = tables.Column(verbose_name=u"Số mẫu")
    lythuyet_repeat_xac_suat_i = tables.Column(verbose_name=u"Lý thuyết")
    tai_repeat_list_count = tables.Column(verbose_name=u"Tài Repeat")
    xiu_repeat_list_count = tables.Column(verbose_name=u"Xỉu Repeat")
    class Meta:
        attrs = {"class": "table-bordered","id": "repeat-table"}
class RepeatTable2(TableReport):
    i_repeat = tables.Column(verbose_name=u"Repeat Times")
    Probability_theory = tables.Column(verbose_name=u"Probability_theory")
    tai_xiu_repeat_description = tables.Column(verbose_name=u"Tài Repeat")
    class Meta:
        attrs = {"class": "table-bordered","id": "repeat-table2"}
class TaiXiuXiuTaiTable(TableReport):
    mau_thu = tables.Column(verbose_name=u"Số mẫu")
    tai = tables.Column(verbose_name=u"Tài")
    xiu = tables.Column(verbose_name=u"Xỉu")
    tai_xiu = tables.Column(verbose_name=u"Tài-Xỉu")
    tai_tai = tables.Column(verbose_name=u"Tài-Tài")
    xiu_tai = tables.Column(verbose_name=u"Xỉu-Tài")
    xiu_xiu = tables.Column(verbose_name=u"Xỉu-Xỉu")
    class Meta:
        attrs = {"class": "table-bordered","id": "txxt-table"}
 


class Thoi_gian_cho_su_lap_lai_Table(TableReport):
    so_lan_lap = tables.Column(verbose_name=u"so_lan_lap")
    xac_suat = tables.Column(verbose_name=u"xac_suat")
    so_phien_can_thiet = tables.Column(verbose_name=u"so_phien_can_thiet")
    so_phut = tables.Column(verbose_name=u"so_phut")
    so_gio = tables.Column(verbose_name=u"so_gio")
    so_ngay = tables.Column(verbose_name=u"so_ngay")
    xiu_xiu = tables.Column(verbose_name=u"Xỉu-Xỉu")
    class Meta:
        attrs = {"class": "table-bordered","id": "txxt-table"}
        
               
class Tong3DiceTable(TableReport):
    tong = tables.Column()
    tai_or_xiu = tables.Column()
    mau_thu = tables.Column()
    phan_tram = tables.Column()

    class Meta:
        attrs = {"class": "table-bordered","id": "Tong3Dice-table"}        
class UlnewTable(TableReport):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    description = tables.Column(verbose_name="Mo ta")
    is_post_amaforum= tables.Column(accessor="pk")
    title = tables.Column()
    #is_report_download = True
    edit_column = tables.Column(accessor="pk", orderable=False,)    
    def render_edit_column(self,value):
        return mark_safe('<div><button class="btn  btn-default edit-entry-btn-on-table" id= "%s" type="button">Edit</button></div></br>'%value)
    def render_is_post_amaforum(self,value):
        try:
            postLog_instance = PostLog.objects.filter(forum = ForumTable.objects.get(url='http://amaderforum.com/'),posted_topic__id = value)[0]
            return postLog_instance.posted_link
        except IndexError:
            return None
    def render_description(self,value):
        return value[:10]
    class Meta:
        model = Ulnew
        attrs = {"class": "table-bordered","id": "ulnew-table"}
        #sequence = ("selection", "date")
        #fields = '__all__' 
class ImportForm(forms.Form):
    text_html_100phien = forms.CharField(widget = forms.Textarea(attrs={'id':'text_html_100phien_id'}))
    def __init__(self, *args, **kwargs):
        super(ImportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'model-manager'
        self.helper.form_action = '/omckv2/modelmanager/ImportForm/new/'
        self.helper.add_input(Submit('add-new', 'ADD NEW',css_class="submit-btn"))
class Import100PhienForm(forms.Form):
    current_phien_plus_one = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        super(Import100PhienForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'model-manager'
        self.helper.form_action = '/omckv2/modelmanager/Import100PhienForm/new/'
        self.helper.add_input(Submit('add-new', 'import 100 phien',css_class="submit-btn"))        
class SoiCauForm(forms.Form):
    end_phien = forms.IntegerField(widget = forms.TextInput(attrs={'id':'end-phien-input'}))
    so_cau_can_soi = forms.IntegerField(widget = forms.TextInput(attrs={'id':'end-phien-input'}),initial=100)
    def __init__(self, *args, **kwargs):
        soi_cau_html = kwargs.pop('soi_cau_html',None)
        super(SoiCauForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'model-manager'
        self.helper.form_class = 'is_table_not '
        self.helper.form_action = '/omckv2/modelmanager/SoiCauForm/new/'
        self.helper.add_input(Submit('soi-cau', 'Soi Cau',css_class="submit-btn"))
        #css_class='col-sm-4'
        if soi_cau_html:
            html = HTML(soi_cau_html)
        else:
            html = HTML('')
        self.helper.layout = Layout(Div(html,Div('end_phien','so_cau_can_soi',css_class='col-sm-4'),css_class="row"))
class AutoImportForm(forms.Form):
    now_phien = forms.IntegerField()
    

    def __init__(self, *args, **kwargs):
        super(AutoImportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(form=self)
        self.helper.form_id = 'model-manager'
        self.helper.form_action = '/omckv2/modelmanager/AutoImportForm/new/'
        self.helper.add_input(Submit('start-auto-import-phien', 'Start',css_class="submit-btn"))
        self.helper.add_input(Submit('stop-auto-import-phien', 'Stop',css_class="submit-btn"))
        self.helper.add_input(Submit('tb-auto-import-phien', 'thongbao',css_class="submit-btn"))
        self.helper.add_input(Submit('poll-auto-import-phien', 'poll',css_class="submit-btn"))
class TaiXiuTable(TableReport):
    jquery_url= '/omckv2/modelmanager/TaiXiuForm/new/'
    is_report_download = True
    edit_column = tables.Column(accessor="pk", orderable=False,)    
    def render_edit_column(self,value):
        return mark_safe('<div><button class="btn  btn-default edit-entry-btn-on-table" id= "%s" type="button">Edit</button></div></br>'%value)       
    class Meta:
        model = TaiXiu
        attrs = {"class": "lenh-table table-bordered"}      
class BaseFormForManager(forms.ModelForm):
    modal_add_title_style = 'background-color:#337ab7'
    design_common_button = True
    #modal_edit_title_style = 'background-color:#5bc0de' 
    modal_edit_title_style = 'background-color:#5cb85c' 
    modal_prefix_title = "Detail"
    allow_edit_modal_form = True
    is_admin_set_create_html_table_edittion_history = False
    def __init__(self,*args, **kw):
        self.loai_form_for_design_btn_n_title_style = kw.pop('form_table_template',None)
        self.is_loc = kw.pop('loc',False)
        self.model_fnames = self.Meta.model._meta.get_all_field_names()
        force_allow_edit = kw.pop('force_allow_edit',False)
        self.request = kw.pop('request',None)
        self.khong_show_2_nut_cancel_va_loc = kw.pop('khong_show_2_nut_cancel_va_loc',None)
        super(BaseFormForManager, self).__init__(*args, **kw)
        self.is_has_instance = bool(self.instance and self.instance.pk)
        self.Form_Class_Name = self.__class__.__name__
        if self.is_admin_set_create_html_table_edittion_history:
            self.create_html_table_edittion_history()
        self.helper = FormHelper(form=self)
        if not self.is_bound:
            if not self.is_has_instance:
                if self.Form_Class_Name =='TaiXiuForm': 
                    initial = {'phien_so':TaiXiu.objects.latest('phien_so').phien_so + 1}
                    self.initial.update(initial)
         
        if self.is_loc:
            self._validate_unique = False
        else:
            self._validate_unique = True
        
        if self.design_common_button:
            if self.loai_form_for_design_btn_n_title_style =='form on modal' and  self.allow_edit_modal_form or force_allow_edit or self.khong_show_2_nut_cancel_va_loc:
                self.helper.add_input(Submit('add-new', 'ADD NEW',css_class="submit-btn"))
            elif self.loai_form_for_design_btn_n_title_style =='form on modal' and not self.allow_edit_modal_form:
                pass
            else: #loai_form_for_design_btn_n_title_style =='normal form template' or None
                self.helper.add_input(Submit('add-new', 'ADD NEW',css_class="submit-btn"))
                self.helper.add_input(Submit('cancel', 'Cancel',css_class="btn-danger cancel-btn"))
                self.helper.add_input(Submit('manager-filter', 'Lọc',css_class="btn-info loc-btn"))
        self.helper.form_id = 'model-manager'
        self.update_action_and_button()
    def update_action_and_button(self):
        self.helper.form_action = '/omckv2/modelmanager/'+self.Form_Class_Name +'/' + (str(self.instance.pk) if self.is_has_instance else 'new')  + '/'
        print self.helper.form_action 
        if self.helper.inputs:
            if not self.is_has_instance:# only get, chua save
                try:
                    self.helper.inputs[0].value = "ADD NEW"
                    self.helper.inputs[0].field_classes = self.helper.inputs[0].field_classes.replace('btn-warning','btn-primary')
                except IndexError:
                    pass
                if self.loai_form_for_design_btn_n_title_style =='form on modal':
                    self.modal_prefix_title="ADD"
                    self.modal_title_style = self.modal_add_title_style
            else:
                try:
                    self.helper.inputs[0].value = "EDIT"
                    self.helper.inputs[0].field_classes  = self.helper.inputs[0].field_classes.replace('btn-primary','btn-warning')
                except IndexError:
                    pass
                if self.loai_form_for_design_btn_n_title_style =='form on modal':
                    self.modal_prefix_title="Detail"
                    self.modal_title_style = getattr(self,'modal_edit_title_style',None)
    
    
     
    
    def _post_clean(self):
        if self.is_loc or  self._errors :
            pass
        else:
            super(BaseFormForManager,self)._post_clean()
   
    def _clean_fields(self):
        for name, field in self.fields.items():
            # value_from_datadict() gets the data from the data dictionaries.
            # Each widget type knows how to retrieve its own data, because some
            # widgets split data over several HTML fields.
            value = field.widget.value_from_datadict(self.data, self.files, self.add_prefix(name))
            try:
                if isinstance(field, FileField):
                    initial = self.initial.get(name, field.initial)
                    value = field.clean(value, initial)
                else:
                    value = field.clean(value)
                self.cleaned_data[name] = value
                if hasattr(self, 'clean_%s' % name):
                    value = getattr(self, 'clean_%s' % name)()
                    self.cleaned_data[name] = value
            except ValidationError as e:
                e_code = getattr(e,'code',None)
                if self.is_loc and e_code=='required':
                    self.cleaned_data[name] = value
                    continue
                self._errors[name] = self.error_class(e.messages)
                if name in self.cleaned_data:
                    del self.cleaned_data[name]# co san rua roi, copy thoi
    def clean(self):
        # thieu unique_valid
        if self.is_loc or  self._errors :
            pass
        else:
            errors= None
            model_fnames = self.model_fnames
            if self.instance and self.instance.pk:#if edit
                if not self.request.user.is_superuser:# lien quan den is_duoc_tao_truoc
                    try:
                        is_duoc_tao_truoc_attr_of_instance = getattr(self.instance,'is_duoc_tao_truoc')
                    except AttributeError:# Neu self.instance khong co is_duoc_tao_truoc attr
                        is_duoc_tao_truoc_attr_of_instance =None
                    if is_duoc_tao_truoc_attr_of_instance != None:
                        if 'is_duoc_tao_truoc' in self.fields:# xem xem nguoi dung co thay doi gia tri nay o tren form khong
                            value  = self.cleaned_data.get('is_duoc_tao_truoc')
                            if  value!=self.instance.is_duoc_tao_truoc:
                                msg = u'Bạn không được thay đổi field này'
                                self.add_error('is_duoc_tao_truoc', msg)
                                
                        if is_duoc_tao_truoc_attr_of_instance==True:
                            name_of_instance = self.instance.Name
                            if name_of_instance != self.cleaned_data['Name']:
                                msg = u'Bạn không được thay đổi field Name'
                                self.add_error('is_duoc_tao_truoc', msg)
                
                if not errors:
                    exclude = getattr(self.Meta, 'exclude',[])
                    if 'ngay_gio_sua'in model_fnames:
                        if 'ngay_gio_sua' in exclude:
                            self.instance.ngay_gio_sua = datetime.now()
                        else:
                            self.cleaned_data['ngay_gio_sua'] = datetime.now()

                            
                            
                    if 'ngay_gio_tao'in model_fnames:# thuc ra khogn can thiet cung duoc, dinh huong lai thoi
                        if 'ngay_gio_tao'  not in exclude:
                            self.cleaned_data['ngay_gio_tao'] = self.instance.ngay_gio_tao
                    if 'nguoi_tao'in model_fnames:
                        if 'nguoi_tao'  not in exclude:# Neu nguoi tao in exclude thi tot roi, neu no khong in ma thay doi lung tung thi phai dinh huong
                            self.cleaned_data['nguoi_tao'] = self.instance.nguoi_tao
                           
                    if 'ly_do_sua' in model_fnames :
                        if 'ly_do_sua' in exclude:
                            self.instance.ly_do_sua = self.request.GET['edit_reason']
                        else:
                            self.cleaned_data['ly_do_sua'] = self.request.GET['edit_reason']
            else: # if add new
                if not self.is_loc:
                    exclude = getattr(self.Meta, 'exclude',[])
                    if 'ngay_gio_tao'in model_fnames:
                        if 'ngay_gio_tao' in exclude:
                            self.instance.ngay_gio_tao = datetime.now()
                        else:
                            self.cleaned_data['ngay_gio_tao'] = datetime.now()
                    if 'nguoi_tao'in model_fnames:
                        if 'nguoi_tao' in exclude:
                            self.instance.nguoi_tao = self.request.user
                        else:
                            self.cleaned_data['nguoi_tao'] = self.request.user
                    
                    
                    if 'nguoi_sua_cuoi_cung' in model_fnames:
                        if 'nguoi_sua_cuoi_cung' in exclude:
                            self.instance.nguoi_sua_cuoi_cung = None
                        else:
                            self.cleaned_data['nguoi_sua_cuoi_cung'] = None
                    # vi ly do khong co clean_nguoi sua_cuoi_cung nen  trong post_clean phai them vao
                    if 'is_duoc_tao_truoc' in model_fnames and not self.request.user.is_superuser:#Neu add New thi field is_duoc_tao_truoc nay luon False
                        if 'is_duoc_tao_truoc' in exclude:
                            self.instance.is_duoc_tao_truoc = False
                        else:
                            self.cleaned_data['is_duoc_tao_truoc'] = False
        return self.cleaned_data
    
class TaiXiuForm(BaseFormForManager):
    ngay_gio_tao =forms.DateTimeField(label=u"Ngày giờ tạo",input_formats = [D4_DATETIME_FORMAT],required =False,widget =forms.DateTimeInput(format=D4_DATETIME_FORMAT,attrs={"readonly":"readonly"}))
    #id =forms.CharField(required =  False,widget = forms.TextInput(attrs={"readonly":"readonly"}))
    #ngay_gio_tao =forms.DateTimeField(label=u"Ngày giờ tạo",input_formats = [D4_DATETIME_FORMAT],required =False,widget =forms.DateTimeInput(format=D4_DATETIME_FORMAT,attrs={"readonly":"readonly"}))
    def __init__(self, *args, **kwargs):
        super(TaiXiuForm, self).__init__(*args, **kwargs)
        #self.helper[-5:].wrap_together(Field, css_class='col-sm-6')
        #self.helper[1:3].wrap(Fieldset, "legend of the fieldset")
        #self.helper[1:3].wrap(Fieldset, "legend of the fieldset", css_class="fieldsets")
        
        #self.helper.layout.append(HTML('ILOVE U'))
    class Meta:
        #exclude = ('Name_khong_dau',)
        model = TaiXiu
        fields = '__all__'
        #widgets = { 'ghi_chu': forms.Textarea(attrs={'autocomplete': 'off'})            } 
