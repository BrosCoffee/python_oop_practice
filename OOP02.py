'''
When working with Class, there are three methods:
1. Regular method: automatically pass the instances as the first argument: "self"
2. Class method: automatically pass the class as the first argument: "cls"
   Also be used as the "Alternative Constructor"
3. Static method: don't pass anything automatically; they perform like normal functions,
   except they have some logical connections with the class.

Youtube:
Corey Schafer Python OOP Tutorial 3: classmethods and staticmethods:
https://www.youtube.com/watch?v=rq8cL2XMM5M&t=211s
'''

class Employee:

    raise_amount = 1.01
    emp_num = 0
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        self.email = first + '.' + last + '@email.com'
        Employee.emp_num += 1 # Increment by 1 whenever a new emp was created

    def fullname(self):
        return self.first + ' ' + self.last

    def salary_raise(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise_amot(cls,amount):
        Employee.raise_amount = amount

    @classmethod
    def from_string(cls,emp_name_str):
        first, last, salary = emp_name_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime

my_date1 = datetime.date(2019,8,8)
my_date2 = datetime.date(2019,8,11)
my_date3 = datetime.date(1989,2,19)

print(Employee.is_workday(my_date1))
print(Employee.is_workday(my_date2))
print(Employee.is_workday(my_date3))

# emp_1 = Employee('Raymond', 'Yang', 60000)
# emp_2 = Employee('Meliza', 'Anzures', 80000)
#
# emp_3_str = "Randy-Yang-70000"
# emp_4_str = "Michael-Jordan-40000"
# emp_5_str = "Jeremy-Lin-45000"
#
# emp_3 = Employee.from_string(emp_3_str)
# emp_4 = Employee.from_string(emp_4_str)
# emp_5 = Employee.from_string(emp_5_str)
#
# print(emp_3.email)
# print(emp_4.email)
# print(emp_5.email)
# print(Employee.emp_num)