# def ad():
#     a = 10
#     b = 20 
#     return a+ b 
# print(ad())



# '''
# function name 


# '''

# def hello ():
#     return "Hello World"
#     print("Sujal")

# print(hello())


# def add(a,b):
#     return a + b 
# add(10,20)

# def add ():
    # kk=("hh")


# def add(a="sfgg",b=44):
#     return a + b 
# print(add())

def student(name, age=22):
    print(name, age)

student("Shivam")
student("Rahul", 24)
# Only Positional 
#it is the imp one code 


def add(a , b , c, * ,d,f=0):
    return a+b+c+d+f

print(add(10,20,30,f=50,d=40))

def show(*name):
    b=name 
    return b 
print(show(10,"aad",4444)[1])
# return sum of all arguments




def show(*sum):
    total = 0 
    for i in sum: 
        total = total +  i 
    return total 
print(show(10,20,30,40))
inp = int(input("Enter what is the lenght of your addition list "))
num1 = []
for i in range(inp):
    s = int(input("Enter the values "))
    num1.append(s)

def show(*num):
    total = 0
    for i in num:
        total  = total+ i 
    return total
print(show(*num1))
    

