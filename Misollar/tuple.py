# top=("salommemem","kam")
# yangi=[]
# a=sum(tuple)
# print(a)
# katta=max(tuple)
# kichik=min(tuple)
# print(katta-kichik)
# top=list(top)
# a=max(top)
# top.remove(a)
# top=tuple(top)
# print(top)
# for x in top:
#     if isinstance(x,str):
#         if len(x)>2:
#             yangi.append(x)
# print(yangi)
# lst=[(1,2),(2,3),(3,4)]
# yangi =[]
# for x in lst:
#     # x=list(x)
#     a=sum(x)
#     yangi.append(a)
# print(yangi)
# lst=[(1,2),(2,3),(3,4)]
# tpl=[]
# for x in lst:
#     x=list(x)
#     tpl.append(x)
# print(tpl)


# t= (1,2,3,4,5,6,7,8,9,0,11)
# print(t[3],t[-4])

# lst=[(10,20,40),(40,50,60),(70,80,90)]
# for x in lst:
#     x=list(x)
#     x[-1]=100
#     # x=tuple(x)
# # print(lst)
# for i in range(len(lst):
#     lst[i]=

# lst=['p','q']
# lst2=[]
# a=int(input("Son kiriting: "))
# soz=""
# for x in range(1,a+1):
#     soz=lst[0]+str(x)
#     lst2.append(soz)
#     soz=lst[1]+str(x)
#     lst2.append(soz)
# print(lst)
tpl=((1,2,3),(4,5),(8,9,10,11))
tpl=list(tpl)
tup=tuple()
tup=list(tup)
d=len(max(tpl))
# for x in tpl:
#     if len(x)==d:
#         tpl.remove(x)
tpl=[x for x in tpl if len(x)!=d]
tup=[ i for x in tpl for i in x ]
print(tpl)
# for x in tpl:
#     for i in x :
#         tup.append(i)
# tup=tuple(tup)
print(tup)