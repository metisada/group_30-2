data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for simvol in data_tuple:
    if type(simvol) == str:
            letters.append(simvol)
    else:
            numbers.append(simvol)

numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(2, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[7] = 'c'
numbers = [x**2 for x in numbers]

letters = tuple(letters)
numbers = tuple(numbers)

print(letters)
print(numbers)
