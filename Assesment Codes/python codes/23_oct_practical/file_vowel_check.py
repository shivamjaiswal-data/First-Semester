f = open("stud.txt","r")
vowels=['a','e','i','o','u','A','E','I','O','U']
#get all names in file
names = f.readlines()
lst = []
#iteratine all the names stored in names file using for loop
for name in names :
 #checking if first letter of name present in vowels
 if name[0] in vowels :
   lst.append(name)
print(lst)