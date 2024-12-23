import pymysql

class MSQL:
    def __init__(self):
           self.ConnectDB()
           self.CreateDB()
           self.CreateTB()
     
    def ConnectDB(self):
           self.db=pymysql.connect(
                 user ="root",
                 password="1234",
                 host="localhost"
           )
           self.cursor=self.db.cursor()

    def CreateDB(self):
          self.cursor.execute("CREATE DATABASE IF NOT EXISTS School")
          self.cursor.execute("USE School")

    # def CreateTB(self):
    #       self.cursor.execute('''CREATE TABLE  IF NOT EXISTS teachers(
    #                           name VARCHAR(50),
    #                           surname VARCHAR(50),
    #                           salary real,
    #                           experience int,
    #                           branch VARCHAR(50)
    #                           )''')

    def CreateTB(self):
          self.cursor.execute('''CREATE TABLE  IF NOT EXISTS students(
                              name VARCHAR(50),
                              surname VARCHAR(50),
                              monthly_pay real,
                              course_duration int,
                              branch VARCHAR(50)
                              )''')
          
    def InsertTB2(self,name,surname,monthly_pay,course_duration,branch):
          self.cursor.execute(f'''INSERT INTO students VALUES("{name}","{surname}",{monthly_pay},{course_duration},"{branch}")''')
          self.db.commit()

    # def FirstQuery(self):
    #       self.cursor.execute("SELECT * from teachers order by salary")
    #       natija=self.cursor.fetchall()
    #     #   print(natija)
    #       for x in natija:
    #             print(x)

    # def SecondQuery(self):
    #       self.cursor.execute("SELECT * from teachers order by salary ,experience desc")
    #       natija=self.cursor.fetchall()
    #     #   print(natija)
    #       for x in natija:
    #             print(x)

    # def ThirdQuery(self):
    #       self.cursor.execute("Update teachers set salary=10 order by salary desc limit 1  ")
    #       self.db.commit()
    #       natija=self.cursor.fetchall()
    #       print(natija)
    #     #   for x in natija:
    #     #         print(x)

    # def ForhtQuery(self):
    #       self.cursor.execute("Update  teachers set branch ='XADRA' order by experience desc limit 1")
    #       self.db.commit()
    #     #   natija=self.cursor.fetchall()
    #     # #   print(natija)
    #     #   for x in natija:
    #     #         print(x)

    # def FifthQuery(self):
    #       self.cursor.execute("SELECT * from teachers order by surname")
    #       natija=self.cursor.fetchall()
    #     #   print(natija)
    #       for x in natija:
    #             print(x)

    # def SixQuery(self):
    #       self.cursor.execute("SELECT * from students  order by monthly_pay desc ")
    #       natija=self.cursor.fetchall()
    #     #   print(natija)
    #       for x in natija:
    #             print(x)

    def SeventhQuery(self):
          self.cursor.execute("SELECT * from teachers order by salary ,experience dec")
          natija=self.cursor.fetchall()
        #   print(natija)
          for x in natija:
                print(x)
sql=MSQL()







# for i in range(int(input("NEchta xodim kiritasiz: "))):
    #  sql.InsertTB2(input("Ism kiriting: "),input("Familya kiriting: "),input("Maoshni kiriting: "),input("Tajriba kiriting: "),input("Filialni kiriting: "))
    
# for x in range(7):
    #   sql.InsertTB2(input("Ism kiriting: "),input("Familya kiriting: "),float(input("Oylik to'lovni kiriting: ")),int(input("Muddatni kiriting: ")),input("Filialni kiriting: "))

# sql.FirstQuery()
sql.SecondQuery()

# sql.ThirdQuery()

# sql.ForhtQuery()
# sql.FifthQuery()
# sql.SixQuery()