numbers = [1, 22, 53, 7, 654, 13, 71, 14]

# odds = [i for i in numbers if i % 2 != 0]
odds = list(filter(lambda number: number % 2 != 0, numbers))

print(numbers)
print(odds)
