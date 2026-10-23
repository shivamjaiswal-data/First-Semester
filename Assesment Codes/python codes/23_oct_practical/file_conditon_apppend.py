f1 = open("stud.txt" ,"r")
#opening a second file as write mode
f2 = open("stud2.txt","w")
#get all names from first file
names=f1.readlines()
#iteratine all the names stored in names file using for
for name in names :
    if (len(name)-1)>5:
        f2.write(name)

print("Filtering Completed")
#close both files
f1.close()
f2.close()