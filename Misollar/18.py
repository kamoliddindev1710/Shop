lst=['p','q']
lst2=[]
a=int(input("Son kiriting: "))
soz=""
for x in range(1,a+1):
    soz=lst[0]+str(x)
    lst2.append(soz)
    soz=lst[1]+str(x)
    lst2.append(soz)
print(lst2)
