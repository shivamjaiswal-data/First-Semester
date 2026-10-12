from array import*

val  = array ('i' ,[1,2,3,4,56,6,77,8])
for i in range (0 ,len(val)) :
    print(val[i], end =" ")
print('\n')

val.reverse()

for i in range (0,len(val)):
    print(val[i], end=" ")