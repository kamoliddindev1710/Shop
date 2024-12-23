# lst=[2,5,4,4,1,2,6,7,2,3,1,2,4,5,2,1]
# dct={'juft':[],'toq':[]}
# for x in lst:
#     if x%2==0:
#         dct.get("juft").append(x)
#     else:
#         dct.get('toq').append(x)
# print(dct)
# keys=['ten','twenty','thirty']
# values=[10,20,30]
# dct={}
# for x in range(len(keys)):
#     dct[keys[x]]=values[x]
    
# print(dct)
# dct={'a':100,'b':200,'c':300}
# if 200 in dct.values():
#     print("Bor")
# dct={1:10,2:20,3:30,4:55,5:25}
# dct=list(dct.items())
# print(dct.remove(max(dct,key=lambda x: x[1])))
# print(dct.remove(min(dct,key=lambda x: x[1])))
# dct=dict(dct)
# print(dct)
# lst=[]

# dct1={1:10,2:20}
# dct2={3:30,4:40}
# dct3={9:90,7:70}
# dct1=list(dct1.items())
# dct2=list(dct2.items())
# dct3=list(dct3.items())
# for x in (1,4):
#     lst.append(dct1)
#     lst.append(dct2)
#     lst.append(dct3)
# print(lst)

# list1=['s001','s0002','s003','s004']
# list2=['Adina Park','Leyton Marsh','Duncan Boyle','Saim Richards']
# list3=[85,98,89,92]
# dct1={}
# dct2={}
# for x in range(len(list1)):
#     dct1[list1[x]]=list2[x]
#     dct2[list2[x]]=dct1
#     dct1={}

# print(dct2)
    
# a=input("Soz kiriting: ")
# dct1={}
# for x in a:
#     b=a.count(x)
#     dct1[x]=b
# # print(dct1)
    
# dict1={1:"ABC",2:'DEF',3:'GHI',4:'JKL',5:'MNO'}
# if len(dict1)%2==0:
#  for x in dict1:
#     int n=dict1.values






# data = [
#     {"full_name":"Eugene Elsmor","company":"Kazu","position":"Electrical Engineer","salary":"$4440.86"},
#     {"full_name":"Joni Stredder","company":"JumpXS","position":"Environmental Tech","salary":"$870.05"},
#     {"full_name":"Terri-jo Fulham","company":"Tagchat","position":"Assistant Media Planner","salary":"$1992.55"},
#     {"full_name":"Priscilla Pandya","company":"Youopia","position":"Help Desk Operator","salary":"$3715.95"},
#     {"full_name":"Wolfy Swanborough","company":"Topiclounge","position":"Recruiter","salary":"$1045.61"},
#     {"full_name":"Raleigh Ratter","company":"Zoozzy","position":"Graphic Designer","salary":"$602.41"},
#     {"full_name":"Anastasia Winward","company":"Avaveo","position":"Cost Accountant","salary":"$3641.42"},
#     {"full_name":"Dorry Vasyunichev","company":"Fivebridge","position":"Junior Executive","salary":"$2035.05"},
#     {"full_name":"Richy Cleft","company":"Jamia","position":"Sales Associate","salary":"$912.98"},
#     {"full_name":"Zack Record","company":"Oyonder","position":"Social Worker","salary":"$2492.23"},
#     {"full_name":"Lissy Newns","company":"Riffwire","position":"Developer II","salary":"$1177.79"},
#     {"full_name":"Audrye Churchyard","company":"Photospace","position":"Environmental Tech","salary":"$4125.83"},
#     {"full_name":"Timothy Seligson","company":"Riffpath","position":"Compensation Analyst","salary":"$1271.94"},
#     {"full_name":"Brandie Rogeon","company":"Riffpath","position":"Analyst Programmer","salary":"$1911.09"},
#     {"full_name":"Dane Rugg","company":"Twimm","position":"Associate Professor","salary":"$2200.72"},
#     {"full_name":"Mick Jeduch","company":"Realblab","position":"Executive Secretary","salary":"$1154.20"},
#     {"full_name":"Rowland Christofol","company":"Mycat","position":"Senior Cost Accountant","salary":"$1119.94"},
#     {"full_name":"Sibella Abrahams","company":"Minyx","position":"Internal Auditor","salary":"$4023.25"},
#     {"full_name":"Layne Thomel","company":"Centimia","position":"Research Associate","salary":"$4073.17"},
#     {"full_name":"Demetris Clemenzi","company":"Tagopia","position":"Human Resources Manager","salary":"$1530.37"},
#     {"full_name":"Kerstin Devon","company":"Katz","position":"Senior Quality Engineer","salary":"$1305.61"},
#     {"full_name":"Brandon Burgwyn","company":"Mydeo","position":"Physical Therapy Assistant","salary":"$1325.58"},
#     {"full_name":"Dyana Crosby","company":"Riffpath","position":"Payment Adjustment Coordinator","salary":"$1501.54"},
#     {"full_name":"Harald Voller","company":"Riffpedia","position":"Accountant I","salary":"$4397.60"},
#     {"full_name":"Nollie Phipard-Shears","company":"Aimbo","position":"Legal Assistant","salary":"$3172.57"},
#     {"full_name":"Gaynor Dannohl","company":"Riffpath","position":"Administrative Assistant II","salary":"$3035.89"},
#     {"full_name":"Tome Bensen","company":"Yamia","position":"Assistant Professor","salary":"$3677.10"},
#     {"full_name":"Jessey Anshell","company":"Bubblemix","position":"Registered Nurse","salary":"$2782.66"},
#     {"full_name":"Valentijn Melbury","company":"Bluejam","position":"Statistician I","salary":"$1308.43"},
#     {"full_name":"Rochelle Andrejevic","company":"Riffpath","position":"VP Product Management","salary":"$1734.61"}
# ]
# count=0
# for x in data:
#    for i in x.values():
#     if "Human Resources Manager" in i:
#       count+=1
# print(f"{count} ta odam ishlaydi")
# a=0
# for x in data:
#   if "Human Resources Manager" in x.values():
#     a+=1
# print(a)
# count = [1 for x in data if "Human Resources Manager" in x.values() ]
# print(len(count))
# sum=0
# for x in data:
#     if "Riffpath" in x.values():
#        sum+= float((x.get("salary")[1:]))
# print(f"${sum}")
# sum=0
# for x in data:
#     if "Riffpath" in x.values():
#        sum+=(float((x.get("salary")[1:])))
# print(f"${sum}")

