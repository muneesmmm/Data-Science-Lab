tup1=('back','space')
tup2=('1','2')
print("original key tuple is:"+str(tup1))
print("original value tuple is:"+str(tup2))
if len(tup1)==len(tup2):
    res=dict(zip(tup1,tup2))
print("dictionary:"+str(res))
