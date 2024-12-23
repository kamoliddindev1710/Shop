class car:
    def __init__(self,engine=False,benzin=20,benzin_bak=40,masofa=0):
        self.motor=engine
        self.__benzin=benzin
        self.bak=benzin_bak
        self.masofa=masofa

    def engine_on(self):
        a=int(input("Motorni yoqmoqchimisiz ha->[1],yo'q->[0] "))
        if a==1:
            if not self.motor:
                self.motor=True
                print("Motor yondi🚒")
            else:
                 print("Mashina allaqachon yoqilgan ")
        else:
             print("Mashina yurmadi")
             exit()

    def yur(self):
        if not self.motor:
             self.engine_on()
        yur=int(input("Qancha masofa yurmoqchisiz (km):"))
        kerakli_benzin=yur//10 #10 km uchun 1 litr benzin
        if kerakli_benzin >self.__benzin:
                print("Benzin yetarli emas ")
                b=int(input("Benzin quymoqchimisz:ha->[1],yo'q->[0] "))
                if b==1:
                    self.benzin_quy()
                elif b==0:
                    print("Mashina yurdi🏎️")
        else:
            print("Benzin yetarli\n Yuryapmiz")
            self.__benzin-=kerakli_benzin
            self.masofa+=yur
            print(f"Mashina {yur} km masofa bosdi. Qolgan benzin: {self.__benzin} litr.")



    def engine_off(self):
        if self.motor:
            a=int(input(("Motorni o'chirmoqchimisiz:ha->[1],yo'q->[0] ")))
            if a==1:
                self.motor=False
                print("Motor ochirildi ")
            else:
                 print("Motor o'chirilmadi")
                 self.yur()
        else :
            print("Motor allaqachon o'chirilgan ")
            
    def benzin_quy(self):
            a=int(input("Qancha benzin quymoqchisiz: 100km----10l "))
            if  a+self.__benzin>self.bak:
                print(f"Benzin miqdori ko'p,nima qilasiz shunchani?\nTo'ldirish uchun {self.bak-self.__benzin} yetarli ")
                a=int(input("Yana kiriting: "))
            
            if a+self.__benzin<=self.bak:
                 self.__benzin+=a
                 print(f"Bu yetarli,shuncha quydik\nMashina yuryapti\nBenzin  {self.__benzin} ta  mavjud  ")
            else:
                 print("EEE palakat bola ekansan 🤬🤬 ")
        
a1=car()
a1.yur()
a1.engine_off()