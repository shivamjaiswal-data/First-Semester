#create a list of 10 numbers and Display the sum of laste four numbers in the list
lst = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(sum(lst[:-4]))

#remove the items from the list located at index 2 and 5 position
print(lst.pop(1))
print(lst.pop(4))
#print the difference of highest and lowest number in the list
print("the difference of highest and lowest number in the list", max(lst)-min(lst))
print(lst)
#append a new element in the list which is half of the item of third position in the list
print("New element in the list which is half of the item of third position in the list",lst.append(lst[3]/2))
print(lst)