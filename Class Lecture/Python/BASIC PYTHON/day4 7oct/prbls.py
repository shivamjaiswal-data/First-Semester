text = "haha"
print(text * 3)

text = "nice"
print(text)

# Finding occurrences of letter 'a' in any word or line
try:
    tex = input("Enter a word or line: ")
except EOFError:
    tex = "banana"
print(tex.count("a"))

# Splitting any word into two parts
tex = "ShivamJaiswal"
mid = len(tex) // 2
print(tex[:mid], tex[mid:])
