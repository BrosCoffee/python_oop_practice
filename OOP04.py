'''
Dunder or Magic method: "__str__" and "__repr__"
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

    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.salary)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)

    def fullname(self):
        return self.first + ' ' + self.last

    def salary_raise(self):
        self.salary = self.salary * self.raise_amount

emp_1 = Employee('Raymond', 'Yang', 60000)

print(emp_1) # > Raymond Yang - Raymond.Yang@email.com
print(emp_1.__repr__()) # > Employee(Raymond, Yang, 60000)
print(emp_1.__str__()) # > Raymond Yang - Raymond.Yang@email.com