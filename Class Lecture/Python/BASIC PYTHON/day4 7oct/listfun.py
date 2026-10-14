# list i want  to apply sum and count and sorting methods on list
my_list = [1, 2, 3, 4, 5]
print("Sum:", sum(my_list))
print("Count:", len(my_list))
my_list.sort()
print("Sorted:", my_list)
#and i want to apply descending order on list
my_list.sort(reverse=True)
print("Descending:", my_list)

#create a list of 10 numbers and Display the sum of laste four numbers in the list
numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
last_four_sum = sum(numbers[-4:])
print("Sum of last four numbers:", last_four_sum)
#remove the items from the list located at index 2 and 5 position
del numbers[2]
del numbers[5]
print("List after removing items at index 2 and 5:", numbers)   
#print the difference of highest and lowest number in the list
print("Difference between highest and lowest number:", max(numbers) - min(numbers))

#append a new element in the list which is half of the item of third position in the list
numbers.append(numbers[2] / 2)
print("List after appending half of the third item:", numbers)
#print sum  of first 10 even number in the list 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Sum of first 10 even numbers:", sum(even_numbers[:10]))
#Accept two values  S And N .Print squar of N numbers starting from S
S = int(input("Enter the starting number S: "))
N = int(input("Enter the number of values N: "))
squares = [i**2 for i in range(S, S+N)]
print("Squares of", N, "numbers starting from", S, ":", squares)
#Reverse the Accepted String and print it
string_input = input("Enter a string: ")
reversed_string = string_input[::-1]
print("Reversed string:", reversed_string)
#Accept the sentence from the User and count the vowels




#Remove Duplicate from list 



#Reverse the list 