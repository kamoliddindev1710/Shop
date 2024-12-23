def friend_website():
    try:
        class yuser:
            def __init__(self,name="",age=0,animal="",fruit="",hobby="",nation="",IQ=0):
                self.ism=name
                self.yosh=age
                self.jonzot=animal
                self.meva=fruit
                self.hobbi=hobby
                self.millat=nation
                self.aykyu=IQ

            def set_info(self):
                self.ism=input("Ismingizni kiriting: ")
                self.yosh=int(input("Yoshingizni kiriting: "))
                self.jonzot=input("Sevimli jonzotingizni kiriting: ")
                self.meva=input("Sevimli mevangizni kiriting: ")
                self.hobbi=input("Sevimli hobbingizni kiriting: ")
                self.millat=input("Millatingizni kiriting: ")
                self.aykyu=int(input("IQingizni kiriting: "))

            def get_info(self):
                print(f"Sizning ismingiz->{self.ism}\nYoshingiz ->{self.yosh}\nSevimli jomzotingiz->{self.jonzot}\nSevimli mevanigz->{self.meva}\nHobbingiz->{self.hobbi}\nMillatingiz->{self.millat}")

            def get_score(self):
                if self.aykyu<85:
                    print(f"{self.ism} sizning IQ iz qoniqarli")
                elif self.aykyu>85 and self.aykyu<135:
                    print(f"{self.aykyu} Zo'r")
                else :
                    print(f"{self.aykyu} Qoyil juda zo'r")

        num_user=int(input("Nechta ishtirokchi kiritmochisiz: "))
        lst=[]
        for x in range(0,num_user):
            useeer=yuser()
            useeer.set_info()
            lst.append(useeer)

        for x in range(0,num_user):
            lst[x].get_info()
            lst[x].get_score()

    except Exception as ex:
        print(ex)



friend_website()
