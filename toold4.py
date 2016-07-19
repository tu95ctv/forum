import re
from django.core.exceptions import MultipleObjectsReturned
#from LearnDriving.settings import MYD4_LOOKED_FIELD

def luu_doi_tac_toold4(Doitac_objects,doi_tac_inputext,is_save_doitac_if_not_exit=True):
    if doi_tac_inputext:
                fieldnames= ['Full_name','Don_vi','So_dien_thoai']
                if "-" not in doi_tac_inputext:
                    try:
                        if is_save_doitac_if_not_exit:
                            taodoitac = Doitac_objects.get_or_create(Full_name = doi_tac_inputext)
                            return taodoitac[0]
                        else:#only get doitac not save new doitac if doitac not exit
                            doitac = Doitac_objects.get(Full_name = doi_tac_inputext)
                            return doitac
                    except :
                        return None
      
                else: # if has - 
                    doi_tac_inputexts = doi_tac_inputext.split('-')
                    sdtfield = fieldnames.pop(2)
                    p = re.compile('[\d\s]{3,}')
                    kq= p.search(doi_tac_inputext)
                    try:
                        phone_number_index_of_ = kq.start()
                        #Define the index of number phone in array, 0 or 1, or 2, or 3
                        std_index = len(re.findall('-',doi_tac_inputext[:phone_number_index_of_]))
                        fieldnames.insert(std_index, sdtfield)
                    except:
                        pass
                    dictx = dict(zip(fieldnames,doi_tac_inputexts))
                    if is_save_doitac_if_not_exit:
                        doitac = Doitac_objects.get_or_create(**dictx)[0]
                    else:
                        doitac = Doitac_objects.get(**dictx)
                return doitac
    else:
        return None

def create_dict_d41(contains,fieldnames):
    dict ={}
    for contain in contains:
        contain = contain.lstrip().rstrip()
        for key in fieldnames:
            p = re.compile('^'+ key +'_',re.VERBOSE)
            kq = p.subn('',contain)
            #print kq[1]
            if kq[1]:
                #print key,contain.replace(key+'_','')
                #print key,p.subn('',contain)
                dict[fieldnames[key]] = kq[0]
                continue
        if kq[1]==0:
            dict["all field"] = contain
                
    print dict
    return dict
def recognize_fieldname_of_query(contain,fieldnames):
    contain = contain.lstrip().rstrip()
    for longfield,sortfield in fieldnames.items():
        p = re.compile('^'+ sortfield +'=',re.IGNORECASE)
        kq = p.subn('',contain)
        if kq[1]:# Neu dung la co sortfield trong contain , vi du sn1=abc
            contain = kq[0]
            fieldname = longfield
            return (fieldname,contain)
    if kq[1]==0:
        p = re.compile('^'+ '(.*?)' +'=(.*?)$',re.IGNORECASE)
        kq = p.findall(contain)
        if kq: # vi du nhu la site_name_2=tram-a
            fieldname = kq[0][0].lstrip().rstrip().replace(" ","_")
            contain = kq[0][1].lstrip().rstrip()
            print 'fieldname',fieldname
        else:
            fieldname = "all field"
        if contain[0]=='!':
            contain = contain[1:]
            is_negative_query = True
        else:
            is_negative_query = False
        return (fieldname,contain,is_negative_query)
    

