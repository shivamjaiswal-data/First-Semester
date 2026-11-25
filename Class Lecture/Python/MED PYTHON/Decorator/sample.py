# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello Sally"

# print(myfunction())




def myfunction_upper(func):
    def innnerfunct(args):
        print("Your code has started Now  ")
        func(args) 
        print("Your code is going to End ")
       
        return 
         
    return innnerfunct


@myfunction_upper
def hii(args):
    return print(args.upper())
    
hii("Shivam")



# def myfunction_upper(func):
#     def innnerfunct():
#          print("Thank you for using this ")
#          return func() 
#     return innnerfunct


# @myfunction_upper
# def hii():
#     num = "Shivam"
#     print(num.upper())

# hii()

