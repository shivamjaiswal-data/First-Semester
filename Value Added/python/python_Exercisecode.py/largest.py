numbers = [12, 45, 23, 67, 34, 89, 10]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number is:", largest)