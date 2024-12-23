a=str(input("Tug'ilgan sanangizni  - bilan kiriting: "))
b=str(input("Tug'ilgan kuningizni  - bilan kiriting: "))
c=b[0:2]+a[2:5]+b[5:]
d=a[0:2]+b[2:5]+a[5:]
print(c,d,sep="\n")