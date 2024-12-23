# class Solution(object):
#     def twoSum(self, nums: list, target:int): 
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j]+nums[i]==target:
#                     return[i,j]
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
# a1=Solution()
# print(a1.twoSum([2,7,11,5],9))

# import datetime
# print(datetime.datetime.today())
# class drug:
#     def __init__(self,name,date):
#         self.nom=name
#         self.sana=date

#     def get_time(self):
#         return self.sana[0:2]+


# import random
# class Book_store:
#     def __init__(self,customer_name,customer_age,book_name,book_price):
#         self.ism=customer_name
#         self.yosh=customer_age
#         self.kitob_nom=book_name
#         self.kitob_narx=book_price

#     def get_price(self):
#         print( self.kitob_narx -(self.kitob_narx*self.yosh)//100)

# a1=Book_store("Asadbek",20,"O'tgan kunlar",randint(20000,100000))
# a1.get_price()


# class Transport:
#     def __init__(self,model,fuel,max_speed):
#         self.tip=model
#         self.yoqilgi=fuel
#         self.tezlik=max_speed

#     def get_info(self):
#         print(f"""Transport info:
#                 Model:{self.tip}
#                 Fuel:{self.yoqilgi}
#                 Max_speed:{self.tezlik}""")

# a1=Transport("Bmw",100,305)
# a1.get_info()


# class Transpot16:
#     def __init__(self,name,max_speed):
#         self.tip=name
#         self.tezlik=max_speed
        
    

# class Car(Transpot16):
#     def __init__(self,consumption,ism,tezlik_max):
#         self.sarflash=consumption
#         super().__init__(ism,tezlik_max)
        

#     def get_info(self):
#         print(f"Mashina tipi:{self.tip}")
#         print(f"Mashina tezligi:{self.tezlik}")
#         print(f"Mashina sarflashi:{self.sarflash}")
#         print(f"{self.tezlik*self.sarflash}")

# a1=Car(10,"Bmw",315)
# a1.get_info()



class population:
    def __init__(self,name,age,exs):
        self.ism=name
        self.yosh=age
        self.jins=exs
    
    def get_info(self):
        if self.yosh>50:
            if self.jins.lower()=="erkak":
                print(f"Janob {self.ism}")

            else:
                print(f"Xonim {self.ism}")


a1=population("Asadbek",56,"Erkak")
a2=population("Katta Xola",57,"Ayol")
a1.get_info()
a2.get_info()

        
       
        
    