def kinolar():
 try:
    with open("kino.txt",encoding="utf-8") as f:
        lst=[x for x in f.read().split('\n')]
        for i in lst:
            if "2000" < i.split(',')[-2]:
                print(i.split(",")[1],i.split(",")[-1])
 except Exception as ex:
    print(ex)

    
kinolar()