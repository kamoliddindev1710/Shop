class Product:
    def __init__(self,name,count,price):
        self.nom=name
        self.miqdor=count
        self.narx=price
        

    def add_product(self,amount):
        self.miqdor+=amount
       
    def sale_product(self,amount):
        if self.miqdor>=amount:
            self.miqdor-=amount
            print(f"{self.nom}dan {amount} ta sotildi")
        else:
            print(f"{self.nom}dan {amount} yetarli emas")


    def update_price(self,new_price):
        self.narx=new_price

    def get_info(self):
        print(f"""
Mahsulot nomi:{self.nom}
Mahsulot miqdori:{self.miqdor} kg
Mahsulot narxi:{self.narx}
""")

class Shop:
    def __init__(self,name="",location="",open_time="",close_time=""):
        self.nom=name
        self.manzil=location
        self.ochilish_vaqti=open_time
        self.yopilish_vaqti=close_time
        self.products=[]

    def add_product(self,product: Product):
        for p in self.products:
            if p.nom.lower() == product.nom.lower():
                p.add_product(product.miqdor)
                print(f"Mahsulot yangilandi: {product.nom}, umumiy miqdor: {p.miqdor}")
                return
        self.products.append(product)
        print(f"Mahsulot qo'shildi: {product.nom}")
       

    def sale_product(self,product_name,count):
        for p in self.products:
            if p.nom.lower() == product_name.lower():
                if p.miqdor >= count:
                    p.sale_product(count)
                    print(f"{count} dona {p.nom} sotildi. Qolgan miqdor: {p.miqdor}")
                    return
                else:
                    print(f"Yetarli {p.nom} yo'q. Faqat {p.miqdor} dona mavjud.")
                    return
        print(f"{product_name} do'konda topilmadi.")

    def update_price(self,income_name,new_price):
       for p in self.products:
            if p.nom.lower() == income_name.lower():
                p.update_price(new_price)
                print(f"{p.nom} mahsulotining narxi yangilandi: {new_price} so'm")
                return
       print(f"{income_name} do'konda topilmadi.")

    def get_info(self):

        print(f"""
Do'kon nomi: {self.nom}
Manzil: {self.manzil}
Ish vaqti: {self.ochilish_vaqti} - {self.yopilish_vaqti}
Mahsulotlar ro'yxati:
""")
        for product in self.products:
            product.get_info()


shop1=Shop("Anhor","Toskent","08:00","21:00")

while True:
    print("[1]  Add product")
    print("[2]  Sale product")
    print("[3]  Udate product_price")
    print("[4]  Show  product")
    print("[0]  Exit")

    try:
        vary=int(input("Tanlang: "))
    except:
        print("Iltimos butun son bering ")
        
    if vary==1:
        name=input("Nomini kiriting: ")
        miqdor=int(input("Miqdorini kiriting: "))
        narx=float(input("Narxini kiriting: "))
        p1=Product(name,miqdor,narx)
        shop1.add_product(p1)
    elif vary==2:
        name=input("Nomini kiriting: ")
        miqdor=int(input("Miqdorini kiriting: "))
        shop1.sale_product(name,miqdor)
    elif vary==3:
        name=input("Nomini kiriting: ")
        narx=float(input("Narxini kiriting: "))
        shop1.update_price(name,narx)
    elif vary==4:
        shop1.get_info()
    elif vary==0:
        break






