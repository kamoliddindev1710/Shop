def ishchi():
    try:
        class employee:
            def __init__(self,surname,position,salary):
                self.familya=surname
                self.lavozim=position
                self.maosh=salary

            def get_info(self):
                return f"""
        Familiya :{self.familya}
        Lavozizmi :{self.lavozim}"""

        class enterprise_employee(employee):
            def __init__(self, surname="", position="", salary=0,rating=0):
                super().__init__(surname, position, salary)
                self.reyting=rating

            def set_info(self):
                self.familya=input("Familyangizni kiriting: ")
                self.lavozim=input("Lavozimingizni kiriting: ")
                self.maosh=int(input("Maoshinigizni kiriting: "))
                self.reyting=int(input("Reytingingizni kiriting: "))

            def set_salary(self):
                if self.reyting >=60 and self.reyting<75:
                    self.maosh=(self.maosh*120)//100
                elif self.reyting >=75 and self.reyting<90:
                    self.maosh=(self.maosh*140)//100
                elif self.reyting>=90 and self.reyting<=100:
                    self.maosh=(self.maosh*160)//100
                
            def get_info(self):
                self.set_salary()
                return f"""
        {super().get_info()}
        Oylik : {self.maosh}
        Reyting: {self.reyting}"""
                
        a1=enterprise_employee()
        a2=enterprise_employee()
        a3=enterprise_employee()
        a4=enterprise_employee()
        a5=enterprise_employee()
        lst=[a1,a2,a3,a4,a5]
        for x in lst:
            x.set_info()

        for x in lst:
            print(x.get_info())

    except Exception as ex:
        print(ex)

ishchi()