# -*- coding: utf-8 -*-
#from django.db.models import F
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from models import Ulnew,ForumTable, PostLog, LeechSite, thongbao, postdict
    
from drivingtest.forms import  ForumChoiceForm, UlnewForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from __main__ import sys
from fetch_website import danhsachforum, PostObject, leech_bai,\
    get_link_from_db, import_ul_txt_to_myul
from drivingtest.forms import PersonTable
from exceptions import Exception
from django_tables2_reports.config import RequestConfigReport as RequestConfig




################CHUNG######################

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








 

def index(request):
    forum_choice_form = ForumChoiceForm()
    # [('1','a'),('2','b')] [(x['url'],x['url']) for x in danhsachforum]
    print 'danh sach',[(x['url'],x['url']) for x in danhsachforum]
    forum_choice_form.fields['forumchoice'].choices = [(x['url'],x['url']) for x in danhsachforum]
    #return render(request, 'drivingtest/index.html', context_dict)
    leech_entry_lists = Ulnew.objects.all().order_by('-id')
    table = PersonTable(Ulnew.objects.all())
    RequestConfig(request, paginate={"per_page": 40}).configure(table)

    #return render(request, 'drivingtest/people.html', {'table': table})
    
    siteobj = ForumTable.objects.get(url = 'http://amaderforum.com/')
    shaanigsite = ForumTable.objects.get(url = 'http://www.shaanig.com/')
    for entry in leech_entry_lists:
        try:
                #posted_ama = Ulnew.objects.get(forumback=siteobj,postLog__Ulnew=entry)
                posted_ama= PostLog.objects.get(forum=siteobj, Ulnew=entry)
                entry.is_post_amaforum = posted_ama.pested_link
               
                #entry.is_post_amaforum = 'yes'
        except:
            entry.is_post_amaforum = 'N'
        try:
                #posted_ama = Ulnew.objects.get(forumback=siteobj,postLog__Ulnew=entry)
          
                posted_shaanigsite= PostLog.objects.get(forum=shaanigsite, Ulnew=entry)
                entry.is_post_shaanig = posted_shaanigsite.pested_link
                #entry.is_post_amaforum = 'yes'
        except:
            entry.is_post_shaanig = 'N'
    
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
    
    '''
    
    leechsite.HDmovie
    leechsite.software
    leechsite.game
    leechsite.anime
    leechsite.mobile
    leechsite.ebook
    '''
    #context_dict = {'forum_choice_form':forum_choice_form,'leech_entry_lists':leech_entry_lists,'leechsites':leechsites}
    context_dict = {'forum_choice_form':forum_choice_form,'leech_entry_lists':leech_entry_lists,'table': table,'leechsites':leechsites}

    return render_to_response("drivingtest/index.html",
                          context_dict, context_instance=RequestContext(request))

def select_forum(request):
    try:
        forum_choice_form = ForumChoiceForm(request.POST)
        if forum_choice_form.is_valid():
            print 'valid'
        else:
            print 'notvalid'
        print 'type(request.POST)',type(request.POST)
        print 'request.POST',request.POST
        notification =  u'{0}'.format(request.body) + '\n' + u'{0}'.format(request.POST['forumchoice'])
        btn = request.POST['btn']
        #return render(request, 'drivingtest/notice.html', {'notification':notification})
        site_will_posts = request.POST.getlist('forumchoice')
        print 'site_will_post',site_will_posts
        #print 'type of site_will_post', type(site_will_post)
        post_sitedict_list = []
        #stuff = map(lambda w: bbcode.find(w) , prefix_links)
        for site_will_post in site_will_posts:
            for site in danhsachforum:
                    if site['url'] == site_will_post:
                        post_sitedict_list.append(site)
        print >>sys.stderr ,'you choice',post_sitedict_list
        print 'so luong hien dang ton tai',len(postdict)
        if btn == 'start':
        
            if 'choiceallentry' in request.POST:
                print 'ban chon het topic'
                entry_id_lists = ['all']
            else:
                entry_id_lists = request.POST.getlist('selection')
            print 'entry_id_lists',entry_id_lists
            
            
            for dict_site in post_sitedict_list:
                try:
                    if postdict[dict_site['url']].is_alive():
                        print 'luong dang chay bam stop cai da'
                        return render(request, 'drivingtest/notice.html', {'notification':'luong dan chay bam stop cai da'})
                    else:
                        pass
                except:
                    print 'New program...let post '
                postdict[dict_site['url']] = PostObject(dict_site,entry_id_lists)
                postdict[dict_site['url']].login_flag = 1
                postdict[dict_site['url']].start()
                print 'chuan bi vao ct post o view'
        elif btn == 'stop':
            print 'dang stop...o view'
            for dict_site in post_sitedict_list:
                print 'postdict',postdict
                print 'dict_site',dict_site['url']
                print 'luong dang ton tai',postdict[dict_site['url']]
                print 'type of postdict truoc stop ',type(postdict)
                print 'type luong dang ton tai',type (postdict[dict_site['url']])
                try:
                    #if postdict[dict_site['url']].is_alive():
                    postdict[dict_site['url']].stop  = True
                    print 'type of postdict sau stop ',type(postdict)
                    postdict[dict_site['url']].join()
                    print 'type of postdict sau join ',type(postdict)
                    notification = 'luong da stop xong, bat dau chay'
                    print 'luong da stop xong, bat dau chay'
                except Exception as e:
                    print 'luong chua ton tai' ,e
        return render(request, 'drivingtest/notice.html', {'notification':notification})
    except Exception as e:
        print type(e),e
        return render(request, 'drivingtest/notice.html', {'notification':"loi gi do"})
    
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
    #del abcdef
    try:
        notification = thongbao.thongbao
        log = thongbao.thongbao
        '''
        notification = newPostProcess.numer_entry_post + newPostProcess.thongbao
        log = newPostProcess.postlog
        '''
    except Exception as e:
        print e
        notification = thongbao.thongbao
    #notification = 'da xoa'
    return render(request, 'drivingtest/notice.html', {'notification':notification,'log':log})
def stop_post(request):
    #del abcdef
    
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
    #notification =  u'{0}'.format(request.body)
    #notification = 'da xoa'
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
    #html = bbcode.render_html(content)
    notification =  html
    #notification = 'da xoa'
    return render(request, 'drivingtest/load_entry.html', {'notification':notification,'form':entry_form,'entry_id':entry_id})









   
