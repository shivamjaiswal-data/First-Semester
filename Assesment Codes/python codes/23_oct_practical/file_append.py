#open file as read mode
f = open("stud.txt","r")
#get all names in file
names = f.readlines()
#Storing all names
lst = []
for name in names :
 #checking is name in a list have 5 char
 if (len(name)-1) > 5:
  
   lst.append(name)
print(lst)
