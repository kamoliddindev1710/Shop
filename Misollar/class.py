class Account:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.__balance=0

    def get_id (self):
        print(f" {self.id}")

    def get_name(self):
        print(f" {self.name}")

    def get_balance(self):
        print(f" Balans {self.balance}")

    def amount(self,miqdor:int):
        self.balance +=miqdor
        print(f" Balans: {self.balance}")

    def chiqar(self,ol:int):
        if self.balance >=ol:
            print(f"{ol} yechdingiz")
            print(f"Sizda {self.balance - ol} qoldi")
            self.balance-=ol
        else :
            print("Sizda yetarli mablag yoq")
    def otkaz(self,another,ol:int):
        if self.balance >=ol:
            another.balance+=ol
            print("O'tkazildi ")
            self.balance-=ol


acoount1=Account(1000,"Ali")
acoount2=Account(1002,"Vali")

acoount1.get_id()
acoount1.get_name()
acoount1.get_balance()
pul=int(input("PUl kiriting: "))
acoount1.amount(pul)
# pul2=int(input("Yechmoqchi pulizi kiriitng: "))
# acoount1.chiqar(pul2)
otkazma=int(input("Qancha pul otkazmoqchisz "))
acoount1.otkaz(acoount2,otkazma)
acoount2.get_balance()
acoount2.__balance+=500
print(acoount2.__balance)