#open file in read mode
f=open("stud.txt","r")
l = []
#get all names from file
names=f.readlines()
for name in names :
 l.append(name.strip())

#iterate over each name
for name in l:
 print(name)
 #print length of name
 print("Length Of Name",len(name)-1)
 #print first charecter of name
 print("First Charecter:",name[0])
 #print last charecter of name
 print("Last Charecter:",name[-1])
 #check if name is palindrome
 print("Is palindrome:",name==name[::-1])
 print()
#close file
f.close()
