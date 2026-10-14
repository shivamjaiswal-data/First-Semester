with open ("newfile.txt","w") as f :
    f.write("\n Now this is the new last line ")
    f.writelines("\n multiple lines \n can be added \n using write line method")
with open ("newfile.txt") as f :
    print(f.read())