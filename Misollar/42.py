def kitob():
    try:
        class book:
            def __init__(self,name,author,year):
                self.nom=name
                self.muallif=author
                self.yil=year

        class book_store(book):
            def __init__(self, name, author, year,price):
                super().__init__(name, author, year)
                self.narx=price
                
            def get_discout(self):
                if (2024-self.yil)>=5:
                    return f"""
        {self.nom}
        {self.muallif}
        {self.yil}
        {(self.narx*80)//100}"""
                else:
                    return f"""
        {self.nom}
        {self.muallif}
        {self.yil}
        {self.narx}"""
                
        a1=book_store("O'tgan kunlar","Abdulla Qodiriy",2018,100000)
        a2=book_store("Mahorat","Rupert Grin",2022,80000)
        a3=book_store("Yapon zobiti","Ato Hamdam",2019,50000)
        a4=book_store("Shirin qovunlar mamlakati","Xudoyberdi To'xtaboyev",2017,30000)
        a5=book_store("Yo'qchilik va to'qchilik","Ernest Hemingey",1980,25000)
        lst=[a1,a2,a3,a4,a5]
        for x in range(5):
            print(lst[x].get_discout())
    
    except Exception as ex:
        print(ex)
kitob()