# num = int(input("Enter How many numbers you write in the List :\n"))
# lst =[]
# for  i in range (num):
#     n = int(input("Enter the numbers:"))
#     lst.append(n)
# largest =lst[0]
# for i in lst:
#     if i > largest:
#         largest = i

# print(largest)

# second_largest = lst[0]
# for i in lst:
#     if i > second_largest:
#         if i != largest:
#             second_largest = i
        

arr =[10,12,34,56,34,5,65,44,34,65]
max=min =arr[0]
smin=smax=arr[0]
for num in arr :
    if num > max:
        smax=max
        max=num
    elif(num>max and num!=max):
        smax=num
    if num<min:
        smin=min
        min=num


