f1=open("stud.txt","r")
#open 2nd file in write name
f2=open("processed_names.txt","w")
#get all names from file
names=f1.readlines()
li=[]
#iterate over all names
for name in names:
 #check if name is already present in list or not
 if name not in li:
   li.append(name)
#sort list according to length of name
for i in range(len(li)):
 for j in range(i):
    if len(li[i])<len(li[j]):
     li[i],li[j]=li[j],li[i]
#write list content to file
for i in range(len(li)):
 f2.write(li[i])