# for x in data:
#     if "K" in (x.get("full_name")[0:1]):
      #   x.get("salary").replace(float(x.get("salary")[1:]),float(x.get("salary")[1:])*2)
      # x.get("salary")[1:]=str(float(x.get("salary")[1:])*2)
      # a=float(x.get("salary")[1:])
      # # print(a)
      # b=a*2
      # print(b)
#       x.get("salary").replace(x.get("salary")[1:],'$'+str(b))
# print(data)
# for x in data:
#     if "K" in (x.get("full_name")[0:1]):
#       a=float(x.get("salary")[1:])
#       b=a*2
#       x["salary"]='$'+str(b)
# print(data)

# for x in data[:]:
#     if "full_name" in x.keys():
#      natija=x.pop("full_name")
#      x["FIO"]=natija  
# print(data)


# for i in data[:]:
#     if i.get("full_name"):
#         natija = i.pop('full_name')
#         a, b = natija[:], i.copy()
#         i.clear()
#         i["FIO"] = a 
#         i.update(b)
# print(data)
# for x in data:
#     if "position" in x.keys():
#          for i in x.values():
#              if "senior"  in i.lower() or "junior" in i.lower():
#                  data.remove(x)
# print(data)
# count=0
# for x in data:
#     if "assistant" in x['position'].lower():
#         count+=1
# print(count,"ta")
# for x in data:
#     if "Assistant" in x['position']:
        # a=x['position'][0:10]
        # a="junior"+x['position'][10:]
        # a=x.get('position')
        # print(x.get('position'))
        # x.get('position').replace('Assistant','Junior')
#         x["position"]=x["position"].replace('Assistant','Junior')
# print(data)

# for x in data:
#     if "Assistant" in x['position']:
#          x["position"]=x["position"].replace('Assistant','Junior')
# print(data)



# dct={'data1':100,'data2':-54,'data3':247}
# a=sum(dct.values())
# print(a)
# i['anor']={olma['meva']='suv'}

