s = input("Enter a sentence:\n")

words = s.split()

longest = words[0]
shortest = words[0]

for word in words:

    if len(word) > len(longest):
        longest = word

    if len(word) < len(shortest):
        shortest = word

print("Longest word is :", longest)
print("Shortest word is :", shortest)