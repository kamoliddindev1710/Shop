def top(son:str):
    count=0
    if son[:1]=='0':
     for x in son:
        if x=='0':
            count+=1
        else :
            print("Xato ")
            break
    print(f"Boshida {count} ta 0 bor ")

a=input("Son kiriting: ")
top(a)