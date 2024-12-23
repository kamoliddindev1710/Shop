def qurilma():
    try:
        with open("qurilma.txt",encoding="utf-8") as f:
            lst=[x for x in f.read().split('\n')]
            lst2=['06','07','08']
            for  l in lst:
                if l.split(",")[-2][3:5] in lst2:
                    print(l)
    except Exception as ex:
        print(ex)
        
    
qurilma()