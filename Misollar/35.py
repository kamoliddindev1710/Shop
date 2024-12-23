from random import randint


# class salom:
#     def show():
#      print('Salom')

# a1=salom
# a1.show()

# class animal:
#     def __init__(self,name,type):
#      self.nomi=name
#      self.turi=type
    
#     def print_t(self):
#        print(self.nomi,self.turi)


# a1=animal("bo'ri","yirtqich")
# a2=animal("sigir ","sut emizuvchi ")
# a1.print_t()
# a2.print_t()


# class computer:
#     def __init__(self,name,price,date,speed,size,color,made_in):
#         self.nomi=name
#         self.narx=price
#         self.sana=date
#         self.tezlik=speed
#         self.vazn=size
#         self.rang=color
#         self.joyi=made_in

#     def nomii(self):
#         print(self.nomi)
#     def narxi(self):
#         print(self.narx)
#     def sanasi(self):
#         print(self.sana)
#     def tezliki(self):
#         print(self.tezlik)
#     def hajmi(self):
#         print(self.hajmi)

# a1=computer
# a2=computer


# class car:
#     def __init__(self,name,year,speed):
#         self.nom=name
#         self.yil=year
#         self.tezlik=speed

#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def turn_right(self):
#         pass
#     def turn_back(self):
#         pass


# c1=car()
# c2=car()
# c3=car()
# c4=car()
# c5=car()



# class talaba:
#     def __init__(self,name,family,score):
#         self.ism=name
#         self.familya=family
#         self.baho=score
    
#     def print_name(self):
#          print(self.ism)

# a1=talaba("Jon","Potter",randint(0,100))
# a2=talaba("Bon","Pete",randint(0,100))
# a3=talaba("Jek","London",randint(0,100))
# print(f"{a1.ism}ning bahosi: {a1.baho}")
# print(f"{a2.ism}ning bahosi: {a2.baho}")
# print(f"{a3.ism}ning bahosi: {a3.baho}")
# if a1.baho > a2.baho and a2.baho>a3.baho:
#     a3.print_name()
# elif a1.baho > a3.baho and a3.baho>a2.baho:
#     a2.print_name()
# else :
#     a1.print_name()




# class Student:
#     def __init__(self, name, surname, grade):
#         self.name = name
#         self.surname = surname
#         self.grade = grade

#     def info(self):
#         return "Name    : %s \nSurname : %s \nName    : %s"%(self.name, self.surname, self.grade)
        
# st1 = Student("Hoshim", "Bugdoyev", 5)
# st2 = Student("Ketmon", "Valiyev", 1)
# st3 = Student("Tesha", "Karimov", 3)

# lst = [st1, st2, st3]

# grade = st1.grade
# person = st1
# for i in lst:
#     if grade > i.grade:
#         grade = i.grade
#         person = i

# print(person.info())


# lst = [st1, st2, st3]
# r = min(lst, key=lambda i: i.grade)
# print(r.info())



# class restoran:
#     def __init__(self,name,time,rating,menu):
#         self.nom=name
#         self.vaqt=time
#         self.reyting=rating
#         self.menyu=menu


#     def print_name(self):
#         print(self.nom)

#     def print_menu(self):
#         print(self.menyu)

#     def kirish_chiqish(self):
#         print(f"{self.vaqt[0:2] }:00 dan {self.vaqt[3:5]}:00 gacha ochiq")
#     def print_rating(self):
#         print(self.reyting)


# a1=restoran("Besh yulduz","08-19",5,["osh","shorva"])
# # a2=restoran()


# a1.print_name()
# a1.print_menu()
# a1.print_rating()
# a1.kirish_chiqish()


# nums=[3,2,4]
# target=6
# lst=[]
# for x in range(len(nums)):
#     for i in range(x+1,len(nums)):
#         if nums[x]+nums[i]==target:
#             lst.append([x,i])
# for x in lst:
#     print(x)


# 