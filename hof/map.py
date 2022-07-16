numbers = [1, 2, 3, 4, 5]

# squares = [i**2 for i in numbers]
squares = list(map(lambda number: number**2, numbers))

print(numbers)
print(squares)
