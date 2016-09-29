 
 function openNav() {
    document.getElementById("mySidenav").style.width = "150px";
    document.getElementById("main-taixiu").style.marginLeft= "150px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main-taixiu").style.marginLeft= "0";
}

function openTopNav() {
    document.getElementById("mySidenav-top").style.height = "250px";
    document.getElementById("main-taixiu").style.marginBottom = "250px";
}

function closeTopNav() {
    document.getElementById("mySidenav-top").style.height = "0";
    document.getElementById("main-taixiu").style.marginBottom= "0";
}


var switchs = false;
function switchfunction_left(){
    switchs = !switchs
    if (switchs) {
        openTopNav() 
    }else {
        closeTopNav()
    }

}

var switchs_left = false;
function switchfunction(){
    switchs_left = !switchs_left
    if (switchs_left) {
        openNav() 
    }else {
        closeNav()
    }

}


$(document).ready(function() {
    var just_poll = true
    var so_lan_quet_poll = 0
    var so_lan_quet_poll_just_poll = 0
    var so_lan_quet_poll_get_data = 0
    var is_poll_previous_complete = true
    $('.cau-for-tooltip').tooltip();
    function form_table_handle(event, intended_for, abitrary_url, sort_field) {
        console.log('e.target',event.target)
        class_value = $(this).attr("class")
        loai_ajax = "normal"
        is_no_show_return_form = false
        closest_wrapper = $(this).closest('div.form-table-wrapper')
        closest_form = $(this).closest('form')
        id_closest_wrapper = closest_wrapper.attr('id')
        is_form = true
        is_table = true
        type = "GET"
        data = {}
        form_table_template = "normal form template" //'form on modal'
        hieu_ung_sau_load_form_va_table = "khong hieu ung"
            // no importaince
        var table_object
        is_get_table_request_get_parameter = false
        is_special_template_for_poll_tai_xiu_repeat = false
            //table_name = '' // table_name dung de xac dinh table , sau khi submit form o modal se hien thi o day, trong truong hop force_allow_edit thi table_name attr se bi xoa 
        if (intended_for == "poll tai xiu") {
            console.log("poll tai xiu")
            console.log("checked",$('input#dont-reload').prop('checked'))
            if ($('input#dont-reload').prop('checked')) {
                console.log('dont reload')
                return false
            }
            is_table = false
            is_form = true
            abitrary_url = '/omckv2/modelmanager/AutoImportForm/new/'
            url = updateURLParameter(abitrary_url, 'which-start-or-stop-btn', "poll")
            is_special_template_for_poll_tai_xiu_repeat = true
            which_start_or_stop_btn = "poll"
            just_poll_local = just_poll
            url = updateURLParameter(url, 'just_poll', just_poll_local)
            is_show_line =  ($('input#show-line').prop('checked'))
            url = updateURLParameter(url, 'is_show_line', is_show_line)
            so_lan_quet_poll += 1
            if (just_poll) {
                so_lan_quet_poll_just_poll += 1
            } else {
                so_lan_quet_poll_get_data += 1
            }
            console.log('so_lan_quet_poll,so_lan_quet_poll_just_poll,so_lan_quet_poll_get_data url', so_lan_quet_poll, so_lan_quet_poll_just_poll, so_lan_quet_poll_get_data, url)
        } else if (intended_for == "poll tai xiu sau khi dat cua") {
            console.log("poll tai xiu sau khi datcua ")
            is_table = false
            is_form = true
            abitrary_url = '/omckv2/modelmanager/AutoImportForm/new/'
            url = updateURLParameter(abitrary_url, 'which-start-or-stop-btn', "poll")
            is_special_template_for_poll_tai_xiu_repeat = true
            which_start_or_stop_btn = "poll"
            just_poll_local = false
            url = updateURLParameter(url, 'just_poll', just_poll_local)
            so_lan_quet_poll += 1
            if (just_poll) {
                so_lan_quet_poll_just_poll += 1
            } else {
                so_lan_quet_poll_get_data += 1
            }
            console.log('so_lan_quet_poll,so_lan_quet_poll_just_poll,so_lan_quet_poll_get_data url', so_lan_quet_poll, so_lan_quet_poll_just_poll, so_lan_quet_poll_get_data, url)
        }
        else if (intended_for == 'intended_for_autocomplete') {
            is_table = true
            is_form = true
            closest_wrapper = $('#form-table-of-tram-info')
            id_closest_wrapper = 'form-table-of-tram-info'
            url = abitrary_url
            type = "GET"
            data = {}
            console.log("$('input#id_khong_search_tu_dong').prop('checked')", $('input#id_khong_search_tu_dong').prop('checked'))
            if ($('input#id_khong_search_tu_dong').prop('checked')) {
                url = updateURLParameter(url, 'search_tu_dong_table_mll', 'no')
            } else {
                url = updateURLParameter(url, 'search_tu_dong_table_mll', 'yes')
            }
            if (name_attr_global != 'object') {
                hieu_ung_sau_load_form_va_table = 'active tram-form-toogle-li'
            }
            console.log('sort_field', sort_field)
            if (sort_field == 'SN1' || sort_field == 'SN2') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-tram toogle'
            } else if (sort_field == '3G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-3g toogle'
            } else if (sort_field == '2G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-2g toogle'
            } else if (sort_field == '4G') {
                hieu_ung_sau_load_form_va_table = 'active thong-tin-4g toogle'
            }

        } else if (intended_for == 'intended_for_manager_autocomplete') {
            is_both_table = "both form and table"
            is_table = true
            is_form = true
            closest_wrapper = wrapper_attr_global
            url = abitrary_url
            type = "GET"
            data = {}


            //@@@@@@@@@@@@@@@
        } else if (class_value.indexOf('input-group-addon') > -1) {
            dtuong_before_submit = $(this)
            console.log('dtuong_before_submit', dtuong_before_submit.attr('class'))
            href_id = $(this).find('span.glyphicon').attr("href_id")
            near_input = $(this).closest('.input-group').find('input[type=text]')
            near_input_value = near_input.val()
            if (typeof href_id === "undefined") {
                if (near_input_value == '') {
                    href_id = "new"
                } else {
                    href_id = near_input_value
                }
            }
            name = modelClassDict[near_input.attr("name")] + 'Form'
            url = "/omckv2/modelmanager/" + name + "/" + href_id + "/"
            is_table = false
            if (href_id == 'new') {
                if (name_attr_global == 'thao_tac_lien_quan') {
                    input_text_to_Name_field = last_add_item
                } else {
                    input_text_to_Name_field = near_input.val()
                }
                hieu_ung_sau_load_form_va_table = 'input text to Name field'
            }
            form_table_template = 'form on modal'
            closest_table_name = closest_wrapper.find('table').attr('name')

            if (closest_table_name && href_id != 'new') {
                $('#modal-on-mll-table').attr('table_name', closest_table_name)
            } else {
                $('#modal-on-mll-table').removeAttr('table_name')
            }

            type = "GET"
            data = {}

        } else if (class_value.indexOf('search-botton') > -1) {
            var query;
            query = $('#text-search-input').val();
            url = "/omckv2/modelmanager/TramForm/new/"
            url = updateURLParameter(url, 'query_main_search_by_button', query)
            is_both_table = 'table only'
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = 'active tram-table-toogle-li'
            if (id_closest_wrapper = 'form-table-of-tram-info_dang_le_ra') {
                closest_wrapper = $('#form-table-of-tram-info')
                id_closest_wrapper = closest_wrapper.attr('id') // no importaince
            }
        } else if (class_value.indexOf('search-manager-botton') > -1) {
            var query;
            wrapper_attr_global = $(e.target).closest('.form-table-wrapper')
            query = wrapper_attr_global.find('#text-search-manager-input').val().split('3G_');
            url = wrapper_attr_global.find('form').attr('action')
            url = updateURLParameter(url, 'query_main_search_by_button', query)
            is_both_table = 'table only'
            type = "GET"
            data = {}
        } else if (class_value.indexOf('searchtable_header_sort') > -1) {
            is_table = true
            is_form = false
            is_both_table = 'table only'
            url = $(this).attr('href')
            if (id_closest_wrapper == 'edit-history-wrapper-div') {
                closest_i_want = $(this).closest('div#form-table-of-tram-info')
                if (closest_i_want.attr('id') != 'form-table-of-tram-info') {
                    closest_i_want = $(this).closest('div#mll-form-table-wrapper')
                    if (closest_i_want.attr('id') != 'mll-form-table-wrapper') {
                        return false
                    } else {
                        url = updateURLParameter(url, 'model_name', 'Mll')
                        tram_id = closest_i_want.find('#id_id').val()
                        console.log('tram_id', tram_id)
                    }
                } else {
                    url = updateURLParameter(url, 'model_name', 'Tram')
                    tram_id = $('#form-table-of-tram-info').find('#id_id').val()
                }
                url = updateURLParameter(url, 'edited_object_id', tram_id)
                url = removeParam('tramid', url)
            }
            type = "GET"
            data = {}
        } else if (class_value.indexOf('edit-entry-btn-on-table') > -1) {
            is_both_table = "form only"
            is_table = false
            is_form = true
            url = closest_wrapper.find('form#model-manager').attr('action')
            entry_id = $(this).attr('id')
            url = url.replace(/\/\w+\/$/g, '/' + entry_id + '/')

            if (id_closest_wrapper == 'form-table-of-tram-info') {
                hieu_ung_sau_load_form_va_table = 'active tram-form-toogle-li'
            } else {
                hieu_ung_sau_load_form_va_table = "edit-entry"

            }
            type = "GET"
            data = {}
        } else if (class_value.indexOf('manager-form-select') > -1) {
            is_table = true
            is_form = true
            url = $(this).val() //url = new va method = get
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box"

        } else if (class_value.indexOf('manager-a-form-select-link') > -1) {
            is_table = true
            is_form = true
            url = $(this).attr('href')
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box 2"

        } else if (class_value.indexOf('show-modal-table-link') > -1) {
            is_form = false
            url = $(this).attr("href")
            form_table_template = 'form on modal'
            type = "GET"
            data = {}
        } else if (class_value.indexOf('show-modal-form-link') > -1) {
            is_table = false
            url = $(this).attr("href") 
            form_table_template = 'form on modal'
            table_name = $(this).closest('table').attr('name')
            console.log('table_name',table_name)
            if (table_name) {
                $('#modal-on-mll-table').attr('table_name', table_name)
            } else {
                console.log('not table_name')
                $('#modal-on-mll-table').removeAttr('table_name')
            }
            type = "GET"
            data = {}
            if (class_value.indexOf('add-comment') > -1 || class_value.indexOf('Nhan-Tin-UngCuu') > -1) {
                mll_id = $(this).closest("tr").find('td.id').html()
                url = updateURLParameter(url, 'selected_instance_mll', mll_id)
            } else if (class_value.indexOf('force_allow_edit') > -1) {
                url = updateURLParameter(url, 'force_allow_edit', 'True')
                $('#modal-on-mll-table').removeAttr('table_name')
            } else if (class_value.indexOf('downloadscript') > -1) {
                is_table = true
                tram_id = $(this).closest('form').find('input[name=id]').val()
                console.log('tram_id', tram_id)
                url = updateURLParameter(url, 'tram_id_for_same_ntp', tram_id)
                hieu_ung_sau_load_form_va_table = 'add class overflow for table'
            }
            if ($(this).hasClass('chon-type-cua')) {

                hieu_ung_sau_load_form_va_table = 'chon-type-cua'
                type_cua_name = $(this).find('span').attr('id')
                console.log('type_cua_name',type_cua_name)
            }
        } else if (class_value.indexOf('cancel-btn') > -1) { //cancle buton duoc nhan.
            is_table = true
            is_form = true
            url = $(this).closest('form').attr("action").replace(/\/\d+\//g, '/new/')
            type = "GET"
            data = {}
        } else if (class_value.indexOf('loc-btn') > -1) {
            is_table = true
            is_form = true
            url = $(this).closest('form').attr("action") + '?loc=true'
            type = "GET"
            data = $(this).closest('form').serialize()
            if (id_closest_wrapper == 'form-table-of-tram-info') {
                hieu_ung_sau_load_form_va_table = 'active tram-table-toogle-li'
            }

            //Nhan nut submit  
        } else if (class_value.indexOf('submit-btn') > -1) { // ca truong hop add and edit
            url = $(this).closest('form').attr("action")
            if ($(this).val() == 'EDIT' || $(this).val() == 'Update to db') {
                var edit_reason_value = ''
                while (edit_reason_value == '') {
                    edit_reason_value = prompt("please give the reason", "");
                }
                if (edit_reason_value == null) {
                    return false
                }
            }
            if (id_closest_wrapper == "manager-modal") {
                form_class_name  =$(this).closest('form').attr('class')
                if(form_class_name=='dat-cua-form') {
                    hieu_ung_sau_load_form_va_table = 'poll tai xiu sau khi dat cua hieu ung'
                }
                console.log('form_class_name',form_class_name)
                table_name = $('#modal-on-mll-table').attr('table_name')
                if (table_name) { // mac du add new commnent hay la edit trang_thai, hay thiet bi thi cung phai is_get_table_request_get_parameter = true
                    is_get_table_request_get_parameter = true
                    table_object = $('table[name=' + table_name + ']').closest('div.table-manager')
                    url = updateURLParameter(url, 'table_name', table_name)
                    is_both_table = "both form and table"
                    is_table = true
                    is_form = true
                    if (url.indexOf('CommentForm') > -1 && $(this).val() == 'ADD NEW') {
                        hieu_ung_sau_load_form_va_table = "change style for add comment to edit comment"
                    }
                } else {
                    console.log('khong co table object, nhugn nut duoc bam van o trong modal')
                    if (class_value.indexOf('edit-ntp') > -1) {
                        is_get_table_request_get_parameter = true
                        is_table = true
                        is_form = true
                        url = removeParam('update_all_same_vlan_sites', url)
                    } else if (class_value.indexOf('update_all_same_vlan_sites') > -1) {
                        url = updateURLParameter(url, 'update_all_same_vlan_sites', 'yes')
                        is_get_table_request_get_parameter = true
                        is_both_table = "both form and table"
                        is_table = true
                        is_form = true

                    } else { // truong hop config ca, hoac la truong hop add new foreinkey
                        is_table = false
                        is_form = true
                        is_get_table_request_get_parameter = false
                        patt = /([^/]*?)Form\/(.*?)\//
                        res = patt.exec(url)
                        form_name = res[1]
                        if (form_name == 'UserProfile') {
                            hieu_ung_sau_load_form_va_table = "update ca truc info"
                        } else if (form_name == 'ThaoTacLienQuan') {
                            near_input = dtuong_before_submit.closest('.input-group').find('input[type=text]')
                            console.log("serach lai", near_input.val())
                            near_input.focus()
                            near_input.autocomplete("search", near_input.val())
                        }

                    }
                }
            } else { // submit trong normal form
                if (id_closest_wrapper == 'profile-loc-ca' || id_closest_wrapper == 'taixiu-wrapper' || id_closest_wrapper == 'import100phienForm-wrapper' ||
                    id_closest_wrapper == 'autoImportForm-wrapper' || id_closest_wrapper == 'soicau-wrapper') {
                    which_start_or_stop_btn = $(this).val()
                    if (which_start_or_stop_btn == "poll") {
                        just_poll_local = false
                    }
                    is_table = false
                    is_form = true
                    url = updateURLParameter(url, 'which-start-or-stop-btn', which_start_or_stop_btn)
                is_show_line =  ($('input#show-line').prop('checked'))
                url = updateURLParameter(url, 'is_show_line', is_show_line)
                } else if (id_closest_wrapper =='select-chart'){
                    is_table = false
                }else {

                    is_form = true

                    if ($(this).val() == 'EDIT') {
                        is_get_table_request_get_parameter = true
                    } else {
                        is_get_table_request_get_parameter = false
                    }
                }
            }

            if (is_get_table_request_get_parameter && is_table) {
                get_parameter_toggle = ''
                var table_contain_div
                if (table_object) {
                    table_contain_div = table_object
                } else {
                    if (id_closest_wrapper == 'form-table-of-tram-info') {
                        table_contain_div = $('#tram-table')
                    } else {
                        table_contain_div = closest_wrapper
                    }
                }
                url = update_parameter_from_table_parameter(table_contain_div, url)
                if (!table_object) {
                    url = removeParam('table_name', url)
                }
            }
            if (edit_reason_value) {
                url = updateURLParameter(url, 'edit_reason', edit_reason_value)
            }
            type = "POST"
            data = $(this).closest('form').serialize()

        } else {
            console.log('not yet handle ')
            return false
        }

        url = updateURLParameter(url, 'form-table-template', form_table_template)
        url = updateURLParameter(url, 'is_form', is_form)
        url = updateURLParameter(url, 'is_table', is_table)
        if (id_closest_wrapper == 'mll-form-table-wrapper' && is_table) {
            loc_cas = $('select[name="loc_ca"]').val()
            if (loc_cas) {
                newpara = loc_cas.join("d4");

            } else {
                newpara = "None"

            }
            url = updateURLParameter(url, 'loc_ca', newpara)
        }
        patt = /Form\/(.*?)\//
        res = patt.exec(url)
        new_or_id = res[1]
        if (is_form && new_or_id != 'new') {
            update_icon_info = true
        } else {
            update_icon_info = false
        }


        $.ajax({
            type: type,
            url: url,
            data: data, // serializes the form's elements.
            success: function(data) {
                if (is_special_template_for_poll_tai_xiu_repeat || (id_closest_wrapper == 'autoImportForm-wrapper' && (which_start_or_stop_btn != "Stop"))) {
                    comback_normal_template_sign = $(data).find('.form-manager_r').length
                    if (comback_normal_template_sign != 1) {
                        form_table_template = "autoImportForm-wrapper-form_table_template"
                        hieu_ung_sau_load_form_va_table = 'openNav_hieu_ung'
                    }
                }

                switch (form_table_template) {
                    case "autoImportForm-wrapper-form_table_template":
                        console.log('url sau khi ajax', url)
                        if (which_start_or_stop_btn == "poll") {
                            if (just_poll_local) {
                                last_phien_in_document = $('#last-phien').html()
                                last_phien_in_data_form = $(data).find('#last-phien-sample').html()
                                last_phien_in_document_int = parseInt(last_phien_in_document)
                                last_phien_in_data_form_int = parseInt(last_phien_in_data_form)
                                if (last_phien_in_document_int == last_phien_in_data_form_int) {
                                    console.log('last_phien_in_document == last_phien_in_data_form --> just_poll van bang True')
                                    just_poll = true
                                    is_poll_previous_complete = true
                                } else {
                                    console.log('last_phien_in_data_form_int', last_phien_in_data_form_int, 'different last_phien_in_document_int', last_phien_in_document_int, 'nen justpoll bang false')
                                    just_poll = false
                                    is_poll_previous_complete = true
                                }
                            } else if (!just_poll_local) {
                                formdata = $(data).find('#main-taixiu').html()
                                obj = $('#main-taixiu')
                                assign_and_fadeoutfadein(obj, formdata)
                                just_poll = true
                                is_poll_previous_complete = true
                                if (!$('input#dont-load-chart').prop('checked')) {
                                load_chart();}
                            }
                            
                        } else {
                            formdata = $(data).find('#main-taixiu').html()
                            obj = $("#main-taixiu")
                            obj.html(formdata)
                            if (!$('input#dont-load-chart').prop('checked')) {
                                load_chart();}
                        }
                        break;
                    case "normal form template":
                        if (is_form & !is_no_show_return_form) {
                            formdata = $(data).find('.form-manager_r').html()
                            if (id_closest_wrapper == 'form-table-of-tram-info') {
                                obj = $('#tram-form')
                            } else {
                                obj = closest_wrapper.children('.form-manager')
                            }
                            form_div_obj = obj.find('.form-div')
                            if (form_div_obj.attr('class')) {
                                form_div_obj.html($(data).find('.form-div').html())
                                notification_form_div_obj = obj.find('.notification-form-div')
                                console.log('dfasdfasdfdsadsfalskdfjlka ldkfj')
                                if(notification_form_div_obj.attr('class')) {
                                    console.log('abcddfa')
                                    notification_form_div_obj.html($(data).find('.notification-form-div').html())
                                }
                            }
                            else{
                            assign_and_fadeoutfadein(obj, formdata)
                            }
                        }
                        if (is_table) { //||table_name la truong hop submit modal form c2hi load lai phai table(gui di yeu cau xu ly form va table, nhung chi muon hien thi table thoi) 
                            tabledata = $(data).find('.table-manager_r').html()
                            if (table_object) {
                                obj = table_object //table_object = table-manager-object
                            } else if (id_closest_wrapper == 'form-table-of-tram-info') {
                                obj = $('#tram-table')
                            } else {
                                obj = closest_wrapper.children('.table-manager')
                            }
                            must_shown_tab_ok = false
                            if (obj.attr('id') == 'tram-table' & hieu_ung_sau_load_form_va_table == 'active tram-table-toogle-li') {
                                console.log('i click it...............')
                                $('.nav-tabs a[href="#tram-table-toogle"]').tab('show')
                                must_shown_tab_ok = true

                            }
                            if (must_shown_tab_ok) {

                                $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').on('shown.bs.tab', function() {
                                    assign_and_fadeoutfadein(obj, tabledata)
                                    $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').unbind('shown.bs.tab');
                                });
                                return false
                            } else {
                                assign_and_fadeoutfadein(obj, tabledata)
                            }


                            if (intended_for == 'intended_for_autocomplete' && !$('input#id_khong_search_tu_dong').prop('checked')) {
                                table2data = $(data).find('.table-manager_r2').html()
                                obj = $('div#mll-form-table-wrapper > div.table-manager')
                                assign_and_fadeoutfadein(obj, table2data)
                            }
                        }
                        break;
                    case 'form on modal': // chi xay ra trong truong hop click vao link show-modal
                        {
                            formdata = $(data).find('.wrapper-modal').html()
                            $("#modal-on-mll-table").html(formdata)
                            $("#modal-on-mll-table").modal()
                        }
                        break;
                }



                if (hieu_ung_sau_load_form_va_table == 'edit-entry') {
                    var navigationFn = {
                        goToSection: function(id) {
                            $('html, body').animate({
                                scrollTop: $(id).offset().top
                            }, 0);
                        }
                    }
                    navigationFn.goToSection('#' + id_closest_wrapper + ' ' + '.form-manager');
                    return false
                } else if (hieu_ung_sau_load_form_va_table == "hide modal") {
                    $("#modal-on-mll-table").modal("hide")
                } else if (hieu_ung_sau_load_form_va_table == 'add class overflow for table') {
                    new_attr = $('#manager-modal').find('.table-manager').attr('class') + ' overflow'
                    $('#manager-modal').find('.table-manager').attr('class', new_attr)
                } else if (hieu_ung_sau_load_form_va_table == "show search box") {
                    $('#manager #search-manager-group').show()
                } else if (hieu_ung_sau_load_form_va_table == "show search box 2") {
                    $('#manager #search-manager-group').show()
                    $("#dropdown-toggle-manager").dropdown("toggle");
                } else if (hieu_ung_sau_load_form_va_table == 'active tram-form-toogle-li') {
                    $('#tram-form-toogle-li a').trigger('click')
                }else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-tram toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-tram"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-3g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-3g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-2g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-2g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-4g toogle') {
                    $('#tram-form-toogle-li a').trigger('click')
                    $('a[href="#thong-tin-4g"]').trigger('click')
                } else if (hieu_ung_sau_load_form_va_table == "update ca truc info") {
                    ca_moi_chon = closest_wrapper.find('select#id_ca_truc option:selected').html()
                    $('span#ca-dang-truc').html('Ca ' + ca_moi_chon)
                } else if (hieu_ung_sau_load_form_va_table == "change style for add comment to edit comment") {
                    dtuong = $('#modal-on-mll-table h4.add-comment-modal-title')
                    dtuong.css("background-color", "#ec971f")
                } else if (hieu_ung_sau_load_form_va_table == 'input text to Name field') {
                    $('div#manager-modal input#id_Name').val(input_text_to_Name_field)
                } else if (hieu_ung_sau_load_form_va_table == 'openNav_hieu_ung'){
                    //openTopNav()
                }else if (hieu_ung_sau_load_form_va_table == 'chon-type-cua') {
                    o_o = $('select#id_tenTable')
                    $('select#id_tenTable').find("option:contains('" + type_cua_name + "')").attr('selected', 'selected');
                }else if (hieu_ung_sau_load_form_va_table == 'poll tai xiu sau khi dat cua hieu ung') {
                    console.log('trong hieu ung',event.target)
                    form_table_handle(event,'poll tai xiu sau khi dat cua')
                }


            },
            error: function(request, status, error) {
                console.log('bi loi 400 hoac 403', error)
                if (error == 'FORBIDDEN') { //400
                    console.log(request.responseText)
                    data = $(request.responseText).find('#info_for_alert_box').html()
                    alert(data);
                } else if (error == 'BAD REQUEST') {
                    console.log('bi loi 403')
                    formdata = $(request.responseText).find('.form-manager_r').html()
                    console.log('formdata', formdata)
                    closest_wrapper.find('.form-manager').html(formdata);

                }

            }

        });
        return false; //ajax thi phai co cai nay. khong thi , gia su click link thi 
    }

    $(this).on('click', '#mll-form-table-wrapper span.input-group-addon,#modal-on-mll-tables span.input-group-addon,a.manager-a-form-select-link,select#id_chon_loai_de_quan_ly,.edit-entry-btn-on-table,form#model-manager input[type=submit],.show-modal-form-link,a.show-modal-table-link,a.show-modal-form-link_allow_edit,a.searchtable_header_sort,.search-botton,.search-manager-botton',
        form_table_handle)




    function abcd(abc) {
        console.log(abc)
        return false
    }
    var refreshIntervalId
    var is_stop_auto_import = false

    var da_nhan_nut_poll = false
    $(this).on('click', '#submit-id-poll-auto-import-phien', function(event) {
        if (da_nhan_nut_poll) {
            alert('da nhan nut poll')
            return false
        }else {
            da_nhan_nut_poll = true
        }

        var interval = 1000 * 3; // where X is your every X giay
        refreshIntervalId = setInterval(function() {
            form_table_handle(event, "poll tai xiu")
        }, interval);
    });

    $(this).on('click', '#submit-id-stop-auto-import-phien', function() {
        clearInterval(refreshIntervalId);
        da_nhan_nut_poll = false
    });



    $('.quest_button').click(function() {
        var catid;
        catid = $(this).attr("idquest");
        id = '#' + 'quest' + catid
        val = $(id).html()
        $('#demo').html(val);


    });

    $('#btn-nxt').click(function() {
        current = (parseInt($('#current_quest').attr("value")) + 1).toString();

        $('#current_quest').attr("value", current);
        id = '#' + 'quest' + current;
        val = $(id).html();
        $('#demo').html(val);
    });

    $('#btn-pre').click(function() {
        current = (parseInt($('#current_quest').attr("value")) - 1).toString();

        $('#current_quest').attr("value", current);
        id = '#' + 'quest' + current;
        val = $(id).html();
        $('#demo').html(val);
    });



    $(this).on('click', "#select-forum input[type=submit]", function() {

        var url = "/select_forum/"; // the script where you handle the form input.
        var val = $("input[type=submit][clicked=true]").attr("value")
        console.log('topic-table', $("#topic-table").serialize())
        var data = $("#myForm").serialize() + '&' + $("#topic-table").serialize() + '&' + 'btn=' + val
        $.ajax({
            type: "POST",
            url: url,
            val: val,
            data: data, // serializes the form's elements.
            success: function(data) {
                $('#thongbao').html(data); // show response from the php script.
            }
        });

        return false; // avoid to execute the actual submit of the form.
    });

    $("#myForm input[type=submit]").click(function() {
        $("input[type=submit]", $(this).parents("#myForm")).removeAttr("clicked");
        $(this).attr("clicked", "true");
    });

    $(".leechform").submit(function() {

        var url = "/leech/"; // the script where you handle the form input.

        $.ajax({
            type: "POST",
            url: url,
            data: $(".leechform").serialize(), // serializes the form's elements.
            success: function(data) {
                $('#thongbao').html(data); // show response from the php script.
            }
        });

        return false; // avoid to execute the actual submit of the form.
    });

    $('#entry').on('submit', '#entryform', function() {



        var url = $(this).attr("action")
        $.ajax({
            type: "POST",
            url: url,
            data: $("#entryform").serialize(), // serializes the form's elements.
            success: function(data) {
                $('#thongbao').html(data); // show response from the php script.
            }
        });

        return false; // avoid to execute the actual submit of the form.
    });




    $('#get-thongbao').click(function() {

        $.get('/get-thongbao/', {
            query: 'a'
        }, function(data) {
            $('#thongbao').html(data);
        });

    });
    $('#importul-btn').click(function() {

        $.get('/importul/', {
            query: 'a'
        }, function(data) {
            $('#thongbao').html(data);
        });

    });
    $('#stop-post').click(function() {

        $.get('/stop-post/', {
            query: 'a'
        }, function(data) {
            $('#thongbao').html(data);
        });

    });




    $('#tao-object').click(function() {

        $.get('/tao_object/', {
            query: 'a'
        }, function(data) {
            $('#thongbao').html(data);
        });

    });

    $('#ulnew-table tr').click(function() {
        //entry_id = $(this).attr("id");
        entry_id = $(this).find('td.id').html()
        console.log('entry_id', entry_id)

        $.get('/get_description/', {
            entry_id: entry_id
        }, function(data) {
            $('#entry').html(data);
        });

    });


    $('.search-botton').click(function(e) {


        var query;
        query = $('#text-search-input').val().split('3G_').join('');
        $.get('/omckv2/tram_table/', {
            query: query
        }, function(data) {
            $('#form-table-of-tram-info .table-manager').html(data);
        });
        $.get('/omckv2/search_history/', function(data) {
            $('#history_search').html(data);
        });

    });


    var counter = 0;
    $(this).on('click', 'table.cm-table > tbody >tr >td.selection>input[type=checkbox] ', function() {
        chosing_row_id = $(this).closest("tr").find('td.id').html()
        console.log('chosing_row_id', chosing_row_id, $(this).is(':checked'))

        if (!$(this).is(':checked')) { /* bo chon 1 row*/
            console.log(chosing_row_id)
            $("table#myTable").find("td.id").filter(function() {
                var id = $(this).html();
                if (id == chosing_row_id) {
                    $(this).parent().remove();
                    var index = choosed_command_array_global.indexOf(id);
                    if (index > -1) {
                        choosed_command_array_global.splice(index, 1);
                    }
                    counter = $('#myTable tr').length - 1;
                    console.log('ban da bo chon 1 row lenh', choosed_command_array_global)
                }
            }) /* close brace for filter function*/

        } /* close if*/
        else {
            counter = counter + 1
            var newrowcopy = "";
            $(this).closest("tr").children().each(function() {
                if (!($(this).hasClass("selection") || $(this).is(':last-child'))) { /*BO CHON NHUNG CAI SELECTION*/
                    var thishtml = $(this).prop('outerHTML')
                    newrowcopy += thishtml
                }
            });
            var newRow = $("<tr>");
            /*newrowcopy = '<td>'+counter + '</td>' +  newrowcopy;*/
            newrowcopy += '<td><input type="button" class="ibtnDel"  value="Delete"></td>';
            newRow.append(newrowcopy);
            if (counter == 1113) alert('het quyen add row')
            $("table#myTable>tbody").append(newRow);
            choosed_command_array_global.push(chosing_row_id)
            console.log(choosed_command_array_global)
        }

    });



    $("table#myTable").on("click", ".ibtnDel", function(event) {

        tr_id = $(this).closest("tr").find('td.id').html()
        $(this).closest("tr").remove();
        $('table.cm-table').find('tr td  input[value =' + tr_id + ']').attr('checked', false)
        counter -= 1
    });




    $(this).on('click', '.generate-command', function() {
        var command_set_many_tram = "";
        $('.tram-table > tbody > tr').each(function() {
            var command_set_one_tram = "";
            var tram_row = $(this)
            $('#myTable > tbody > tr > td.command').each(function() {
                var one_command = $(this).html();
                var reg = /\[(.+?)\]/g;
                var matches_tram_attribute_sets = []
                var found
                while (found = reg.exec(one_command)) {
                    console.log('found.index', found.index, 'found', found, '\nreg.lastIndex', reg.lastIndex)
                    matches_tram_attribute_sets.push(found[1]);
                    reg.lastIndex = found.index + 1;
                }
                $.each(matches_tram_attribute_sets, function(index, tram_attribute) {
                    value = tram_row.find('td.' + tram_attribute.split(" ").join("_")).html()
                    value = value.replace(/^ERI_3G_/g, '')
                    one_command = one_command.replace('[' + tram_attribute + ']', value)
                });
                command_set_one_tram += one_command + '\n'
            });

            command_set_many_tram += command_set_one_tram + '\n\n'
        });

        $('textarea.command-erea').val(command_set_many_tram);
        console.log(command_set_many_tram)
    });

    var id;
    $(this).on('click', 'ul.dropdown-menu > li.delete ', function() {
        id = $(this).closest("tr").find('td.id').html();

        bootbox.confirm("Are you sure?", function(result) {
            if (result == true) {
                $.get('/omckv2/delete_mll/', {
                    query: id
                }, function(data) {
                    $('#danh-sach-mll').html(data);
                });
            };
        }); //confirm box and function

        return false
    }); //on and function



    $(this).on('click', '.link_to_download_scipt', function() {
        console.log('button ok')
        var data = $(this).closest('form').serialize()
        site_id = $('#form-table-of-tram-info').find('input#id_id').val()
        var win = window.open('/omckv2/download_script_ntp/' + '?site_id=' + site_id + '&' + data);
        if (win) {
            //Browser has allowed it to be opened
            $("#config_ca_modal").modal("hide");
            win.focus();
        } else {
            //Broswer has blocked it
            alert('Please allow popups for this site');
        }

        return false

    })



    function copy_row(this_obj) {
        tableHtml = $(this_obj).closest("table").prop('outerHTML')
        var rownum = $(this_obj).closest("tr").prevAll("tr").length + 1
        doituong = $(tableHtml)
        doituong.find('tbody > tr').not(':nth-child(' + rownum + ')').remove()
            //$('th:lt(10):gt(5),th:last-child', doituong).remove()
            //$('td:lt(10):gt(5),td:last-child', doituong).remove()

        $('th:lt(15):gt(5)', doituong).remove()
        $('td:lt(15):gt(5)', doituong).remove()

        $('a', doituong).contents().unwrap();
        doituong.attr("class", "table table-bordered")
        doituong.find('th').each(function() {
            $(this).attr("class", "")
        })
        content = doituong.prop('outerHTML')
        $("#modal-on-mll-table").find('div.table-div').html(content)
    }

    function gup(name, url) {
        if (!url) url = location.href;
        name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
        var regexS = "[\\?&]" + name + "=([^&#]*)";
        var regex = new RegExp(regexS);
        var results = regex.exec(url);
        return results == null ? null : results[1];
    }

    function updateURLParameter(url, param, paramVal) {
        var newAdditionalURL = "";
        var tempArray = url.split("?");
        var baseURL = tempArray[0];
        var additionalURL = tempArray[1];
        var temp = "";
        if (additionalURL) {
            tempArray = additionalURL.split("&");
            for (i = 0; i < tempArray.length; i++) {
                if (tempArray[i].split('=')[0] != param) {
                    newAdditionalURL += temp + tempArray[i];
                    temp = "&";
                }
            }
        }

        var rows_txt = temp + "" + param + "=" + paramVal;
        return baseURL + "?" + newAdditionalURL + rows_txt;
    }

    function toggleDesAsc(additionalURL) {
        var newAdditionalURL = "";
        tempArray = additionalURL.split("&");
        for (i = 0; i < tempArray.length; i++) {
            key = tempArray[i].split('=')[0]

            if (key != 'sort') {
                newAdditionalURL += "&" + tempArray[i];
            } else {
                paraValue = tempArray[i].split('=')[1]
                if (paraValue.indexOf('-') > -1) {
                    console.log('paraValue co - la', paraValue)
                    paraValue = paraValue.replace('-', '')
                } else {
                    paraValue = '-' + paraValue
                }
                newAdditionalURL += "&" + key + '=' + paraValue;
            }
        }
        return newAdditionalURL
    }




    

    $(this).on("click", ".btnEdit", function() {
        var array_td_need_edit = [] //array la chua nhung index cua td can edit
        var par = $(this).parent().parent();
        wrapper_table = $(this).closest('table')
        table_class = wrapper_table.attr("class") //tr
        if (table_class.indexOf('history-table') > -1) {
            array_td_need_edit = [2, 3, 4]
        } else if (table_class.indexOf('doi_tac-table') > -1) {
            array_td_need_edit = [1, 2, 3, 4, 5, 6]
        }
        this_row = par.children('td')
        var total = this_row.length;
        this_row.each(function(i, v) {
            this_html = $(this).text()
            this_html = ((this_html == "—") ? "" : this_html)
            if (array_td_need_edit.indexOf(i) > -1) {
                $(this).html("<input type='text' id='" + $(this).attr("class") + "' value='" + this_html + "'/>");
            } else if (i == total - 1) {
                $(this).html("<img src='media/images/disk.png' class='btnSave'/>");
            }
        })

    });
    $(this).on("click", ".btnSave", function() {
        wrapper_table = $(this).closest('table')
        table_class = wrapper_table.attr("class")
        table_div = $(this).closest('div.table-div')
        url = wrapper_table.attr("table-action")
        var trow = $(this).parent().parent(); //tr
        history_search_id = trow.find('td.id').html()
        var row = {
            action: "edit"
        };
        row.history_search_id = history_search_id
        trow.find('input,select,textarea').each(function() {
            row[$(this).attr('id')] = $(this).val();
        });
        if (table_class.indexOf('history-table') > 0) {
            //url = '/omckv2/edit_history_search/',
            $.get(url, row, function(data) {
                $('#history_search').html(data);
            });
        } else if (table_class.indexOf('doi_tac-table') > 0) {

            $.get(url, row, function(data) {
                console.log(data);

                $('#table-doitac').html(data);
            });
        }

    });

    $(this).on("click", ".btnDelete", function() {

        wrapper_table = $(this).closest('table')
        table_class = wrapper_table.attr("class")
        url = wrapper_table.attr("table-action")
        var trow = $(this).parent().parent(); //tr
        history_search_id = trow.find('td.id').html()

        if (table_class.indexOf('history-table')) {
            $("#myModal").find('div#id-deleted-object').html("Doi tuong xoa co id " + history_search_id)
                //$("#myModal").modal();
            if (confirm("Are you sure?")) {
                $.get(url, {
                        "action": "delete",
                        "history_search_id": history_search_id
                    },
                    function(data) {
                        $('#history_search').html(data);
                    });

                return false; //url = '/omckv2/edit_history_search/',
            }
        }

    });
    $(this).on('click', '.addrow', function() {
        a = $(this).parent()
        tbody = a.find('tbody')
        firstrow = tbody.find('tr:first')
        total = firstrow.find('td').length
        console.log('tbody', a)
        array_td_need_edit = [1, 2, 3, 4, 5, 6]
        row = $('<tr><td class="id">')

        firstrow.find('td').each(function(i, v) {
            if (array_td_need_edit.indexOf(i) > -1) {
                row.append("<td><input type='text' id='" + $(this).attr("class") + "'/></td>");
            }
        })

        row.append("<img src='media/images/disk.png' class='btnSave'/>");
        firstrow.before(row);
        //$(row).prependTo(tbody);

    })


    $('.datetimepicker').datetimepicker({
        format: DT_FORMAT,
    });

    $(this).on('click', ".autocomplete,.autocomplete_search_tram,.autocomplete_search_manager", function() {
        value = $(this).val()
        if (value.length === 0) {
            value = 'tatca'
            if ($(this).hasClass('autocomplete')){
               
            }
        }
        $(this).autocomplete("search", value)

    });
    $(this).on("focus", ".autocomplete", function() {
        $(this).autocomplete({
                create: function() {

                    $(this).data('ui-autocomplete')._renderItem = function(ul, item) {
                        return $(' <li class="abc" ' + 'thietbi="' + item.label + '">')
                            .append("<a>" + '<b>' + item.label + '</b>' + "<br>" + '<span class="std">' + item.desc + '</span>' + "</a>")
                            .appendTo(ul);
                    }
                },
                search: function(e, ui) {
                    name_attr_global = $(e.target).attr("name")

                },
                source: function(request, response) {
                    console.log('name_attr_global', name_attr_global)
                    var query = request.term
                    $.get('/omckv2/autocomplete/', {
                        query: query,
                        name_attr: name_attr_global
                    }, function(data) {
                        response(data['key_for_list_of_item_dict'])

                    })
                },
                select: function(event, ui) {
                    this.value = ui.item['label'];
                    return false
                }

            }) //close autocompltete


    });



    $(this).on("focus", ".autocomplete_search_tram", function() {
        $(this).autocomplete({
                create: function() {
                    $(this).data('ui-autocomplete')._renderItem = function(ul, item) {

                        return $('<li>').append(
                                $('<a>').append('<b>' + '<span class="greencolor">' + item.sort_field + "-</span>" + item.label + '</b>')
                                .append("<br>" + '<span class="std">' + item.desc + '</span>' +
                                    "<br>" + '<span class="std">' + item.desc2 + '</span>'))
                            .appendTo(ul)

                    }
                },
                focus: function(event, ui) {

                    event.preventDefault(); // Prevent the default focus behavior.
                    return false;

                },
                search: function(e, ui) {
                    name_attr_global = $(e.target).attr("name") //name_attr_global de phan biet cai search o top of page or at mllfilter
                    console.log('name_attr_global', name_attr_global)

                },
                source: function(request, response) {

                    console.log('name_attr_global', name_attr_global)
                    var query = extractLast(request.term)
                    $.get('/omckv2/autocomplete/', {
                        query: query,
                        name_attr: name_attr_global
                    }, function(data) {
                        response(data['key_for_list_of_item_dict'])
                            //response(projects)
                    })
                },
                select: function(event, ui) {
                    if (name_attr_global == "subject") {
                        var terms = split(this.value);
                        // remove the current input
                        terms.pop();
                        // add the selected item
                        terms.push(ui.item.value);
                        // add placeholder to get the comma-and-space at the end
                        terms.push("");
                        this.value = terms.join(", ");
                    } else {
                        this.value = ui.item['label']; //this.value tuc la gia tri hien thi trong input text
                    }
                    if (name_attr_global == "subject") {
                        $('#id_site_name').val(ui.item.site_name_1)
                            //http://stackoverflow.com/questions/314636/how-do-you-select-a-particular-option-in-a-select-element-in-jquery
                        string_to_item = 'select option:contains("' + ui.item.thiet_bi + '") '
                        $('#div_id_thiet_bi').find(string_to_item).attr('selected', 'selected')
                    }

                    form_table_handle('intended_for_autocomplete', '/omckv2/modelmanager/Table3gForm/' + ui.item.id + '/?table3gid=' + ui.item.id)

                    return false // return thuoc ve select :
                }

            }) //close autocompltete
    });

    $(this).on('submit', 'form#detail_tram', function() {
        var val = $('.thong-tin-tram').attr('site_id')
        var data = $(this).serialize() + '&' + 'site_id=' + val
        var url = $(this).attr('action') ///omckv2/edit_site/
        $.ajax({
            type: "POST",
            url: url,
            val: val,
            data: data, // serializes the form's elements.
            success: function(data) {
                $('.thong-tin-tram').fadeOut(300);
                $('.thong-tin-tram').html(data).fadeIn(300);
                //$('.thong-tin-tram').find('form').attr('site_id',val)
            }
        });

        return false;
    });

    function split(val) {
        return val.split(/,\s*/);
    }

    function extractLast(term) {
        return split(term).pop();
    }

    $(".autocomplete_search_tram1")
        // don't navigate away from the field on tab when selecting an item
        .bind("keydown", function(event) {
            if (event.keyCode === $.ui.keyCode.TAB &&
                $(this).autocomplete("instance").menu.active) {
                event.preventDefault();
            }
        })
        .autocomplete({
            minLength: 0,
            search: function(e, ui) {
                name_attr_global = $(e.target).attr("name") //name_attr_global de phan biet cai search o top of page or at mllfilter
                console.log('name_attr_global', name_attr_global)
                    //console.log("ui in search", ui)
                    //console.log(e.target)
            },
            source: function(request, response) {

                console.log('name_attr_global', name_attr_global)
                var query = extractLast(request.term)
                $.get('/omckv2/autocomplete/', {
                    query: query,
                    name_attr: name_attr_global
                }, function(data) {
                    response(data['key_for_list_of_item_dict'])
                        //response(projects)
                })
            },
            focus: function() {
                // prevent value inserted on focus
                return false;
            },
            select: function(event, ui) {
                var terms = split(this.value);
                // remove the current input
                terms.pop();
                // add the selected item
                terms.push(ui.item.value);
                // add placeholder to get the comma-and-space at the end
                terms.push("");
                this.value = terms.join(", ");
                return false;
            }
        });
    //consume_alert();
    
    $('.selectmultiple').select2({
        width: '100%'
    });
 
        //$(".tablemll").colResizable();

    $('.mySelect2').select2({
        width: '80%'
    });

