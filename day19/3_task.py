# First 20 multiples of 3

for i in range(1, 21):
    print(3 * i)


n = 1
while n <= 20:
    print(3 * n)
    n += 1


# first 50 even numbers

n = 0
even_number_count = 0
while even_number_count != 50:
    if n % 2 == 0:
        print(n)
        even_number_count += 1
    n += 1
