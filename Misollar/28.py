def nechta(son1:int,son2:int):
    count=0
    bolinma=son1
    print(f"{son1}->",end=" ")
    while bolinma>son2*2:
        count+=1
        bolinma/=2
        if bolinma>son2*2:
           print(f"{bolinma}->",end=" ")
        else :
           print(bolinma)
    print(f"{count} ta ")
    

a=int(input("1- son kiriting: "))
b=int(input("2- son kiriting:  "))
if a>=b*2:
   nechta(a,b)
else :
   print("Qaytadan kiriting ")