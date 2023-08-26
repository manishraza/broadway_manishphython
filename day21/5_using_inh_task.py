class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        self.display_details()
        print("Salary:", self.salary)
        print("Designation:", self.designation)


# Creating an Employee object and displaying details
emp = Employee("John Doe", 30, 50000, "Software Engineer")
emp.get_details()
