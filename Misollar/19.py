tpl=((1,2,3),(4,5),(8,9,10,11))
tpl=list(tpl)
tup=tuple()
tup=list(tup)
d=len(max(tpl))
tpl=[x for x in tpl if len(x)!=d]
tup=[ i for x in tpl for i in x ]
tup=tuple(tup)
print(tup)