def kinolar():
    try:
        with open("kino.txt",encoding="utf-8") as f:
            lst=[x for x in f.read().split('\n')]
            lst=sorted(lst,key=lambda i : i.split(',')[-2])
            for l in lst:
                print(l)
    except Exception as x:
        print(x)
    

kinolar()
