# from array import *
# data={}
# data = {1: ["161E90 ","Raman",41,56000],
#          2: ["161F91", "Himadri", 38,67500],
#          3: ["161F99","Jaya",51,82100],
#          4: ["171E20","Tejas",30,55000],
#          5: ["171G30","Ajay",45,44000]
#          }
import pandas as pd

data={}
class Employee:
    def __init__(self,id,name,age,salary):
       self.id=id
       self.name=name
       self.age=age
       self.salary=salary

    def disp(self):
        print(self.id)
        print(self.name)
        print(self.age)
        print(self.salary)

    def to_dict(self):
        headers = ['Employee ID', 'Name', 'Age', 'Salary (PM)']
        for i in range(0,len(headers)):
            return {
                i: [self.id,self.name,self.age,self.salary],
            }

    # def sort_age(self):
    #     self.sortAge = sorted(self.data.items(), key=lambda x: x[2])
    #     for key, value in self.sortAge.items():
    #         print(f'{value[0]: <15}{value[1]: <15}{value[2]: <15}{value[3]}')
    #     # for i in self.sortAge:
	#     #     print(i[2])

e1=Employee("161E90","Raman",41,56000)
e2=Employee("161F91","Himadri",38,67500)
e3=Employee("161F99","Jaya",51,82100)
e4=Employee("171E20","Tejas",30,55000)
e5=Employee("171G30","Ajay",45,44000)
e1.disp()
res1=e1.to_dict()
res2=e2.to_dict()
res3=e3.to_dict()
res4=e4.to_dict()
print(res1,res2,res3,res4)
# headers = ['Employee ID', 'Name', 'Age', 'Salary (PM)']
# print(f'{headers[0]: <15}{headers[1]: <15}{headers[2]: <15}{headers[3]}')
# for key, value in data.items():
#     print(f'{value[0]: <15}{value[1]: <15}{value[2]: <15}{value[3]}')

# val=1
# while val:
#     print("------MENU------")
#     print("1. Sort by AGE")
#     print("2. Sort by NAME")
#     print("3. Sort by SALARY")
#     print("4. Exit")
#     val=int(input("Enter your choice: "))
#     if val==1:
#         print(e1.sort_age())
#     elif val==2:
#         print(e2.sort_name())
#     elif val==3:
#         print(e3.sort_salary())
#     elif val==4:
#         exit()
#     else:
#         exit()
