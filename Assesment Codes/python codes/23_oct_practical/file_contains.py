#open file in read mode
f=open("stud.txt","r")
#get all names from file
names=f.readlines()
lst = []
#iterate over all names in file
for name in names:
 if 'a' in name or 'A' in name:
  lst.append(name)
print(lst)
#close file
f.close()