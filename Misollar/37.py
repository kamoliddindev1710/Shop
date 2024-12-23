def kitob():
    try:
        class book:
            def __init__(self,name,author,price,publisher):
                self.nom=name
                self.muallif=author
                self.narx=price
                self.nashriyot=publisher
            

            def input_info(self):
                self.nom=input("Kitob nomini kiriting: ")
                self.muallif=input("Muallifni kiriting: ")
                self.narx=float(input("Kitob narxini kiriting: "))
                self.nashriyot=input("Kitob nashriyotini kiriting: ")

            def output_info(self):
                print(f"Kitob nomi {self.nom}")
                print(f"Kitob muallifi {self.muallif}")
                print(f"Kitob narxi {self.narx}")
                print(f"Kitob nashriyoti {self.nashriyot}")


        c1=book("O'tkan kunlar","Abdulla Qodiriy",25000,"Asaxiy")
        c2=book("Jannati odamlar","Xudoyberdi To'xtaboyrv",20000,"Zumrad")
        c3=book("Garri potter va sehrli tosh","Joanna Ketlin Rouling",30000,"Asaxiy")
        c4=book("Mahorat","Rupert Grin",50000,"Ildiz")
        c5=book("Yapon zobiti","Ato Hamdam",40000,"Qamar")
        lst=[c1,c2,c3,c4,c5]
        for x in range(0,5):
            lst[x].input_info()

        for x in range(0,5):
         if  lst[x].nashriyot[0].lower()>"a" and lst[x].nashriyot[0].lower()<"h":
            lst[x].output_info()
            print()

    except Exception as ex:
        print(ex)

kitob()







        



        