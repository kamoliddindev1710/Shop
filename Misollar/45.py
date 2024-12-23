lst=["steal","share"]
# dct={"share":3,"steal":0}
a1=3
a2=3

for x in range(len(lst)):
    if lst[x] =="share" and x%2==0:
        a1=a1-1
        a2=a2+3
        print("1 oyinchi")
    elif lst[x] =="steal" and x%2==0:
        a1=a1+3
        a2=a2-1
        print("1 oyinchi")

    elif lst[x] =="share" and x%2!=0:
        a1=a1+3
        a2=a2-1
        print("2 oyinchi")

    elif lst[x] =="steal" and x%2!=0:
        a1=a1-1
        a2=a2+3
        print("2 oyinchi")
  

print([a1,a2])

