def kompyuter():
    try:
        class computer:
            def __init__(self,name,RAM,price,processor):
                self.nom=name
                self.ram=RAM
                self.narx=price
                self.protsessor=processor
            

            def input_info(self):
                self.nom=input("Kompyter nomini kiriting: ")
                self.ram=int(input("Kompyuter ramini kiriting: "))
                self.narx=float(input("Komputer narxini kiriting: "))
                self.protsessor=input("Kompyuter protsessorini kiriting: ")

            def output_info(self):
                print(f"kompyuter nomi {self.nom}")
                print(f"kompyuter rami {self.ram}")
                print(f"kompyuter narxi {self.narx}")
                print(f"kompyuter protsessor {self.protsessor}")


        c1=computer("hp 100",8,2000000,"core i7")
        c2=computer("Asus",5,3000000,"i3")
        c3=computer("lenovo",8,4000000,"i7")
        c4=computer("Toshiba",16,5000000,"i7")
        lst=[c1,c2,c3,c4]
        for x in range(0,5):
            lst[x].input_info()

        for x in range(0,5):
         if  lst[x].ram>4 and lst[x].ram<16:
            lst[x].output_info()
            print()

    except Exception as ex:
        print(ex)

kompyuter()

