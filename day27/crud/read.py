import json
filename = "student.json"
def read_student(student_id):
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
        student = list(filter(lambda x: x["id"] == student_id, students))
        if student:
            student = student[0]
            print(student)
        else:
            print("no matching student id")
        repeat = input("do you want to continue?(y/n)")
        return True if repeat.lower() == "y" else False
