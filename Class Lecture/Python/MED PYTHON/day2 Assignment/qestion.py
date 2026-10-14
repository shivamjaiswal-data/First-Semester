#write a program to read a file and count how many vowels are present in content
f = open("file.txt", "r")
content = f.read()

vowel_count = 0
vowels = "aeiouAEIOU"

for char in content:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the file:", vowel_count)

f.close()

# Read all lines from a file into a list .print the total number of lines and dispaly the 2nd and 4th line.
f = open("file.txt", "r")

lines = f.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 4:
    print("2nd line:", lines[1])
    print("4th line:", lines[3])

f.close()

#Take a sentence from from the user,split it into words ,and store then in list .print the longest word.
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)

"""4 Read a file,split its contents into words, and store them in a list
  1 , print the total number of words.
2 ,print all unique words.  """
f = open("file.txt", "r")

content = f.read()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)

f.close()