
n = 7

for i in range(n):
    for j in range(n):
        if i == 3 or j == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()