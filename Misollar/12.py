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
