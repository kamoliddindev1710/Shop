lst=[[1,2],[0,0,2],[7,0],[2,1,3],[7,0]]
yangi=[]
a=sum(lst[0])
for x in lst:
    natija=sum(x)
    if a<natija:
        a=natija
        yangi=x
print(yangi)