# lst=[1,2,3]
# lst2=[61,99,22,61] 
# a=sorted(a,max(lst,key=lambda x: x)
# a=sorted(lst,key=lambda x: x,reverse=True)
# a="".join(max(lst,key=lambda x: x))
# a="".join(str(i) for i in (sorted(lst2,key=lambda x: x)))
# print(a)


ls = [61,228,9]
# # ls.sort(key=lambda x:str(x),reverse=True)
# ls = sorted(ls,key=lambda x: str(x),reverse=True)

# st = ""
# for i in ls:
#     st += str(i)

# print(int(st))


# lst = [[12,'er', 45], [34,55,"wertolot"], [12,"komoldin", 67]]
# # lst = dict(map(dict, lst))
# print(lst)
# lst=dict(lst)
# lst[12]={lst['er']=45}
# a=input("So'z kiriting: ")
# dct={}

# for x in a:
#     for i in x:
#         dct[i]=a.count(i)
# print(dct)
    
# a=input("Satr kiriting: ")
# b=a.split()
# # b[0],b[-1]=b[-1],b[0]
# # print(" ".join([x for x in b]))
# # print(b)
# for x in b:
#     # x[0],x[-1]=x[-1],x[0]
#     temp=x[0]
#     x[0]=x[-1]
#     x[-1]=temp
# print(" ".join([x for x in b]))






# def uzgargan_son(a:int,b:int):
#     return str(a)+str(b)
# print(uzgargan_son(int(input("Qoshmoqchi bolgan soningizni kiriting: ")),int(input("Qoshiladigan sonni kiriting: "))))
# d1={'a':100,'b':200,'c':300}
# d2={'a':300,'b':200,'c':400}

# for x in len(d1):


# for x in range(1000,9999):

# def tort():
#     d=set()
#     for x in range(1000,10000):
#         x=str(x)
#         for i in x.split():
#             set().add(i[0])
#         if len(set())==4:
#             print(x)
#             set().clear

# print(tort())
# def tub(b,a):
#     if b==a:
#         return 0
        
#     if b%a==0:
#         return a 
#     tub(b,a+1)
    

# b=int(input("Son kiriting: "))
# print(tub(b,1))

# a=int()
# a=input("son kiriting: ")
# print(type(a))      
    
# son=int()
# son=int(input())
# print(type(son))

# son=int(input("Son kiriting: "))
# ikki=int(input("Ikkinchi sonni kiriting: "))
# if son>=ikki*2:




# dct2={}
# lst=[]
# a=int(input("Nechta mahsulot kiritmoqchisiz: "))
# for x in range(a):
#    dct={}
#    dct["name"]=input("Nomini kiriting; ")
#    dct["price"]=int(input("Narxini kiriting: "))
#    lst.append(dct)
# for x in range(len(lst)):
#     dct[x]=lst[]

# print(dct2)
# def top(son:str):
#     count=0
#     if son[:1]=='0':
#      for x in son:
#         if x=='0':
#             count+=1
#         else :
#             print("Xato ")
#             break
#     print(f"Boshida {count} ta 0 bor ")

# a=input("Son kiriting: ")
# top(a)


# for x in "salom":
# #     print(x)
# def nechta(son1:int,son2:int):
#     count=0
#     bolinma=son1
#     print(f"{son1}->",end=" ")
#     while bolinma>son2*2:
#         count+=1
#         bolinma/=2
#         if bolinma>son2*2:
#            print(f"{bolinma}->",end=" ")
#         else :
#            print(bolinma)
#     print(f"{count} ta ")
    

# a=int(input("1- son kiriting: "))
# b=int(input("2-son kiriting:  "))
# if a>=b*2:
#    nechta(a,b)
# else :
#    print("Qaytadan kiriting ")

def mahsulot(son1,ls ):
    ls2=[]
    for x in range(len(ls)):
        ls2.append(ls[x]["price"])

    ls2=sorted(ls2,reverse=True)

    for x in range(len(ls)):
        if ls[x]["price"] in ls2[:b]:
           print(ls[x])


lst=[]
a=int(int(input("Nechta mahsulot kiritimoqchisiz: ")))
for x in range(a):
    dct={}
    dct["name"]=input("Nomini kiriting: ")
    dct["price"]=int(input("Narxini kiriting: "))
    lst.append(dct)
b=int(input("Soningizni kiriting: "))
mahsulot(b,lst)


