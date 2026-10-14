print("Output of loop ")
for i in range (11):
    if i %2 != 0 :
        print(i)

# printing the table of odd number 

print("Output of table of odd number 1 to 10 ")
for i in range(1, 11):
    if i % 2 != 0:
        for j in range(1, 11):
            print(i, "x", j, "=", i * j)
        print()


        