import json
import os
filename = "student.json"
def create_student():
    id = input("enter the student id ")
    name = input("enter the student name ")
    age = input("enter the student age ")
    address = input("enter the student address ")
    student = dict(id=id, name=name, age=age, address=address)
    if not os.path.exists(filename):
     with open(filename, "w") as fp:
        data = json.dumps([student], indent=2)
        fp.write(data)

    else:
        with open (filename, "r+") as fp:
            students = json.loads(fp.read())
            students.append(student)
            fp.seek(0)
            data = json.dumps(students, indent=2)
            fp.write(data)
    print("student added successfully !!")
    repeat = input("do you want to continue?(y/n)")
    return True if repeat.lower() == "y" else False