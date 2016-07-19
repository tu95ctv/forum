# -*- coding: utf-8 -*-
'print in form 4'
from django import forms
from drivingtest.models import Ulnew
from crispy_forms.layout import Submit, Field
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django.utils.html import   strip_tags
from django.forms.fields import DateTimeField, FileField
from datetime import datetime
from django.core.exceptions import ValidationError
from toold4 import luu_doi_tac_toold4
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from crispy_forms.bootstrap import AppendedText
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,HTML, Div
from crispy_forms.bootstrap import TabHolder, Tab
from django.template.context import Context, RequestContext
from django.template.loader import get_template
import re
from django_tables2_reports.tables import TableReport
from django.template.base import Template
from exceptions import IndexError
from django_tables2_reports.config import RequestConfigReport
from django.http.response import HttpResponse, StreamingHttpResponse
import xlwt
import collections
from django_tables2_reports.csv_to_xls.xlwt_converter import write_row
import csv







#END TABLE###########END TABLE####################END TABLE#############END TABLE####END TABLE########END TABLE#######END TABLE#####
#UL
        
        









#TRANGPHUKIEN------------------------------------------







#ULLLLLLL---------------------------

class ForumChoiceForm(forms.Form):
    forumchoice = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,label="Xin chon forum")
class UlnewForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    description= forms.CharField(widget=forms.Textarea(attrs={'class': 'special'}))
    class Meta:
        model = Ulnew
        
#Table for UL
#PersonTable(tables.Table)
class PersonTable(TableReport):
    selection = tables.CheckBoxColumn(accessor="pk", orderable=False)
    description = tables.Column(verbose_name="Mo ta")
    is_posted_shaanig = tables.Column(empty_values=())
    title = tables.Column()
    def render_is_posted_shaanig(self):
        return 'hk'
    def render_description(self,value):
        return value[:10]
    class Meta:
        model = Ulnew
        attrs = {"class": "paleblue"}
        sequence = ("selection", "date")
        
        
               
