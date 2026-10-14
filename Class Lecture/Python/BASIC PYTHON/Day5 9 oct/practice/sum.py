print("Sum of digit of a list of numbers ")
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = sum(lst)
print(f"The sum of digits in the list is: {sum}")   

# sum of digit in the list of numbers using for loop
sum = 0
for num in lst:
    sum += num
print(f"The sum of digits in the list is: {sum}")   