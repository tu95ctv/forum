from django.contrib import admin

from drivingtest.models import Ulnew, ForumTable


'''
class Tadmin(admin.ModelAdmin):
    search_fields = ['site_name_1','site_id_3g']
    
class PermissionAdmin(admin.ModelAdmin):
    model = Permission
    #fields = ['name','codename']
class Table3gAdmin(admin.ModelAdmin):
    list_display=('site_name_1','site_id_3g','Ngay_Phat_Song_3G')
    search_fields = ('site_name_1','site_id_3g')
    list_filter = ('Cabinet','RNC')
    date_hierarchy = 'Ngay_Phat_Song_3G'
    ordering = ('Ngay_Phat_Song_3G','-site_name_1')
    filter_horizontal = ('du_an',)
    raw_id_fields = ('Cabinet',)
    #dfields =('site_name_1','site_id_3g','Ngay_Phat_Song_3G')
    #fields = ['name','codename']
'''
#admin.site.register(Ulnew,Table3gAdmin)
admin.site.register(Ulnew)
admin.site.register(ForumTable)