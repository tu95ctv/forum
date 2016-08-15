print 'in url 3'
from django.conf.urls import patterns, url
from drivingtest import views
from django.conf import settings
from django.contrib import admin

# UNDERNEATH your urlpatterns definition, add the following two lines:
admin.autodiscover()
urlpatterns = patterns('',
        
        #################OMCKV2####################

        
        
        
        #######FORUM
        
        
        
        url(r'^$', views.index, name='index'),
        url(r'^omckv2/modelmanager/(?P<modelmanager_name>\w+)/(?P<entry_id>.*?)/$', views.modelmanager, name='suggestion'),
        url(r'^taixiu/$', views.taixiu, name='index'),
        url(r'^taixiu2/$', views.taixiu2, name='index'),
        url(r'^import100phien/$', views.import100phien, name='index'),
        url(r'^select_forum/$',  views.select_forum, name='select_forum'),
        url(r'^get-thongbao/$',  views.get_thongbao, name='get-thongbao'),
        url(r'^leech/$',  views.leech, name='leech'),
        url(r'^importul/$',  views.importul, name='importul'),
        url(r'^stop-post/$',  views.stop_post, name='stop-post'),
        url(r'^get_description/$',  views.get_description, name='tao-object'),
        url(r'^edit_entry/(?P<entry_id>\d+)/$',  views.edit_entry, name='edit_entry'),
        
        
        ##########CHUNG
        #url(r'^$', views.index, name='index'),
        url(r'^login/$',views.user_login,name="user_login"),
        url(r'^logout/$',views.user_logout,name="user_logout"),
        #url(r'^omckv2/registers/$', views.register, name='register'), # ADD NEW PATTERN! 
                   
        )
if settings.DEBUG:
    urlpatterns += patterns( 
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
 
    
    
    