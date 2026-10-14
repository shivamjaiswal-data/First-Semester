# accept the name and check if its palindrome write code to check if the given name is palindrome or not and use simple code 
s = input("Enter a word: ").lower()
print("Palindrome")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



# s = input("Enter a word: ").lower()
# print("Palindrome" if s == s[::-1] else "Not a palindrome")