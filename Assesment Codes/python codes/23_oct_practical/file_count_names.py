f=open("stud.txt","r")
#create dictionary
count={}
#get all names from file
names=f.readlines()
#iterate over each name
for name in names:
    if name in count:
      count[name]+=1
 #else set it to one
    else:
      count[name]=1
#print name and its frequency
print(count)
#close file
f.close()
