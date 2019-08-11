'''
Assuming there are Developer and Manager positions in a company.
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

class Developer(Employee):
    raise_amount = 1.03 # Override the raise_amount from 1.01 to 1.03
    # Thus, regular employee and developer have different raise amount

    def __init__(self, first, last, salary, prog_lang):
        super().__init__(first, last, salary)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, salary, employees = None):
        super().__init__(first, last, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Raymond', 'Yang', 60000, "Python")
# dev_1 = Employee('Raymond', 'Yang', 60000)
dev_2 = Developer('Meliza', 'Anzures', 80000, "Java")

mgr_1 = Manager('Barak', 'Obama', 100000, [dev_1])

print(dev_1.email)
print(dev_1.prog_lang)
print(mgr_1.fullname())
print(mgr_1.print_emps())
mgr_1.add_emp(dev_2)
print(mgr_1.print_emps())



# print(dev_1.salary)
# dev_1.salary_raise()
# print(dev_1.salary)