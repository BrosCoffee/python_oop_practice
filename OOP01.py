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

emp_1 = Employee('Raymond', 'Yang', 60000)
emp_2 = Employee('Meliza', 'Anzures', 80000)

print("emp_1's email: {}".format(emp_1.email))
print("emp_2's fullname: {}".format(emp_2.fullname()))

print("emp_2's origin salary: {}".format(emp_2.salary))
print("company's annual raise: {}".format(Employee.raise_amount))
emp_2.salary_raise() # Apply the company's annual raise
print("emp_2's salary after raise: {}".format(emp_2.salary))

print("Total amount of emp: {}".format(Employee.emp_num))
Employee.set_raise_amot(1.03) # change the annual raise to 1.03%
print("Annual raise after change: {}".format(Employee.raise_amount))
emp_1.salary_raise()
print("emp_1's salary after the new raise: {}".format(emp_1.salary))


# class Calculator:
#     def __init__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#     def multiple(self):
#         return self.num1 * self.num2
#
#     def addition(self):
#         return self.num1 + self.num2
#
# number1 = Calculator(2,5).multiple()
# number2 = Calculator(7,2).addition()
# print(number1 if number1 > number2 else number2)