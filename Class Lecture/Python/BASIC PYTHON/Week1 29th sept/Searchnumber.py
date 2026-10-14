num = int(input("Enter How many numbers you write in the List :\n"))
lst =[]
for  i in range (num):
    n = int(input("Enter the numbers:\n"))
    lst.append(n)
fnum=int(input("Enter what number do you want to find out\n"))
for j in lst:
    if fnum == j:
        print(f"Yes ,{fnum} is present in this list and that place is ",j)
        break
# this part gave me alot of hectic
else :
    print(f"{fnum} is not present in this lst")

