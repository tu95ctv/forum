def f(x):
    return '<td>%s</td>'%x
    
ls = ['a','b','c']
print ' '.join(map(f,ls))