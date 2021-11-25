def Merge(dict1,dict2):
    return(dict2.update(dict1))
dict1={'arun':23,'zyna':34,'sona':67}
dict2={'amal':21,'balu':1,'anjana':45}
print(dict1)
print(dict2)
print(Merge(dict2,dict1))
print(dict1)
