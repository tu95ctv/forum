def f():
    return '<td>%s</td>'%x
    
ls = ['a','b','c']
print ' '.join(map(lambda x:'<td>%s</td>'%x,ls))