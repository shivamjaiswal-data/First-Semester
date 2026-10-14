
s = input("Enter a sentence:\n")

words = s.split()

for word in words:
    print(word[::-1], end=" ")