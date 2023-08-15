# filter
# filter() is a built-in function

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def get_even_nums(data):
    return data % 2 == 0
result = filter(get_even_nums,nums)
print(nums)
print(list(result))


def get_multiply_of_5_nums(data):
    return data % 5 == 0
result = filter(get_multiply_of_5_nums,nums)
print(nums)
print(list(result))
