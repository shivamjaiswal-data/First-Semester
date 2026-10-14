#print sum  of first 10 even number in the list 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = [x for x in lst if x % 2 == 0]
print("Sum of first 10 even numbers:", sum(even_numbers[:10]))