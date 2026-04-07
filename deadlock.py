import time

tugas1= False
tugas2= False

def thread1_step():
    global tugas1, tugas2
    
    if not tugas1:
        print("Thread 1: mengambil lock1")
        tugas1 = True
        return "hold"
    
    elif tugas1:
        print("Thread 1: menunggu lock2")
        return "wait"

def thread2_step():
    global tugas1, tugas2
    
    if not tugas2:
        print("Thread 2: mengambil lock2")
        tugas2= True
        return "hold"
    
    elif tugas2:
        print("Thread 2: menunggu lock1")
        return "wait"

for i in range(10):
    print(f"\niterasi {i+1}")
    
    t1 = thread1_step()
    time.sleep(0.5)
    
    t2 = thread2_step()
    time.sleep(0.5)
    
    if t1 == "wait" and t2 == "wait":
        print("\n terjadi deadlock!!!")
        break