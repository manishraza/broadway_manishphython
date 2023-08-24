try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 + num2
    print("The sum of {} and {} is {}".format(num1, num2, result))
except ValueError:
    print("Invalid input. Please enter valid numbers.")
