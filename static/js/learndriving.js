$(document).ready(function() {

    var just_poll = true

    function form_table_handle(e, intended_for, abitrary_url, sort_field) {
        console.log("okkkkkkkkkkkkkkkkk first form_table_handle")

        class_value = $(this).attr("class")
        loai_ajax = "normal"
        is_no_show_return_form = false
            //is_both_table = "both form and table"
        //is_table_not
        closest_wrapper = $(this).closest('div.form-table-wrapper')
        closest_form = $(this).closest('form')
        id_closest_wrapper = closest_wrapper.attr('id')
        /*
        try { 
        class_closest_form = closest_form.attr('class')
        if (class_closest_form.indexOf('is_table_not')>-1){
            is_table = false}
        else{
            is_table = true }
        }
        catch {
            
        }
        */
        is_form = true
        is_table = true 
        type = "GET"
        data = {}
        form_table_template = "normal form template" //'form on modal'
        hieu_ung_sau_load_form_va_table = "khong hieu ung"
        // no importaince
        console.log('id_closest_wrapper', id_closest_wrapper)
        var table_object
        is_get_table_request_get_parameter = false
        is_special_template = false
            //table_name = '' // table_name dung de xac dinh table , sau khi submit form o modal se hien thi o day, trong truong hop force_allow_edit thi table_name attr se bi xoa 
        if (intended_for == "poll tai xiu") {
            console.log("poll tai xiu")
            is_table = false
            is_form = true
            abitrary_url = '/omckv2/modelmanager/AutoImportForm/new/'
            url = updateURLParameter(abitrary_url, 'which-start-or-stop-btn', "poll")
            is_special_template = true
            which_start_or_stop_btn = "poll"
            just_poll_local = just_poll
            url = updateURLParameter(url, 'just_poll', just_poll_local)


        } else if (intended_for == 'intended_for_autocomplete') {
            //is_both_table = "both form and table"
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
            //query = $(this).closest('.search-w').find('input[type="text"]:eq(1)').val().split('3G_');
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
                console.log('$(this)', $(this).attr('class'))
                closest_i_want = $(this).closest('div#form-table-of-tram-info')
                console.log('closest_i_want', closest_i_want)
                console.log('0closest_i_want', closest_i_want.attr('id'))
                if (closest_i_want.attr('id') != 'form-table-of-tram-info') {
                    closest_i_want = $(this).closest('div#mll-form-table-wrapper')
                    console.log('2closest_i_want', closest_i_want)
                    if (closest_i_want.attr('id') != 'mll-form-table-wrapper') {
                        return false
                    } else {
                        console.log('3closest_i_want', closest_i_want.attr('id'))
                        url = updateURLParameter(url, 'model_name', 'Mll')
                        tram_id = closest_i_want.find('#id_id').val()
                        console.log('tram_id', tram_id)
                    }
                } else {
                    url = updateURLParameter(url, 'model_name', 'Tram')
                    tram_id = $('#form-table-of-tram-info').find('#id_id').val()
                    console.log('tram_id', tram_id)
                }
                url = updateURLParameter(url, 'edited_object_id', tram_id)
                url = removeParam('tramid', url)
                    //url = url.replace(/&?tramid=([^&]$|[^&]*?&)/i, "")
                console.log('###########url new', url)
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
            console.log('url', url)

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
                //url = $('#id_chon_loai_de_quan_ly option:selected').val()
            url = $(this).val() //url = new va method = get
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box"


        } else if (class_value.indexOf('manager-a-form-select-link') > -1) {
            is_table = true
            is_form = true
            url = $(this).attr('href')
            console.log('@@@@@@@@@@ndt', url)
            type = "GET"
            data = {}
            hieu_ung_sau_load_form_va_table = "show search box 2"


        } else if (class_value.indexOf('show-modal-table-link') > -1) {
            is_form = false
            url = $(this).attr("href") ///omckv2/show-modal-form-link/ThietBiForm/1/
            form_table_template = 'form on modal'
            console.log('@@@@@@@@@@ndt', url)
            type = "GET"
            data = {}


        } else if (class_value.indexOf('show-modal-form-link') > -1) {
            is_table = false
            url = $(this).attr("href") ///omckv2/show-modal-form-link/ThietBiForm/1/
            form_table_template = 'form on modal'
            table_name = $(this).closest('table').attr('name')
            if (table_name) {
                $('#modal-on-mll-table').attr('table_name', table_name)
            } else {
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
                console.log('!@#$!@#$1')
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
                console.log('sdsdsdsdsdsds')
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
                            //dtuong_before_submit.attr
                            //near_input = dtuong_before_submit.closest('.input-group').find('input[type=text]')
                            near_input = dtuong_before_submit.closest('.input-group').find('input[type=text]')
                            console.log("serach lai", near_input.val())
                                //near_input.trigger('focus')
                            near_input.focus()
                            near_input.autocomplete("search", near_input.val())
                                //near_input = $('#mll-form-table-wrapper #id_thao_tac_lien_quan')

                            //near_input.val('dfasdfdfdfd')
                        }

                    }
                }


            } else { // submit trong normal form



                if (id_closest_wrapper == 'profile-loc-ca' || id_closest_wrapper == 'taixiu-wrapper' || id_closest_wrapper == 'import100phienForm-wrapper' ||
                    id_closest_wrapper == 'autoImportForm-wrapper'||id_closest_wrapper == 'soicau-wrapper') {
                    which_start_or_stop_btn = $(this).val()
                    if (which_start_or_stop_btn == "poll") {
                        console.log('giai thoat thoi')
                        return false;
                    }
                    is_table = false
                    is_form = true
                    url = updateURLParameter(url, 'which-start-or-stop-btn', which_start_or_stop_btn)

                } else {
                    
                    is_form = true

                    if ($(this).val() == 'EDIT') {
                        is_get_table_request_get_parameter = true
                    } else {
                        is_get_table_request_get_parameter = false
                    }
                }
            }


            //get context cua table 
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
                //console.log('table_contain_div', table_contain_div.attr('class'))

                url = update_parameter_from_table_parameter(table_contain_div, url)




                if (!table_object) {
                    url = removeParam('table_name', url)
                        //url = url.replace(/&?table_name=([^&]$|[^&]*)/i, "")
                    console.log('url new', url)

                    //url2 = url.replace(/&khong_show_2_nut_cancel_va_loc=([^&]$|[^&]*)/i, "")
                    //console.log('url 2',url2)
                }

            }

            if (edit_reason_value) {
                url = updateURLParameter(url, 'edit_reason', edit_reason_value)
            }

            console.log('##after add edit_reason', url)
            type = "POST"

            data = $(this).closest('form').serialize()

        } else {
            console.log('not yet handle ')
            return false
        }

        url = updateURLParameter(url, 'form-table-template', form_table_template)
        url = updateURLParameter(url, 'is_form', is_form)
        url = updateURLParameter(url, 'is_table', is_table)
            //url = updateURLParameter(url, 'which-form-or-table', is_both_table)
        if (id_closest_wrapper == 'mll-form-table-wrapper' && is_table) {
            loc_cas = $('select[name="loc_ca"]').val()
            console.log('aaaaaaaaaaaaaaaaaaaaaaaaa', loc_cas)
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
                if (is_special_template || id_closest_wrapper == 'autoImportForm-wrapper' && (which_start_or_stop_btn != "Stop")) {

                    comback_normal_template = $(data).find('.form-manager_r').length
                    if (comback_normal_template != 1) {
                        form_table_template = "autoImportForm-wrapper-form_table_template"
                    }
                    //show_map_from_longlat()
                }

                switch (form_table_template) {

                    case "autoImportForm-wrapper-form_table_template":
                        if (which_start_or_stop_btn == "poll") {
                            console.log('url', url)
                            if (just_poll_local) {
                                last_phien_hien_tai = $('#last-phien').html()
                                
                                
                                console.log('type of last_phien_hien_tai document',typeof(last_phien_hien_tai))
                                console.log('last_phien_hien_tai', last_phien_hien_tai)
                                //console.log('data', data)
                                last_phien_in_data_form = $(data).find('div#last-phien-sample')
                                console.log('type of last_phien_in_data_form',typeof(last_phien_in_data_form))
                                if (last_phien_in_data_form!=last_phien_in_data_form){
                                    console.log('why 2 cai nay khong bang nhau',last_phien_hien_tai,last_phien_in_data_form)

                                }
                                last_phien_hien_tai = parseInt(last_phien_hien_tai)
                                last_phien_in_data_form = parseInt(last_phien_in_data_form.html())
                                console.log('last_phien_in_data_form', last_phien_in_data_form)
                                console.log('neu toi day thi khogn co return')
                                if (last_phien_in_data_form == last_phien_hien_tai) {
                                }
                                else {  console.log('do data formv', last_phien_in_data_form,'different', last_phien_hien_tai, 'nen justpoll bang false')
                                    just_poll = false
                                }
                            } else if (!just_poll_local ) {
                                just_poll = true
                                formdata = $(data).find('#special-for-auto-import').html()
                                obj = $("#special-for-auto-import")
                                assign_and_fadeoutfadein(obj, formdata)
                                data_receive_poll = true
                            }

                        } else {
                            formdata = $(data).find('#special-for-auto-import').html()
                            obj = $("#special-for-auto-import")
                            obj.html(formdata)
                                //assign_and_fadeoutfadein(obj, formdata)
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

                            assign_and_fadeoutfadein(obj, formdata)
                                //show_map_from_longlat()
                        }

                        if (is_table) { //||table_name la truong hop submit modal form chi load lai phai table(gui di yeu cau xu ly form va table, nhung chi muon hien thi table thoi) 
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
                                    //$('#tram-table-toogle-li a').trigger('click')
                                $('.nav-tabs a[href="#tram-table-toogle"]').tab('show')
                                must_shown_tab_ok = true

                            }
                            if (must_shown_tab_ok) {

                                $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').on('shown.bs.tab', function() {
                                    assign_and_fadeoutfadein(obj, tabledata)
                                    scrolify(obj.find('table.table-bordered'), 580); // 160 is height 
                                    $('#tram-manager-lenh-nav-tab-wrapper-div .nav-tabs a').unbind('shown.bs.tab');
                                });

                                return false
                            } else {
                                assign_and_fadeoutfadein(obj, tabledata)
                                scrolify(obj.find('table.table-bordered'), 580); // 160 is height   
                            }


                            if (intended_for == 'intended_for_autocomplete' && !$('input#id_khong_search_tu_dong').prop('checked')) {
                                table2data = $(data).find('.table-manager_r2').html()
                                obj = $('div#mll-form-table-wrapper > div.table-manager')
                                assign_and_fadeoutfadein(obj, table2data)
                                scrolify(obj.find('table.table-bordered'), 580); // 160 is height    

                            }


                        }


                        break;
                    case 'form on modal': // chi xay ra trong truong hop click vao link show-modal
                        console.log('vao form on modal okkkkkkkkkkkk')

                        {
                            console.log('ndt data',data)
                            formdata = $(data).find('.wrapper-modal').html()
                            console.log('ndt formdata',formdata)
                            //formdata = update_icon_info_function(update_icon_info, formdata)
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
                    console.log('!@#$!@#$2')
                    new_attr = $('#manager-modal').find('.table-manager').attr('class') + ' overflow'
                    $('#manager-modal').find('.table-manager').attr('class', new_attr)
                } else if (hieu_ung_sau_load_form_va_table == "show search box") {
                    $('#manager #search-manager-group').show()
                } else if (hieu_ung_sau_load_form_va_table == "show search box 2") {
                    $('#manager #search-manager-group').show()
                    $("#dropdown-toggle-manager").dropdown("toggle");
                } else if (hieu_ung_sau_load_form_va_table == 'active tram-form-toogle-li') {

                    $('#tram-form-toogle-li a').trigger('click')

                }
                /*else if (hieu_ung_sau_load_form_va_table == 'active tram-table-toogle-li') {

                                   $('#tram-table-toogle-li a').trigger('click')
                               } */
                else if (hieu_ung_sau_load_form_va_table == 'active thong-tin-tram toogle') {
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
                    console.log('@@@@ca_moi_chon', ca_moi_chon)
                    $('span#ca-dang-truc').html('Ca ' + ca_moi_chon)
                } else if (hieu_ung_sau_load_form_va_table == "change style for add comment to edit comment") {
                    dtuong = $('#modal-on-mll-table h4.add-comment-modal-title')
                    console.log('@@@@@@@@@@@', dtuong.attr('class'))
                    dtuong.css("background-color", "#ec971f")
                        //dtuong.attr('style',"background-color:#ec971f")
                } else if (hieu_ung_sau_load_form_va_table == 'input text to Name field') {
                    $('div#manager-modal input#id_Name').val(input_text_to_Name_field)

                    //console.log('odfadsfasdfds',$(this).closest('.input-group').find('input[type=text]').val())

                }


            },
            error: function(request, status, error) {
                console.log('bi loi 400 hoac 403', error)
                if (error == 'Forbidden') { //403
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


    $(this).on('click', '#submit-id-poll-auto-import-phien-btn', function(event) {
        console.log('just_poll',just_poll)
        var interval = 1000 * 10; // where X is your every X giay
        refreshIntervalId = setInterval(function() {
            form_table_handle(event, "poll tai xiu")
        }, interval);
    });

    $(this).on('click', '#submit-id-stop-auto-import-phien', function() {
        clearInterval(refreshIntervalId);
    });

    /*
    $(this).on('click', '#submit-id-poll-auto-import-phien-btn',function(event) {

    while(1) {
    var delay=10000; //1 second
    setTimeout(abcd('abc'), delay)
    }

    })
    */




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




    /*
    $(this).on("submit", "#amll-form", function() {
        var clicked_button = $("input[type=submit][clicked=true]").attr("value");
        if (clicked_button == "Filter") {
            console.log(' trong ham Filter')
            var url = "/omckv2/mll_filter/"; // the script where you handle the form input.
            var type = 'GET';
        } else {
            var url = "/omckv2/luu_mll_form/"; // the script where you handle the form input.
            var type = 'POST'
        }
        var data = $(this).serialize()
        if (clicked_button == "Cancle") {
            data = {}
            type = 'GET'
        }
        url = url + '?which-button=' + clicked_button
        $.ajax({
            type: type,
            url: url,
            data: data, // serializes the form's elements.
            error: function(request, status, error) {
                if (error == 'FORBIDDEN') { //403
                    alert('ban ko co quyen tao mll, chi co truc ca moi duoc,', request.responseText)
                } else if (error == 'BAD REQUEST') {
                    $('.filter-mll-div').html(request.responseText);
                } else {
                    new PNotify({
                        title: 'Oh No!',
                        text: request.responseText,
                        type: 'error'
                    });
                }
            },
            success: function(data) {
                //     
                formhtml = $(data).find('div#form-area').html()
                $('.filter-mll-div').html(formhtml); // show response from the php script.
                tabelhtml = $(data).find('div#table-area').html()
                $('#danh-sach-mll').html(tabelhtml);
                assign_and_fadeoutfadein($('#danh-sach-mll'), tabelhtml)

            }

        }); //ajax curly close
        return false; // avoid to execute the actual submit of the form.
    });



    $(this).on('click', '.edit-mll-bnt', function() {
        mll_id = $(this).attr("id");
        if (!mll_id) {
            mll_id = 'Cancel'
        }
        $.get('/omckv2/mll_form/', {
            mll_id: mll_id
        }, function(data) {
            $('.filter-mll-div').html(data);

            if (mll_id != 'submit-id-cancel') {

            }
        });
        var navigationFn = {
            goToSection: function(id) {
                $('html, body').animate({
                    scrollTop: $(id).offset().top
                }, 0);
            }
        }
        navigationFn.goToSection('#amll-form');
        return false

    });

*/
    //command................

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
    function gup( name, url ) {
      if (!url) url = location.href;
      name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
      var regexS = "[\\?&]"+name+"=([^&#]*)";
      var regex = new RegExp( regexS );
      var results = regex.exec( url );
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




    //IMPORTANCE
    //GET FORM
    /*

            $(this).on('click', 'ul.dropdown-menu > li#add-comment,ul.comment-ul > li > a.edit-commnent', function() {
            class_atag = $(this).attr("class")
            that = this
            mll_id = $(this).closest("tr").find('td.id').html()
            url = '/omckv2/handelCommentForMLLForm/'
            comment_id = $(this).attr("comment_id")
            if (!comment_id) {
            comment_id = 'new'
                }
            data = {}
            url = url + comment_id + '/'
            action = url
            url = action + '?selected_instance_mll=' + mll_id //add



            $.get(url, data, function(data) {
                $("#modal-on-mll-table").html(data)
                $("#modal-on-mll-table").find('form#add-comment-form-id').attr('action', action)
                copy_row(that)
                $("#modal-on-mll-table").modal();
            })

            return false;
        })



     // chi con dung cho form commenformllform
        $(this).on('submit', '#add-comment-form-id', function() {
            var clicked_button = $("input[type=submit][clicked=true]").attr("value")
            console.log('clicked_button', clicked_button)
            var url = $(this).attr('action')
            var classname = $(this).attr("class")
            
            if (clicked_button == "ADD NEW") {
                url = url.replace(/\/\d+\//g, '/new/')
                console.log(url)
            }

            console.log('url in form submit', url)
            var data = $(this).serialize()
                //data += "&selected_instance_mll=" + encodeURIComponent(selected_instance_mll)
            $.ajax({
                type: "POST",
                url: url,
                data: data, // serializes the form's elements.
                success: function(data) {
                        $("#modal-on-mll-table").modal("hide");
                        $('#danh-sach-mll').html(data); // show response from the php script.
                
                },
                error: function(request, status, error) {
                    console.log('status', error)
                    if (error == 'FORBIDDEN') { //403
                        alert(request.responseText);
                    } else if (error == 'BAD REQUEST') { //400 required form, validation form
                        $("#modal-on-mll-table").html(request.responseText)
                        $("#modal-on-mll-table").find('form#add-comment-form-id').attr('action', url)
                    }
                }

            });
            //}
            return false;
        })
    */


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
                    if (ui.item['desc'] == "chưa có sdt" || !ui.item['desc']) {
                        this.value = ui.item['label']
                    } else {
                        this.value = ui.item['label'] + "-" + ui.item['desc'];
                    }

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

                    /*
                    $.get('/omckv2/detail_tram_compact_with_search_table/', {
                        id: ui.item.id,
                        query: ui.item.label
                    }, function(data) {
                        formhtml = $(data).find('div#form-area').html()
                        tabelhtml = $(data).find('div#table-area').html()
                        $('.thong-tin-tram').fadeOut(300);
                        $('.thong-tin-tram').html(formhtml).fadeIn(300);
                        $('.thong-tin-tram').attr('site_id', ui.item.id)
                        assign_and_fadeoutfadein($('.danh-sach-tram-tim-kiem'), tabelhtml)
                            //$('.danh-sach-tram-tim-kiem').html(tabelhtml);
                    });
                        */
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
    $('.selectmultiple').select2()
        //$(".tablemll").colResizable();

    $('.mySelect2').select2({
        width: '100%'
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

    $('.comboboxd4').combobox()
        /*
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
$(function() {
    $(".comboboxd4").combobox();

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
    /*
    function consume_alert() {
        if (_alert) return;
        _alert = window.alert;
        window.alert = function(message) {
            new PNotify({
                title: 'Alert',
                text: message
            });
        };
    }
    */
PNotify.prototype.options.delay ? (function() {
    PNotify.prototype.options.delay = 1500;

}()) : (alert('Timer is already at zero.'))


function test() {
    console.log('toi dang test')
}

test(1);

(function($) {
    $.widget("custom.combobox", {
        _create: function() {
            this.wrapper = $("<span>")
                .addClass("custom-combobox")
                .insertAfter(this.element);

            this.element.hide();
            this._createAutocomplete();
            this._createShowAllButton();
        },

        _createAutocomplete: function() {
            var selected = this.element.children(":selected"),
                value = selected.val() ? selected.text() : "";

            this.input = $("<input>")
                .appendTo(this.wrapper)
                .val(value)
                .attr("title", "")
                .addClass("custom-combobox-input ui-widget ui-widget-content ui-state-default ui-corner-left")
                .autocomplete({
                    delay: 0,
                    minLength: 0,
                    source: $.proxy(this, "_source")
                })
                .tooltip({
                    tooltipClass: "ui-state-highlight"
                });

            this._on(this.input, {
                autocompleteselect: function(event, ui) {
                    ui.item.option.selected = true;
                    this._trigger("select", event, {
                        item: ui.item.option
                    });
                },

                autocompletechange: "_removeIfInvalid"
            });
        },

        _createShowAllButton: function() {
            var input = this.input,
                wasOpen = false;

            $("<a>")
                .attr("tabIndex", -1)
                .attr("title", "Show All Items")
                .tooltip()
                .appendTo(this.wrapper)
                .button({
                    icons: {
                        primary: "ui-icon-triangle-1-s"
                    },
                    text: false
                })
                .removeClass("ui-corner-all")
                .addClass("custom-combobox-toggle ui-corner-right")
                .mousedown(function() {
                    wasOpen = input.autocomplete("widget").is(":visible");
                })
                .click(function() {
                    input.focus();

                    // Close if already visible
                    if (wasOpen) {
                        return;
                    }

                    // Pass empty string as value to search for, displaying all results
                    input.autocomplete("search", "");
                });
        },

        _source: function(request, response) {
            var matcher = new RegExp($.ui.autocomplete.escapeRegex(request.term), "i");
            response(this.element.children("option").map(function() {
                var text = $(this).text();
                if (this.value && (!request.term || matcher.test(text)))
                    return {
                        label: text,
                        value: text,
                        option: this
                    };
            }));
        },

        _removeIfInvalid: function(event, ui) {

            // Selected an item, nothing to do
            if (ui.item) {
                return;
            }

            // Search for a match (case-insensitive)
            var value = this.input.val(),
                valueLowerCase = value.toLowerCase(),
                valid = false;
            this.element.children("option").each(function() {
                if ($(this).text().toLowerCase() === valueLowerCase) {
                    this.selected = valid = true;
                    return false;
                }
            });

            // Found a match, nothing to do
            if (valid) {
                return;
            }

            // Remove invalid value
            this.input
                .val("")
                .attr("title", value + " didn't match any item")
                .tooltip("open");
            this.element.val("");
            this._delay(function() {
                this.input.tooltip("close").attr("title", "");
            }, 2500);
            this.input.autocomplete("instance").term = "";
        },

        _destroy: function() {
            this.wrapper.remove();
            this.element.show();
        }
    });
})(jQuery);


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


//$(function() {
//PNotify.prototype.options.styling = "bootstrap3";
//new PNotify({
//title: 'Regular Notice',
//text: 'Hello! Have a good day!'
//});
//