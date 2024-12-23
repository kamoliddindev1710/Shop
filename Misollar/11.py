for x in range(10,999):
    a=x//100
    b=(x//10)%10
    c=x%10
    if a==b and a!=c or a==c and a!=b:
        print(x)