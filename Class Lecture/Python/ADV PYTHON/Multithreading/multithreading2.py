
from threading import Thread
from time import sleep

# Yeh function thread ke andar execute hoga
def student():
    for i in range(1, 4):
        print("Student is studying:", i)
        sleep(1)  # Yeh 1 second ke liye program ko rokega

# Yeh function bhi ek alag thread mein chalega
def teacher():
    for i in range(1, 4):
        print("Teacher is teaching:", i)
        sleep(1)  # Yeh bhi 1 second wait karega

# Yeh dono threads create kar rahe hain
t1 = Thread(target=student)
t2 = Thread(target=teacher)

# Yeh dono threads ko start karega
t1.start()
t2.start()

# Yeh wait karega jab tak dono threads complete nahi ho jaate
t1.join()
t2.join()

# Yeh tabhi print hoga jab dono threads complete ho jayenge
print("End of program")
