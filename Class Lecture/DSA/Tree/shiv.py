numbers = [12, 45, 23, 67, 34, 89, 67]

largest = numbers[0]
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print("Largest:", largest)
print("Second Largest:", second_largest)