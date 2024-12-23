class Dori:
    def __init__(self,name="",tan_narxi=0,srok=0,miqdor=0,kompaniya_nomi="",tasir=""):
        self.nom=name
        self.__tan_narxi=int(tan_narxi)
        self.__sotlish_narxi=self.__tan_narxi*2
        self.muddat=srok
        self.miqdor=int(miqdor)
        self.kompaniya_nomi=kompaniya_nomi
        self.tasir=tasir
    
    def add_product(self,new_miqdor):
        self.miqdor+=new_miqdor

    def sell_product(self,new_miqdor):
        self.miqdor-=new_miqdor

    def get_sotlish_narxi(self):
        return self.__sotlish_narxi

    def show_info(self):
        print(f"""
Dori nomi {self.nom}
Sotilish narxi {self.__sotlish_narxi} so'm
Muddati {self.muddat}
MIqdori {self.miqdor}
Kompaniya nomi {self.kompaniya_nomi}
T'asiri {self.tasir}""")

    
class Apteka:
    def __init__(self,name):
        self.nom=name
        self.kassa=100000
        self.dori_royxat={}
    
    def add_dori(self, obj: Dori):
        if obj.nom in self.dori_royxat:
            self.dori_royxat[obj.nom].add_product(obj.miqdor)
            print(f"Mahsulot yangilandi: {obj.nom}, umumiy miqdor: {self.dori_royxat[obj.nom].miqdor}")
        else:
            self.dori_royxat[obj.nom] = obj
            print(f"Mahsulot qo'shildi: {obj.nom}")

    def sale_dori(self, name, miqdor):
        if name in self.dori_royxat:
            dori = self.dori_royxat[name]
            num = int(input("Sotib olishni xohlasizmi ha->[1] yo'q->[0] "))
            if num not in [0, 1]:
                print("Faqat 1 yoki 0 ni tanlang!")
                return
            if dori.miqdor >= miqdor and num == 1:
                self.pul(dori, miqdor)
                dori.sell_product(miqdor)
                print(f"{miqdor} dona {dori.nom} sotildi. Qolgan miqdor: {dori.miqdor}")
            elif dori.miqdor < miqdor and num == 1:
                print(f"Yetarli {dori.nom} yo'q. Faqat {dori.miqdor} dona mavjud.")
        else:
            print(f"{name} do'konda topilmadi.")


    def delete_dori(self):
        if len(self.dori_royxat):
            self.dori_royxat = {key: value for key, value in self.dori_royxat.items() if value.muddat >= 2024}
            print("Eski muddatli dorilar o'chirildi.")
        else:
            print("Dorixonada hech qanday dori mavjud emas.")


    def show_dorilar(self):
        if len(self.dori_royxat):
            for dori in self.dori_royxat.values():
                dori.show_info()
        else:
            print("Dori mavjud emas")

    def pul(self, obj: Dori, amount):
        if amount < 0:
            print("Noto'g'ri miqdor kiritildi!")
            return
        self.kassa += obj.get_sotlish_narxi() * amount

    def apteka_kassa(self):
         print(f"Kassa balans {self.kassa}")

    def drug_to_pain(self, kasal):
        found = False
        for dori in self.dori_royxat.values():
            if kasal.lower() in dori.tasir.lower():
                dori.show_info()
                found = True
        if not found:
            print("Bunday kasallik uchun dori mavjud emas.")


    def show_apteka(self):
        print(f"""
Apteka nomi: {self.nom}
Kassa puli :{self.kassa}""")


apteka_name=input("Apteka nomini kiriting: ")
apteka1=Apteka(apteka_name)
while True:
    print("[1] Add drugs")
    print("[2] Sale drugs")
    print("[3] Delete drugs")
    print("[4] Show drugs")
    print("[5] Medicine to pain")
    print("[6] Show Pharmacy info")
    print("[0] Exit")

    try:
        vary=int(input("Tanlang: "))
    except:
        print("Iltimos butun son bering ")

    if vary==1:
        name=input("Dorini nomini kiriting: ")
        tan_narx=float(input("Dorining tannarxini kiriting: "))
        muddat=int(input("Dorining muddatini kiriting: "))
        amount=int(input("Dorining miqdorini kiriting (dona): "))
        company_name=input("Kompaniya nomini kiriting: ")
        drug_affect=input("Dorining ta'sir joyini kiriting: ")
        d1=Dori(name,tan_narx,muddat,amount,company_name,drug_affect)
        apteka1.add_dori(d1)

    elif vary==2:
        name=input("Dori nomini kiriting: ")
        amount=int(input("Miqdorini kiriting: "))
        apteka1.sale_dori(name,amount)

    elif vary==3:
        apteka1.delete_dori()
    
    elif vary==4:
        apteka1.show_dorilar()
        
    elif vary==5:
        tasir=input("Qayeringiz uchun dori kerak ")
        apteka1.drug_to_pain(tasir)


    elif vary==6:
        apteka1.apteka_kassa()


    elif vary==0:
        break