$('#showmenu').click(function() {
                $('.menu').slideToggle("fast");
        });

}); //END READY DOCUMENT




$(document).on('click', "input[type=submit]", function() {
    $("input[type=submit]").removeAttr("clicked");
    $(this).attr("clicked", "true");
});
//var $loading = $('#loadingDiv').hide();
$(document).ajaxComplete(function(event, xhr, settings) {

    $('.datetimepicker-comment').datetimepicker({
        format: DT_FORMAT
    });
    /*
        $('.comboboxd4').combobox()
            
                $('.comboboxd4').select2({
      placeholder: "Select a state",
      allowClear: true
    });
    */
    $('.datetimepicker').datetimepicker({
        format: DT_FORMAT,
    });

    $('.datetimepicker').datetimepicker({
        format: DT_FORMAT,
    });
    $('#id_thao_tac_lien_quan,.mySelect2').select2({
        width: '100%'
    });
    $('.selectmultiple').select2({
        width: '100%'
    })

});

var ajax_is_complete
$(document).on("ajaxStart", function() {
    ajax_is_complete = false
    $("#loading").show();
}).on("ajaxComplete", function() {
    $("#loading").hide();
    ajax_is_complete = true
});

$("#loading").hide();

var choosed_command_array_global = []
$('#submit-id-command-cancel').hide()

