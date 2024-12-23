import pymysql

class MySQL:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db = pymysql.connect(
            user = "root",
            password = "yusuf6451895",
            host = "localhost"
        )
        self.cursor = self.db.cursor()

    def CreateDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS kitobcha")
        self.cursor.execute("USE kitobcha")
    
    def CreateTB(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            ism VARCHAR(50) DEFAULT 'Ali',
                            age INT,
                            salary REAL
                            )""")
    
    # def InsertTB(self):
    #     self.cursor.execute('''INSERT INTO user(ism, age, salary) VALUES("Aziz", 23, 45.6320)''')
    #     self.db.commit()

    def InsertTB2(self, name, age, salary):
        self.cursor.execute(f'''INSERT INTO user(ism, age, salary) VALUES("{name}",{age},{salary})''')
        self.db.commit()
    
    def FirstQuery(self):
        self.cursor.execute("UPDATE user SET salary=salary*2 WHERE ism LIKE 'a%'")
        self.db.commit()

    def SecondQuery(self):
        self.cursor.execute("SELECT id, ism FROM user WHERE salary > 20")
        natija = self.cursor.fetchall() # [(),(),(),()]
        # natija = self.cursor.fetchmany(2)
        # natija = self.cursor.fetchone()
        # print(natija)

        for i in natija:
            print(i)

sql = MySQL()
# sql.InsertTB()
# sql.InsertTB2("Akmal", 13, 1000)
# for i in range(int(input("NECHTA DATA KIRITASIZ: "))):
#     sql.InsertTB2(input("Ism: "), int(input("Yosh: ")), float(input("Oylik: ")))
# sql.FirstQuery()
sql.SecondQuery()