from array import*

val  = array ('i' ,[1,2,3,4,56,6,77,8])
# for i in range (0 ,len(val)) :
#     print(val[i], end =" ")
# print('\n')

# val.reverse()

# for i in range (0,len(val)):
#     print(val[i], end=" ")


# val.insert(1, 50)

# want to make a copy of array 
coppyArray = array(val.typecode , (x*2 for x in val) )
for i in range (0,len(val)):
    print(coppyArray[i], end=" ")



