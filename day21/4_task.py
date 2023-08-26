# Create another class Employee with attributes salary and
# #designation and inherits the Person class. Create a method get_details in this class
#to print name, age, salary and designation of the Employee.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation
    def get_details(self):
        print("name:", self.name)
        print("age:", self.age)
        print("salary:", self.salary)
        print("designation:", self.designation)
emp = Employee("manish", 30, 20000, "software engineer")
emp.get_details()