var name_attr_global
var DT_FORMAT = 'HH:mm DD/MM/YYYY'
   



// D4 fadeIn fadeOut
function d4fadeOutFadeIn(jqueryobject, datahtml) {

    jqueryobject.fadeOut(300);
    jqueryobject.html(datahtml).fadeIn(300);
    jqueryobject.attr('site_id', ui.item.value)
};

function assign_and_fadeoutfadein(jqueryobject, datahtml) {
    if (datahtml) {

        jqueryobject.fadeOut(100);
        jqueryobject.html(datahtml).fadeIn(100);
    }
};

/*
window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
        animationEnabled: true,
        title:{
            text: "Multi Series Spline Chart - Hide / Unhide via Legend"
        },
        data: [
        {
            type: "spline", //change type to bar, line, area, pie, etc
            showInLegend: true,        
            dataPoints: [
                { x: 10, y: 51 },
                { x: 20, y: 45},
                { x: 30, y: 50 },
                { x: 40, y: 62 },
                { x: 50, y: 95 },
                { x: 60, y: 66 },
                { x: 70, y: 24 },
                { x: 80, y: 32 },
                { x: 90, y: 16}
            ]
            },
            {
            type: "spline", //change type to bar, line, area, pie, etc
            showInLegend: true,        
            dataPoints: [
                { x: 10, y: 510 },
                { x: 20, y: 450},
                { x: 30, y: 500 },
                { x: 40, y: 620 },
                { x: 50, y: 950 },
                { x: 60, y: 660 },
                { x: 70, y: 240 },
                { x: 80, y: 320 },
                { x: 90, y: 160}
            ]
            },
            {
            type: "spline",
            showInLegend: true,        
            dataPoints: [
                { x: 10, y: 21 },
                { x: 20, y: 44},
                { x: 30, y: 35 },
                { x: 40, y: 45 },
                { x: 50, y: 75 },
                { x: 60, y: 58 },
                { x: 70, y: 18 },
                { x: 80, y: 30 },
                { x: 90, y: 11}
            ]
            }
        ],
        legend: {
            cursor: "pointer",
            itemclick: function (e) {
                if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                    e.dataSeries.visible = false;
                } else {
                    e.dataSeries.visible = true;
            }
            chart.render();
            }
        }
    });

    chart.render();
}
*/
//series_from_div = JSON.parse($("#json > #series").attr('data').replace(/'/g,'"'))
function create_highcharts_object(series,repeat_tai_or_xiu,sample) {
    highcharts_object = {
        chart: {
                zoomType: 'xy'
            },
        title: {
            text: 'SPACE AGGREGATE' + repeat_tai_or_xiu,
            x: -20 //center
        },
        subtitle: {
            text: 'Source: WorldClimate.com',
            x: -20
        },
        xAxis: {
            categories: categories[sample]
        },
        yAxis: {
            title: {
                text: 'Số lần xuất hiện của repeat (lần)'
            },
            plotLines: [{
                value: 0,
                width: 10,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: 'Lần'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
        series: series,
    }


    return highcharts_object
}

/*
function load_chart(){
    DTUONG_ARRAY = ['repeat-tai','repeat-xiu','xenke-tai','xenke-xiu','tai_xiu_ttxx']
    Samples = [100,512]
    for (i=0;i<DTUONG_ARRAY.length;i++ ){
        for (j=0;j<Samples.length;j++){
        sample = Samples[j]
        type_name = DTUONG_ARRAY[i]
        class_name = '.container-'+ type_name
        sample_for_find = 'div[simple='+ sample.toString()+']'
        chart_container_div_obj = $(class_name).filter('div[sample='+sample.toString()+']'
            )
        one_type_series = series[type_name][sample]
        hc_data= create_highcharts_object(one_type_series,' ' + type_name + '-' + sample.toString(),sample )
        chart_container_div_obj.highcharts(hc_data);
        }
    }
}
*/

function load_chart(){
    DTUONG_ARRAY = ['repeat-tai','repeat-xiu','xenke-tai','xenke-xiu','tai_xiu_ttxx']
    Samples = [25,50,100,200,512]
    for (i=0;i<DTUONG_ARRAY.length;i++ ){
        for (j=0;j<Samples.length;j++){
        sample = Samples[j]
        type_name = DTUONG_ARRAY[i]
        parent = $('#chart-for-margin-top')
        new_obj_id= 'container-' + type_name + '-' + sample.toString()
        new_div = document.createElement("div");
        new_div = $(new_div).attr('id',new_obj_id).attr('style','min-width: 310px; height: 400px; margin: 0 auto')
        parent.append(new_div)
        chart_container_div_obj = new_div
            
        one_type_series = series[type_name][sample]
        hc_data= create_highcharts_object(one_type_series,' ' + type_name + '-' + sample.toString(),sample )
        chart_container_div_obj.highcharts(hc_data);
        }
    }
}
//load_chart();