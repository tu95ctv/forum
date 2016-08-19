ls = ['a','b','c']
def insert_item_end_list_delete_begin(ls,end_item):    
    ls.insert(len(ls),end_item)
    ls.remove(ls[0])
    print ls
insert_item_end_list_delete_begin(ls,'d')
insert_item_end_list_delete_begin(ls,'e')