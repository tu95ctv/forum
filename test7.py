a = {2:3}
def x():
    global a
    a= {}
    a.update({4:5})
x()
print a