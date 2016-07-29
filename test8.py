# -*- coding: utf-8 -*-
from random import randint
xac_suat = {3:0.00462962962962963,4:0.0138888888888889,5:0.0277777777777778,6:0.0462962962962963,7:0.0694444444444444,8:0.0972222222222222,9:0.115740740740741,10:0.125,11:0.125,12:0.115740740740741,13:0.0972222222222222,14:0.0694444444444444,15:0.0462962962962963,16:0.0277777777777778,17:0.0138888888888889,18:0.00462962962962963}
mau_thu = 10000
TAI = 1
XIU = 0
def roll_3_dice():
    tong_3_cau_lists = []
    tai_xiu_lists = []
    so_luong_tai = 0
    so_luong_xiu = 0
    for i in range(1,mau_thu+1):
        tong_3_cau = randint(1,6) + randint(1,6) + randint(1,6)
        tong_3_cau_lists.append(tong_3_cau)
        if tong_3_cau <11:
            so_luong_xiu +=1
            tai_xiu_lists.append(XIU)
        else:
            so_luong_tai +=1
            tai_xiu_lists.append(TAI)
    return tong_3_cau_lists,tai_xiu_lists
    
    
    
tong_3_cau_lists,tai_xiu_lists = roll_3_dice()    
#Test lai xac suat cua 1 lan roll 3 dice
count_3_to18_dict  = {}
for i in range(3,19):
    rs_percent = tong_3_cau_lists.count(i)/float(mau_thu)
    sai_so = (rs_percent -xac_suat[i])*100/float(xac_suat[i])
    count_3_to18_dict[rs_percent ] = i
    print u'tổng 3 cầu, phần trăm, sai số ',i,rs_percent,"%.2f%%" %sai_so


# count xen ke, hoac giong nhau, tich luy
GIONG_NHAU=0
XEN_KE=1

def create_giong_nhau_khac_nhau_lists(tai_xiu_lists,show_description = "tai xiu type"):
    xen_ke_or_giong_nhau_lists= []
    GIONG_NHAU=0
    XEN_KE=1
    so_cau_tai_giong_nhau_trong_1_nhom = 0
    so_cau_xiu_giong_nhau_trong_1_nhom = 0
    tai_repeat_lists = []
    xiu_repeat_lists = []
    for c,current_i in enumerate(tai_xiu_lists):
        if current_i==XIU:
            so_cau_xiu_giong_nhau_trong_1_nhom += 1
        else:
            so_cau_tai_giong_nhau_trong_1_nhom +=1
        if c ==0:
            bf_i = current_i
        else:
            if current_i !=bf_i:
                xen_ke_or_giong_nhau_lists.append(XEN_KE)
                if current_i==XIU:
                    chot_tai = so_cau_tai_giong_nhau_trong_1_nhom
                    tai_repeat_lists.append(chot_tai)
                    so_cau_tai_giong_nhau_trong_1_nhom =0
                else:#chot so_luong_tai
                    chot_xiu = so_cau_xiu_giong_nhau_trong_1_nhom
                    xiu_repeat_lists.append(chot_xiu)
                    so_cau_xiu_giong_nhau_trong_1_nhom= 0
            else:
                xen_ke_or_giong_nhau_lists.append(GIONG_NHAU)
            bf_i = current_i
    
    description_for_tai = "tai" if  show_description == 'xen ke type' else  "xen ke"
    description_for_xiu = "xiu" if  show_description == 'xen ke type' else  "giong nhau"
    print '%s_repeat_lists'%description_for_tai,tai_repeat_lists
    print '%s_repeat_lists'%description_for_tai,xiu_repeat_lists
    print 'len_%s_repeat_list,len_%s_repeat_list'%(description_for_tai,description_for_xiu),len(tai_repeat_lists),len(xiu_repeat_lists)
    for i in range(1,20):
        tai_repeat_list_count = tai_repeat_lists.count(i)
        xiu_repeat_list_count =  xiu_repeat_lists.count(i)
        rs_percent_t = tai_repeat_list_count*100/float(mau_thu)
        rs_percent_x =  xiu_repeat_list_count*100/float(mau_thu)
        print u'repeat number,%s repeat,%s repeat '%(description_for_tai,description_for_xiu),i,"%s (%.2f%%)"%(tai_repeat_list_count,rs_percent_t),"%s (%.2f%%)"%(xiu_repeat_list_count,rs_percent_x)
    print 'so luong different',xen_ke_or_giong_nhau_lists.count(XEN_KE)
    print 'so luong same',xen_ke_or_giong_nhau_lists.count(GIONG_NHAU)
    return xen_ke_or_giong_nhau_lists,tai_repeat_lists,xiu_repeat_lists
if __name__ == '__main__':            
    xen_ke_or_giong_nhau_lists,tai_repeat_lists,xiu_repeat_lists = create_giong_nhau_khac_nhau_lists(tai_xiu_lists,show_description = 'xen ke type')            
    print '###########################'
    print 'tai xiu list',tai_xiu_lists
    print 'xen_ke_or_gion',xen_ke_or_giong_nhau_lists
    print 'chieu dai cua xen_ke_or_giong_nhau_lists',len(xen_ke_or_giong_nhau_lists)
    create_giong_nhau_khac_nhau_lists(xen_ke_or_giong_nhau_lists)
