
def mahsulot(son1,ls ):
    ls2=[]
    for x in range(len(ls)):
        ls2.append(ls[x]["price"])

    ls2=sorted(ls2,reverse=True)

    for x in range(len(ls)):
        if ls[x]["price"] in ls2[:b]:
           print(ls[x])


lst=[]
a=int(int(input("Nechta mahsulot kiritimoqchisiz: ")))
for x in range(a):
    dct={}
    dct["name"]=input("Nomini kiriting: ")
    dct["price"]=int(input("Narxini kiriting: "))
    lst.append(dct)
b=int(input("Soningizni kiriting: "))
mahsulot(b,lst)
