#counting a vowels in words without using for loop

tex = input("Enter a Word or Line\n ")
if tex.isalpha():
    vowels = "aeiouAEIOU"
    count = sum(1 for char in tex if char in vowels)
    print("Number of vowels in the word:", count)
else:
    print("Please enter a valid word containing only letters.")
    