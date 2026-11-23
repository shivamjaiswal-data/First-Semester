# from threading import Thread
# def task():
#     print("Tread is running ")
# #create thread 
# t =Thread(target= task)

# #Start thread 
# t.start 
# #Waiting for completion
# t.join 

# print("Main program ends")
# # Jaoin makes a thread while wait untilll 



from threading import Thread
from time import sleep

def task():
    for i in range(3):
        print(i)
        sleep(i)

t = Thread(target=task)

t.start()
t.join()

print("End program")





from threading import Thread
import time 
def number():
    for i in range ():
        print()


