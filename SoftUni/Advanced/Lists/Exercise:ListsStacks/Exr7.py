# 1.
# numbers = [1,2,3,4,5]
# result = list(map(lambda x: x * 3, numbers))
# print(result)
# 2.
# num1 = [1,2,3]
# num2 = [4,5,6]
# num3 = [7,8,9]
# result = list(map(lambda x, y, z: x + y + z, num1, num2, num3))
# print(result)
# 3.
# lst = ['Red', 'Green', 'Black']
# results = list(map(list, lst))
# print(results)
# 4.
# import math
# numbers = [10,20,30,40,50]
# result = list(map(lambda x:math.sqrt(x), numbers))
# for i in range(0, len(result)):
#     print(f'{result[i]:.2f}')
#5.
# def compareLists(l1, l2):
#     return l1 + l2, l1 - l2
# lst = [6, 5, 3, 9]
# lst1 = [0, 1, 7, 7]
# result = map(compareLists, lst, lst1)
# print(list(result))

class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)