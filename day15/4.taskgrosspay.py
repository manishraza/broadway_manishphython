# WAP to prompt the user for hours and rate per hour using input to compute
# gross pay. Pay the hourly rate for the hours up to 40 and 1.5
#times the hourly rate for all hours worked above 40 hours. Use 45
#hours and a rate of 10.50 per hour to test the program (the pay should be
#498.75). You should use input to read a string and float) to convert the string
#to a number.
# Prompt the user for input

hours_str = input("Enter the number of hours worked: ")
rate_str = input("Enter the hourly rate: ")

# Convert input strings to numbers
hours_worked = float(hours_str)
hourly_rate = float(rate_str)

# Calculate gross pay
if hours_worked <= 40:
    gross_pay = hours_worked * hourly_rate
else:
    regular_pay = 40 * hourly_rate
    overtime_pay = (hours_worked - 40) * 1.5 * hourly_rate
    gross_pay = regular_pay + overtime_pay

# Display the result
print("Gross pay:", gross_pay)
