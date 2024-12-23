# a=int(input("Havo haroratini kiriting: "))
# if a<0:
#     print("Sovuq")
# else:
#     print("Issiq")
# # print("Issiq") if a>0 else print("0ga teng") if a==0 else print("past")
# a=int(input("Parolni kiriting: "))
# print("Xush kelibsiz") if a==1017 else print("Xayrrrr")
# a=str(input("Ismingizni kiriting: "))
# b=a.count("aka")
# if a in a:
#     print("Ismingizda a bor")
# else:
#     print('Ismingizda a yoq')
# print(b, "ta")
# b=a.find("a")
# # print(b)
# b=a.rfind("a")
# # print(b)
# a=str(input("Ismingizni kiriting: "))
# a=a.title()
# print(a)
# for x in range(1,21):
#     if x%2==0:
# #      print(x)
# a="kamol".join(a)
# print(a)
# # a=a.split()
# son=int(input("Son kiriting: "))
# for x in range(son,0,-1):
#     for g in range (x,0,-1):
#         print("*",end=" ")
# #     print()
# limit=int(input("Sonlar limitini kiriting: "))
# b=0
# kopaytma=1
# for x in range(0,limit):
#     print("Son kiriting: ")
#     son=int(input(f"{x}-> "))
#     d=son
#     if son%2!=0 and son>0:
#         kopaytma*=son
#     if (d=son)>b:
#         a=d
# print(f"{kopaytma} va {a} ortasida gi farq={kopaytma-a}")
# while True:
#     a=int(input("Son kiriting: "))
#     if a==0:
#         print("Game overrr")
#         break
#     elif a%3==0 and a%5==0 and a%7==0:
# #         print(a)
# limit=int(input("Limitni kiriting: "))
# b=11
# for x in range(0,limit):
#     son=int(input("Son kiriting; "))
#     if son%11==0:
#         d=son
#         if b<d:
#             b=d
# # print(b)      
# counnt=0   
# while True:
#     i=0
#     while i<=3:
#         son=int(input("Son kiriting: "))
#         if son<0:
#             counnt+=1
#             if counnt==3:
#                 print("Uchta manfiy son bor ")
#         i+=1
# i=21
# while True:
#     son=int(input("Son kiriting: "))
#     if i<son:
#         i=son
#     elif son==0:
#         break
# print(i)\
# i=0
# count=0
# while True:
#     son=int(input("Son kiriting: "))
#     if son%5!=0 and son%7!=0:
#         count+=1
#     if son<0:
#         i+=son
#     if son==0:
#         break
# print(f"Soni {count}")
# # print(f"Manfiylar yigindisi {i}")
# sum=0
# i=0
# while True:
#     son=int(input("Son kiriting: "))
#     if son==0:
#         break
#     if son%7==0:
#         sum+=son
#         i+=1
    
# print(f"{sum/i}")
# b=0
# while True:
#     son=int(input("Son kiriting: "))
   
#     if b>son or b==son:
#      print("Sonlar kamayish tartibida ")
#     else:
#         print("Xato ketdii")


# # list hosil qilish
# list=[1,2,3,"kamol",13.5]
# print(list)
# print("kamol" in list)
# list.append("kamron")
# print(list)
# nimaga yangi malumot oshilayotgan paytda qavs olish kerak hunki  by yangi malumoti bildiradi,agar tirtbchak olina bu listg aetibor qaratilayotgan boladi
# list.remove("kamron")
# print(list)
# list.pop(4)
# # print(list)
# list=(1,2,3 ,"kamol")
# # print(list[3])
# a=int(input("Son kiriting: "))
# b=int(input("Son kiriting: "))
# if (a+b)%2!=0:
#     print("oq")
# else:
# #         print("qora")
# for x in range(1,1001):
#     count=0
#     for z in range(1,x+1):
#         if x%z==0:
#             count+=1
#     if count==9:
#         print(x)

# for x in range(1,99):
#    if str(x).count("3") :
#     print(x)

# for x in range(1,99):
#   count=0
#   for z in range(1,x+1):
#     if x%z==0:
#         count+=1
#   if count==2:
#     a=x//10
#     b=x%10
#     c=b*10+a
#     d=x+c
#     if d//10 == d%10 :
# #         print(x)
# for x in range(1,1001):
#     sum=0
#     for  z in range(0,x):
#         if x%z==0:
#             sum+=z
#     if sum==x:
# #         print(z,)
# a=list[input("Gap kiriting: ")]
# print(a)
# a.split()
# # print(a)
# a=list(input("Son kiriting: "))
# b=len(a)
# d=max(a)
# for i in a:
# #     if d>i:
# a=input("soz kiriting: ")
# word=a.split()
# sentence=a.split(".")
# print(word)
# # print(sentence)
# list=[1,3,4,6,3,4,0,-1,7,8]
# for indeks,n in  enumerate(list):
#     indeks=list[0]
#     for z ,l in enumerate(list):
#         if indeks<l:
#             print(l)
#             indeks=l
#     print()
# uyga vazifa 28.11 kunniki ,avzu list
# natija=max(lst)
# # print(natija)
# lst=[[1,2],[0,0,2],[7,0],[2,1,3],[7,0]]
# yangi=[]
# a=sum(lst[0])
# for x in lst:
#     natija=sum(x)
#     if a<natija:
#         a=natija
#         yangi=x
# # print(yangi)
# lst=['alik','found','ation','78','arsenal','arsenal']
# katta=[]
# a=len(lst[0])
# for x in lst:
#     if a<len(x):
#        a=len(x)
#        katta=x
# # print(katta)
# lst=[[],['salom',0],[],[76,3],[],[]]
# # print(lst[0])
# # print(len(lst))
# for x in [[],['salom',0],[],[76,3],[],[]] :
#     if len(x)==0:
#        lst.remove(x)
      
# print(lst)
# for i in range(lst.count(0)):
#     lst.remove(0)
# print(lst)

# for harf in lst:
#     soz+=harf
# yangi.append(soz)
# print(yangi)
x=float(input("1-> "))
y=float(input("2-> "))
z=x+y
z=round(z,3)
print(z)
print(f"{z:.2f}")