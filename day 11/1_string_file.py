# we can format  strings using f-strings
name = input("enter your name")
language = input("enter your language")
message = (f"hello i am {name}."
          f"i am learning {language}")
print(message)


name = input("enter your name")
age = int(input("enter your age"))
message = 'i am %s and i am %d years old' % (name, age)
print(message)

name = input("enter your name")
age = int(input("enter your age"))
message = f"hello i am {name}and i am {age}years old"
print(message)

#### using format() method ####
message = "i am {} and i am {} years old."
result = message.format(name,age)
print(result)


message = "i have {1} ,{0}, and {2} in my bag." .format('book' ,'pen', 'copy')
print(message)

## it raises error
# message = "i have {1} ,{0}, and {2} in my bag." .format('book' ,'pen')
# print(message)
#here place
message = "i have {} , and {} in my bag." .format('book' ,'pen', 'copy','pencil')
print(message)








