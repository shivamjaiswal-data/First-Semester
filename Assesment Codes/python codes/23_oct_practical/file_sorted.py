#opening a file as read mode
f1=open("stud.txt","r")
#get alll names from file
names=f1.readlines()
#sort name in ascending order and print
name=sorted(names)
print(name)
#close file
f1.close()
