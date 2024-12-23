# def kitob():
#     try:
#         class computer:
#             def __init__(self,name,author,price,publisher):
#                 self.nom=name
#                 self.muallif=author
#                 self.narx=price
#                 self.nashriyot=publisher
            

#             def input_info(self):
#                 self.nom=input("kompyuter nomini kiriting: ")
#                 self.muallif=input("Muallifni kiriting: ")
#                 self.narx=float(input("kompyuter narxini kiriting: "))
#                 self.nashriyot=input("kompyuter nashriyotini kiriting: ")

#             def output_info(self):
#                 print(f"kompyuter nomi {self.nom}")
#                 print(f"kompyuter muallifi {self.muallif}")
#                 print(f"kompyuter narxi {self.narx}")
#                 print(f"kompyuter nashriyoti {self.nashriyot}")


#         c1=computer("O'tkan kunlar","Abdulla Qodiriy",25000,"Asaxiy")
#         c2=computer("Jannati odamlar","Xudoyberdi To'xtaboyrv",20000,"Zumrad")
#         c3=computer("Garri potter va sehrli tosh","Joanna Ketlin Rouling",30000,"Asaxiy")
#         c4=computer("Mahorat","Rupert Grin",50000,"Ildiz")
#         c5=computer("Yapon zobiti","Ato Hamdam",40000,"Qamar")
#         lst=[c1,c2,c3,c4,c5]
#         for x in range(0,5):
#             lst[x].input_info()

#         for x in range(0,5):
#          if  lst[x].nashriyot[0].lower()>"a" and lst[x].nashriyot[0].lower()<"h":
#             lst[x].output_info()
#             print()

#     except Exception as ex:
#         print(ex)

# kitob()



# def kompyuter():
#     try:
#         class computer:
#             def __init__(self,name,RAM,price,processor):
#                 self.nom=name
#                 self.ram=RAM
#                 self.narx=price
#                 self.protsessor=processor
            

#             def input_info(self):
#                 self.nom=input("Kompyter nomini kiriting: ")
#                 self.ram=int(input("Kompyuter ramini kiriting: "))
#                 self.narx=float(input("Komputer narxini kiriting: "))
#                 self.protsessor=input("Kompyuter protsessorini kiriting: ")

#             def output_info(self):
#                 print(f"kompyuter nomi {self.nom}")
#                 print(f"kompyuter rami {self.ram}")
#                 print(f"kompyuter narxi {self.narx}")
#                 print(f"kompyuter protsessor {self.protsessor}")


#         c1=computer("hp 100",8,2000000,"core i7")
#         c2=computer("Asus",5,3000000,"i3")
#         # c3=computer("lenovo",8,4000000,"i7")
#         # c4=computer("Toshiba",16,5000000,"i7")
#         lst=[c1,c2]
#         for x in range(0,2):
#             lst[x].input_info()

#         for x in range(0,2):
#          if  lst[x].ram>4 and lst[x].ram<16:
#             lst[x].output_info()
#             print()

#     except Exception as ex:
#         print(ex)

# kompyuter()






def friend_website():
    try:
        class yuser:
            def __init__(self,name="",age=0,animal="",fruit="",hobby="",nation="",IQ=0):
                self.ism=name
                self.yosh=age
                self.jonzot=animal
                self.meva=fruit
                self.hobbi=hobby
                self.millat=nation
                self.aykyu=IQ

            def set_info(self):
                self.ism=input("Ismingizni kiriting: ")
                self.yosh=int(input("Yoshingizni kiriting: "))
                self.jonzot=input("Sevimli jonzotingizni kiriting: ")
                self.meva=input("Sevimli mevangizni kiriting: ")
                self.hobbi=input("Sevimli hobbingizni kiriting: ")
                self.millat=input("Millatingizni kiriting: ")
                self.aykyu=int(input("IQingizni kiriting: "))

            def get_info(self):
                print(f"Sizning ismingiz->{self.ism}\nYoshingiz ->{self.yosh}\nSevimli jomzotingiz->{self.jonzot}\nSevimli mevanigz->{self.meva}\nHobbingiz->{self.hobbi}\nMillatingiz->{self.millat}")

            def get_score(self):
                if self.aykyu<85:
                    print(f"{self.ism} sizning IQ iz qoniqarli")
                elif self.aykyu>85 and self.aykyu<135:
                    print(f"{self.aykyu} Zo'r")
                else :
                    print(f"{self.aykyu} Qoyil juda zo'r")

        num_user=int(input("Nechta ishtirokchi kiritmochisiz: "))
        lst=[]
        for x in range(0,num_user):
            useeer=yuser()
            useeer.set_info()
            lst.append(useeer)

        for x in range(0,num_user):
            lst[x].get_info()
            lst[x].get_score()

    except Exception as ex:
        print(ex)



friend_website()
