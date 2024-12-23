import pymysql

class MYSQl:
    def __init__(self):
        self.ConnectDB()
        self.CreateDB()
        self.CreateTB()

    def ConnectDB(self):
        self.db=pymysql.connect(
            user="root",
            password="1234",
            host="localhost"
        )
        self.cursor=self.db.cursor()

    def CreateDB(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS work")
        self.cursor.execute("USE work")

    def CreateTB(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Staff(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            first_name VARCHAR(50),
                            second_name VARCHAR(50),
                            phone_number VARCHAR(50),
                            job_id VARCHAR(50),
                            salary REAL )""")

    def InsertTB(self):
        self.cursor.execute('''INSERT INTO Staff(first_name,second_name,phone_number,job_id,salary) VALUES
                            ("Steven","King","+998941234567","AD_PRES",24000),
                            ("Neena","Kochnar","+998941244668","AD_VP",17000),
                            ("Lex","De Haan"," +998941244669","AD_PRES",17000),
                            ("Aleksandr","Hunold","+998941244670","IT_PROG",11000),
                            ("Bruce","Ernest","+998941244671","IT_PROG",8000),
                            ("David","Austin","+998941244871","IT_PROG",6800),
                            ("Valli","Patabella"," +998941244975","IT_PROG",6800),
                            ("Diana","Lorentz","+998946254976","IT_PROG",6200),
                            ("Nancy","Greenberg","+998946255946","FI_MGR",12000),
                            ("Daniel","Faviet","+998946755948","FI_ACCOUNT",9000),
                            ("John","Chen","+998946756953","FI_ACCOUNT",8200),
                            ("Ismael","Sciarra","+998946856983","FI_ACCOUNT",7700),
                            ("Den","Raphaely","+998946886983","PU_MAN",11000),
                            ("Aleksandr","Kahoo","+998946888493","PU_CLERK",3100)
''')
        self.db.commit()
    
    def FirstQuery(self):
        self.cursor.execute("SELECT first_name , second_name   from Staff")
        result=self.cursor.fetchall()
        for i,y in result:
            print(f"|Ism {i} | Familiya {y}|")

    def SecondQuery(self):
        self.cursor.execute("Select first_name ,second_name,salary from Staff where job_id ='IT_PROG'")
        result=self.cursor.fetchall()
        print("Ism     Familiya      Maosh")
        for i,x,y in result:
            print(f"{i} | {x} | {y} ")
    
    def ThirdQuery(self):
        self.cursor.execute("SELECT job_id,salary from Staff where salary BETWEEN 5000 and 20000")
        result=self.cursor.fetchall()
        for x,y in result:
            print(f"Job_Id {x} | Maosh {y}")

    def FourthQuery(self):
        self.cursor.execute("Select * from Staff where phone_number like '%6983' ")
        result=self.cursor.fetchall()
        for x in result:
            print(x)

    def FifthQuery(self):
        self.cursor.execute("SELECT SUM(SALARY) FROM STAFF")
        result=self.cursor.fetchone()
        print(f"Jami {result[0]} ")

    def SixthQuery(self):
        self.cursor.execute("Select * from Staff where job_id='IT_PROG' order by salary desc ")
        result=self.cursor.fetchone()
        print(result)

    def SeventhQuery(self):
        self.cursor.execute("Select * from Staff where salary>(select sum(salary)/14 from Staff)")
        result=self.cursor.fetchall()
        for x in result:
            print(x)

    def EigthQuery(self):
        # self.cursor.execute("SELECT * FROM Staff WHERE salary > (SELECT SUM(salary)/COUNT(*) FROM STAFF where job_id='IT_PROG')")
        self.cursor.execute("SELECT * from Staff where salary >(SELECT avg(salary) from Staff where job_id='IT_PROG')")
        result=self.cursor.fetchall()
        for x in result:
            print(x)

# if __name__ == "__main__":
#     sql = MYSQl()

sql=MYSQl()
# sql.InsertTB()
# sql.FirstQuery()
# sql.SecondQuery()  
# sql.ThirdQuery()
# sql.FourthQuery()
# sql.FifthQuery()
# sql.SixthQuery()
# sql.SeventhQuery()
sql.EigthQuery()