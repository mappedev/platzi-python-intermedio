from functools import reduce


numbers = [2, 2, 2, 2, 2]

# all_multiplied = 1
# for number in numbers:
#     all_multiplied *= number
all_multiplied = reduce(lambda x, y: x * y, numbers)

print(numbers)
print(all_multiplied)
