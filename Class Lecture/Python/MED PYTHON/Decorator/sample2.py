def mydecorate(func):
    def innerfunc():
        print ("Pyhton code is Started")
        func()
        print("Python code is Ended ")
    return innerfunc

@mydecorate
def outerfuc():
    a =  10
    b = 20
    print("Hello Everyone ")
     


outerfuc()
