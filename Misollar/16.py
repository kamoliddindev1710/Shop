lst=['alik','found','ation','78','arsenal','arsenal']
katta=[]
a=len(lst[0])
for x in lst:
    if a<len(x):
       a=len(x)
       katta=x
print(katta)