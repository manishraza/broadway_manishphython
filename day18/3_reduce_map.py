# reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce
def sum_all(x, y):
    return x + y
result = reduce(sum_all, nums)
print(nums)
print(result)
sum = lambda