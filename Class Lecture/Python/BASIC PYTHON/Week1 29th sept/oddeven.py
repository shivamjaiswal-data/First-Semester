num = int(input("Enter How many numbers you write in the List :\n"))
lst =[]
for  i in range (num):
    n = int(input("Enter the numbers:"))
    lst.append(n)
countofodd=0
countofeven=0
for i in lst:
    if i%2 == 0:
        countofeven=countofeven+1
    else:
        countofodd=countofodd+1
print(countofeven)
print(countofodd)
    

