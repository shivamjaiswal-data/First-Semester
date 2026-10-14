'''
create a heterogeneous list of numbers and names.split the list from  highest number
use a split method to break the list into two parts, one list with he highest number and 
 the other with less than or equal to the highest number
  
 ''' 
lst = [5, "Alice", 35, "Bob", 15, "Charlie", 20, "David", 12, "Eve"]
high= []
for value in lst :
    if isinstance(value,int):
        high.append(value)
highest = max(high)

index = lst.index(highest)
part1 = lst[index:]
part2 = lst[:index]

print("List  with highest number " ,part1)
print("list with remaining", part2)

# lst = [5, "Alice", 35, "Bob", 15, "Charlie", 20, "David", 12, "Eve"]

# numbers = []
# for value in lst:
#     if isinstance(value, int):
#         numbers.append(value)

# high = max(numbers)

# index = lst.index(high)
# part1 = lst[index:index+1]
# part2 = lst[:index] + lst[index+1:]

# print("Highest number:", part1)
# print("Remaining list:", part2)

# 