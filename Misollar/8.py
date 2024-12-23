# a=int(input("Son kiriting: "))
# i=1
# while i<=a:
#           j=1
#           while j<=i:
#             print("*",end=" ")
#             j+=1 
#           print()
#         #   i+=1  
# a=input("Matn kiriting ")
# indeks=int(input("Indeksni kiriting: "))
# d=0
# for i in a:
#     if d==indeks:
#         b=a[:indeks]+a[indeks+1:]
#     d+=1
    
# # print(b)        
# b=a[:indeks]+a[indeks+1:]
# # print(b)
# b=0
# a=int(input("Son kiriting: "))
# for i in range(1,a+1):
#     b+=i**2
   

# # print(b)
# a=int(input("Bahongizni kiriting: "))
# if a==5:
#     print("A'lo! Ajoyib natija!")
# elif a==4:
#     print("Yaxshi, davom eting!")
# elif a==3:
#     print("Qoniqarli, lekin o'qishni kuchaytirish kerak")
# elif a==2 or a==1:
#     print("Juda past baho, o'qishni yaxshilash kerak!")
# else:
# #     print("Bunday baho yoq")
# a=int(input("Yoshingizni kiriting: "))
# for x in range(200):
#     if x==a:
#         print("Sizning yoshingiz!!!")
#     print(x)

# while True :
#  print("Ovqat turlari","1->Sariyog'li non (bo'lakda)","2->Sho'rva (kosada)","3->Palov (kosada)","4->Shirinlik (bo'lakda)",sep="\n")
#  a=int(input("Ovqat turini kiriting: "))
#  b=int(input("Miqdorini kiriting: "))
#  if a==1:
#     print(f"{b*180} kkal")
#  elif a==2:
#     print(f"{b*150} kkal")
#  elif a==3:
#     print(f"{b*500} kkal")
#  elif a==4:
#     print(f"{b*250} kkal")
#  else:
#     print("Bunday ovqat yoq")
#  print("Davom etasizmi (ha yoki yoq)")
#  javob=input()
#  if javob=="ha":
#     pass
# #  else:
#     break

# for x in range(10,999):
#     a=x//100
#     b=(x//10)%10
#     c=x%10
#     if a==b and a!=c or a==c and a!=b:
#         print(x)
import random
a=int(input("Limitni kiriting: "))
b=random.randint(1,a)


for x in range(1,4):
    top=int(input("Son kiriting: "))
    if top==b:
        print("Winner")
        break
    if x==3:
        print("Looser")
        break
    print(f"Sizda {3-x} ta imkoniyat qoldi")

