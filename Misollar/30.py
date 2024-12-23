# f=open("Salom.txt","w")
# with open("Salom.txt",encoding="utf-8") as f:
#  lst = [i for i in f.read().split("\n")]
#  ls = sorted(lst, key=lambda i: i.split(" ")[-1])
# for i in ls:
#  print(i)
#  raqam=[]
#  for x in f.read().split('\n'):
#   raqam.append(x[5:8])
# print(raqam)
#  yangi=[]
#  for i in f.read().split('\n'):
#   yangi.append(i[8:])

# # a=set()
# for x in yangi:
# #  a=set(x)
#  if len(set(x))==8:
#   print(x)
 

# with open("Salom.txt", encoding="utf-8") as f:
#     for i in f.read().split("\n"):

#         if len(set(i[8:]))==8:
#             print(i)

# f=open("kino.txt","w")
# f.close()
# def kinolar():
#     try:
#         with open("kino.txt",encoding="utf-8") as f:
#             lst=[x for x in f.read().split('\n')]
#             lst=sorted(lst,key=lambda i : i.split(',')[-2])
#             for l in lst:
#                 print(l)
#     except Exception as x:
#         print(x)
    

# kinolar()

       
# with open("kino.txt",encoding="utf-8") as f:
#     lst=[x for x in f.read().split('\n')]
#     for i in lst:
#         if "2000" < i.split(',')[-2]:
#             print(i.split(",")[1],i.split(",")[-1])

# f=open("qurilma.txt","w")
# f.close()

# def qurilma():
#     try:
#         with open("qurilma.txt",encoding="utf-8") as f:
#             lst=[x for x in f.read().split('\n')]
#             lst2=['06','07','08']
#             for  l in lst:
#                 if l.split(",")[-2][3:5] in lst2:
#                     print(l)
#     except Exception as ex:
#         print(ex)

# qurilma()


# f=open("karta.txt","w")
# f.close()
# with open("karta.txt",encoding="utf-8") as f:
#     natija={}
#     for x in f.read().split('\n'):
#         b=x.split(',')[-1]
#         if b not in natija:
#             natija[b]=1
#         else :
#             natija[b]+=1
#     print(natija)

# def karta():
#     try:
#         with open("karta.txt",encoding="utf-8") as f:
#             lst=[x for x in f.read().split('\n')]
#             ls=[]
#             for i in lst:
#                 if "visa"in i.split(',')[1]:
#                     ls.append(i)
#             ls=sorted(ls,key=lambda x: x.split(",")[-1])
#             for x in ls:
#                 print(x)
#     except Exception as ex:
#             print(ex)
# karta()
            

# def karta():
#     try:
#         with open("karta.txt",encoding="utf-8") as f:
#             lst=[x for x in f.read().split('\n')]
#             for x in lst:
#                 r=set(x.split(',')[0])
#                 if len(r)==10:
#                     print(x)

#     except Exception as ex:
#         print(ex)
# karta()


# f=open("internet.txt",'w')
# f.close()

# def internet():
#     try:
#         with open("internet.txt",encoding="utf-8") as f:
#             lst= f.read().split("\n")
#             for x in lst:
#                 r=x.split(',')[-2]
#                 a=r.split("-")
#                 # print(a)
#                 c=True
#                 for i in a:
#                     if i.isdigit():
#                         continue
#                     else:
#                         c=False
#                 if c==True:
#                     print(a)
#     except Exception as ex:
#          print(ex)
        
        


# internet()


