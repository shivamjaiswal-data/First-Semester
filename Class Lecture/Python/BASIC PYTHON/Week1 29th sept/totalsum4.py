num = int(input(" How many numbers you want to enter : \n"))

lst = []
sum = 0
for i in range (num):
    s =int(input("Enter your Numbers :\n"))
    lst.append(s)
for j in lst :
    sum = sum +j
print(f"Total sum of list {lst}\n {sum}")
