
text = "hey! , hows is it going??"
#2 . convert to lower case 
print("upper case" , text.upper())
#3 . capitilize first letter 
text = text.strip()
print("Capitilize First letter" , text.capitalize())
#4 . Title case 
print(text.title())
#5 . count Occurance of a substtring 
print("Letter C occurrs" , text.count("c" ), "times in text")
 # find the position of substring 
print("Possition of IMCC text is ",text.find("IMCC"))
#6 . Replacing a sub string 
print(text.replace("hey","Python MAGIC"))
#7 . check id string start or end with certain substring 
print(text.startswith(" we"))
print(text.endswith("! "))
#8 . split string in to list by a decliner
print("hey",text.split())
#9 Join Words
word = ['python ' ,'is', 'magic']
print(" ".join(word))