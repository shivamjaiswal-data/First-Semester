with open ("myfile1.text") as f :
    print("output using for")
    for i in f :
        print(i)
with open("myfile1.txt","r") as f:
    f.write("\n Newly Added contents in div b ")
